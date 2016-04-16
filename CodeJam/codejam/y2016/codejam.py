import copy
from collections import deque, defaultdict
import sys

import matplotlib.pyplot as plt
import networkx as nx

import prime as pr

class Bff(object):
    """
    https://code.google.com/codejam/contest/4304486/dashboard#s=p2
    """
    def __init__(self, filename):
        """ Initialize with the given input file.

        :param filename: input file path
        :return:
        """
        self._filename = filename
        pass

    def solve(self, output=sys.stdout):
        """ Handle input and output before calling an internal method to solve the problem.

        :param output: specify output to file or screen.
        :return:
        """
        try:
            with open(self._filename, 'r') as f:
                lines = f.readlines()
                num = int(lines[0])

                for case_num, idx in enumerate(xrange(2,len(lines),2), start=1):
                    # skip the first line
                    cycle_length = self._solve_bff(lines[idx].strip())
                    output.write("Case #%d: %d\n" %(case_num, cycle_length))
        except IOError:
            print "Error opening file"
        pass

    def _solve_bff(self, input):
        # Construct the directed graph
        bffs = [int(e.strip()) for e in input.split(' ')]
        nodes = [i+1 for i in xrange(len(bffs))]
        gr = nx.DiGraph()
        gr.add_nodes_from(nodes)
        gr.add_edges_from([e for e in zip(nodes, bffs)])

        max_length = 0
        tree = self._build_tree(bffs)
        # For each simple cycles in the graph
        for cycle in nx.simple_cycles(gr):
            if len(cycle) == 2:
                # If cycle length is two, we can add more nodes
                path_length = self._find_path_length(cycle, tree)
                if path_length > max_length:
                    max_length = path_length
            elif len(cycle) > max_length:
                # If cycle length is three, we cannot add more nodes
                max_length = len(cycle)

        # nx.draw_networkx(gr)
        # plt.show()

        return max_length

    def _find_path_length(self, mutual_bff, tree):
        """ Find length due to mutual bff.

        If two BFFs form a cycle of two, we can keep adding BFFs to both sides to form larger cycle.
        """
        # Remove the cycle from the general tree.
        left_tree = copy.deepcopy(tree)
        left_tree[mutual_bff[0]].remove(mutual_bff[1])
        right_tree = copy.deepcopy(tree)
        right_tree[mutual_bff[1]].remove(mutual_bff[0])

        left_length = self._tree_height(mutual_bff[0], left_tree)
        right_length = self._tree_height(mutual_bff[1], right_tree)

        return left_length + right_length

    def _build_tree(self, bff_list):
        """ Build the reverse tree: given BFF's ID, find the original ID.

        :param bff_list: List of BFFs, such that value at is BFF of i.
        :return:
        """
        tree = defaultdict(list)

        for idx, friend in enumerate(bff_list):
            tree[friend].append(idx+1)

        return tree

    def _tree_height(self, root, tree):
        # print root, tree.items()
        if root in tree and tree[root]:
            return max([self._tree_height(e, tree) for e in tree[root]]) + 1
        else:
            return 1


class LastWord(object):
    """
    https://code.google.com/codejam/contest/4304486/dashboard#s=p0
    """
    def __init__(self, filename):
        """ Initialize with the given input file.

        :param filename: input file path
        :return:
        """
        self._filename = filename
        pass

    def solve(self, output=sys.stdout):
        """ Handle input and output before calling an internal method to solve the problem.

        :param output: specify output to file or screen.
        :return:
        """
        try:
            with open(self._filename, 'r') as f:
                lines = f.readlines()
                num = int(lines[0])

                for i in xrange(num):
                    last_word = self._solve_last_word(lines[i+1].strip())
                    output.write("Case #%d: %s\n" %(i+1, last_word))
        except IOError:
            print "Error opening file"
        pass

    def _solve_last_word(self, word):
        q = deque(word[0])

        for c in word[1:]:
            if c >= q[0]:
                q.appendleft(c)
            else:
                q.append(c)
        return ''.join(q)


class CoinJam(object):
    """
    https://code.google.com/codejam/contest/6254486/dashboard#s=p2
    """

    def __init__(self, filename):
        """ Initialize with the given input file.

        :param filename: input file path
        :return:
        """
        self._filename = filename
        pass

    def solve(self, output=sys.stdout):
        """ Handle input and output before calling an internal method to solve the problem.

        :param output: specify output to file or screen.
        :return:
        """
        try:
            with open(self._filename, 'r') as f:
                lines = f.readlines()
                N, J = [int(ele) for ele in lines[1].strip().split(' ')]
                output.write("Case #1:\n")
                self._find_jam_coins(length=N, cases=J, output=output)
        except IOError:
            print "Error opening file"
        pass

    def _product(self, list_a, list_b):
        return sum([a*b for a, b in zip(list_a, list_b)])

    def _find_jam_coins(self, length, cases, output):

        TRIAL = 100

        bases = []
        for base in xrange(2, 11):
            base_mul = [base**i for i in range(length)]
            bases.append(base_mul)
        # print bases

        count = 0
        number = 1 << (length-1)
        number += 1

        while count < cases:
            num_string = bin(number)[2:]
            # Convert the binary string to a vector of 0 and 1
            num_lst = [int(e) for e in reversed(num_string)]
            flag = False
            factors = [0]*len(bases)

            for idx in xrange(len(bases)):
                value = self._product(num_lst, bases[idx])
                # print value
                factor = pr.find_factor(value, trial=TRIAL)

                if factor == 1:
                    flag = True
                    break
                else:
                    factors[idx] = factor

            number += 2
            if flag:
                continue
            else:
                output.write("%s %s\n" % (num_string, ' '.join([str(e) for e in factors])) )
                count += 1

        pass


class RevengeOfPancakes(object):
    """
    https://code.google.com/codejam/contest/6254486/dashboard#s=p1
    """

    def __init__(self, filename):
        """ Initialize with the given input file.

        :param filename: input file path
        :return:
        """
        self._filename = filename
        pass

    def solve(self, output=sys.stdout):
        """ Handle input and output before calling an internal method to solve the problem.

        :param output: specify output to file or screen.
        :return:
        """
        try:
            with open(self._filename, 'r') as f:
                lines = f.readlines()
                num = int(lines[0])

                for i in xrange(num):
                    idx = i + 1
                    out = self._solve_revenge_pancakes(lines[idx].strip())
                    output.write("Case #%d: %d\n" %(idx, out))
        except IOError:
            print "Error opening file"
        pass

    def _solve_revenge_pancakes(self, stack):
        """ Find the minimum number of flips to make all pancakes up.

        The idea: for a stack of N cakes,
        if the last cake is up (+), the problem is equivalent to solving the top N-1 cakes.
        if the last case is down (-), the problem is equivalent to solving the top N-1 cakes inverted + 1.

        :param stack:
        :return:
        """

        my_dict = { "+" : True, "-": False}
        count = 0
        # instead of inverting top (N-1) cakes, keep this flag to invert the top cakes if needed.
        flip = True

        for char in reversed(stack):
            # Check the bottom pancake first

            is_up = my_dict[char] if flip else not my_dict[char]
            if not is_up:
                # if the bottom pancake is "-"
                count += 1
                flip = not flip
            else:
                # do nothing
                pass

        return count


class CountingSheep(object):
    """
    https://code.google.com/codejam/contest/6254486/dashboard#s=p0
    """

    def __init__(self, filename):
        """ Initialize with the given input file.

        :param filename: input file path
        :return:
        """
        self._filename = filename
        pass

    def solve(self, output=sys.stdout):
        """ Handle input and output before calling an internal method to solve the problem.

        :param output: specify output to file or screen.
        :return:
        """
        try:
            with open(self._filename, 'r') as f:
                lines = f.readlines()
                num = int(lines[0])

                for i in xrange(num):
                    idx = i + 1
                    out = self._solve_counting_sheep(int(lines[idx].strip()))
                    if out == -1:
                        output.write("Case #%d: INSOMNIA\n" %(idx))
                    else:
                        output.write("Case #%d: %d\n" %(idx, out))
        except IOError:
            print "Error opening file"
        pass

    def _solve_counting_sheep(self, number):
        """ Find the last number before Bellatrix falls asleep.

        :param number: starting number
        :return: -1 if Bellatrix will have INSOMNIA
        """

        if number == 2 * number:
            # Could not figure out any other case that gives INSOMNIA
            return -1
        else:
            curr_number = 0
            check = set()
            while len(check) < 10:
                # current number
                curr_number += number
                # Keep adding new unique digits into the set
                check |= set(str(curr_number))

            return curr_number

def main():
    pass


if __name__ == "__main__":
    main()