
from collections import deque
import sys

import prime as pr


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