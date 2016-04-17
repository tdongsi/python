"""
Practice for Code Jam 2016
"""

import math
import re
import sys


class Problem(object):
    """
    Base class for Code Jam problems.
    Specify the input file.
    """

    def __init__(self, filename):
        """ Initialize with the given input file.

        :param filename: input file path
        :return:
        """
        self._filename = filename
        pass


class ReverseWords(Problem):
    """
    https://code.google.com/codejam/contest/351101/dashboard#s=p1
    """

    def solve(self, output=sys.stdout):
        """ Handle input and output before calling an internal method to solve the problem.

        :param output: specify output to file or screen.
        :return:
        """
        try:
            with open(self._filename) as f:
                lines = f.readlines()

                N = int(lines[0])
                lines_iter = iter(lines)
                next(lines_iter)

                try:
                    for count in xrange(1, N+1):
                        output_string = "Case #%d" % count

                        my_string = next(lines_iter).strip()
                        words = my_string[::-1].split(' ')
                        reverse_words = ' '.join([word[::-1] for word in words])

                        output.write("%s: %s\n" % (output_string, reverse_words))
                except StopIteration:
                    print "Unexpected StopIteration error. Verify input file"

        except IOError:
            print "Error opening file %s" % self._filename
        pass


class StoreCredit(Problem):
    """
    https://code.google.com/codejam/contest/351101/dashboard#s=p0
    """

    def solve(self, output=sys.stdout):
        """ Handle input and output before calling an internal method to solve the problem.

        :param output: specify output to file or screen.
        :return:
        """
        try:
            with open(self._filename) as f:
                lines = f.readlines()

                N = int(lines[0])
                lines_iter = iter(lines)
                next(lines_iter)

                try:
                    for count in xrange(1, N+1):
                        output_string = "Case #%d" % count

                        credit = int(next(lines_iter))
                        item_num = int(next(lines_iter))
                        items = next(lines_iter).strip().split(' ')
                        # Convert to list of ints
                        items_int = [int(item) for item in items]
                        assert item_num == len(items_int)
                        first, second = self._solve_store_credit(credit, items_int)

                        output.write("%s: %d %d\n" % (output_string, first, second))
                except StopIteration:
                    print "Unexpected StopIteration error. Verify input file"

        except IOError:
            print "Error opening file %s" % self._filename

    def _solve_store_credit(self, credit, items_in):
        items = sorted(items_in)
        # keys store the index of item after sorting
        keys = sorted(range(len(items_in)), key=lambda s: items_in[s])

        i = 0
        j = len(items) - 1
        sum = items[i] + items[j]
        while sum != credit and i < j:
            if sum > credit:
                j -= 1
            else:
                i += 1
            sum = items[i] + items[j]

        first = keys[i]+1
        second = keys[j]+1
        return (first, second) if first <= second else (second, first)

    pass


class AlienLanguage(Problem):

    def solve(self, output=sys.stdout):
        """ Handle input and output before calling an internal method to solve the problem.

        :param output: specify output to file or screen.
        :return:
        """
        try:
            with open(self._filename, 'r') as f:
                lines = f.readlines()
                lines_iter = iter(lines)

                # First line
                line = lines_iter.next().split(' ')
                length, dict_count, test_count = [int(elem) for elem in line]

                # Construct dictionary
                dictionary = set([])
                for i in xrange(dict_count):
                    dictionary.add(lines_iter.next())

                # Process test cases
                for i in xrange(test_count):
                    test = lines_iter.next()
                    count = self._solve_alien_language(dictionary, test)
                    output.write("Case #%d: %d\n" % (i+1, count))
        except StopIteration:
            print "Unexpected StopIteration, check file"
        except IOError:
            print "Error opening file"
        pass

    def _solve_alien_language(self, dictionary, test):
        """ Solve by converting the test case to regular expression.

        :param dictionary:
        :param test:
        :return:
        """
        pattern = test.replace("(", "[").replace(")", "]")
        # print pattern
        matcher = re.compile(pattern)
        count = 0
        for entry in dictionary:
            if matcher.match(entry):
                count += 1
        return count


class AllYourBase(Problem):
    """
    https://code.google.com/codejam/contest/189252/dashboard#s=p0
    """

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
                    out = self._solve_all_your_base(lines[idx].strip())
                    output.write( "Case #%d: %d\n"%(idx, out) )
        except IOError:
            print "Error opening file"
        pass

    def _solve_all_your_base(self, line):
        """ Compute the minimum number, given the string

        Brute force algorithm:
        Most significant digit should be one.
        The next significant, different digit should be zero.
        Other digits: increment, starting from two for next significant digits.

        The base is the number of distinct digits + 1.
        """
        my_dict = {}
        digit_value = 1

        for char in line:
            if digit_value == 1:
                my_dict[char] = digit_value
                digit_value = 0
            elif char not in my_dict and digit_value == 0:
                my_dict[char] = digit_value
                digit_value = 2
            elif char not in my_dict:
                my_dict[char] = digit_value
                digit_value += 1

        base = max(len(my_dict),2)
        prod = my_dict[line[0]]
        for char in line[1:]:
            prod *= base
            prod += my_dict[char]

        return prod


class CenterOfMass(Problem):
    """
    https://code.google.com/codejam/contest/189252/dashboard#s=p1&a=0
    """

    def solve(self, output=sys.stdout):
        """ Handle input and output before calling an internal method to solve the problem.

        :param output: specify output to file or screen.
        :return:
        """
        try:
            with open(self._filename, 'r') as f:
                lines = f.readlines()
                num = int(lines[0])
                i_lines = iter(lines)
                i_lines.next()

                for case in xrange(num):
                    num_fly = float(i_lines.next())
                    sum_pos = [0, 0, 0]
                    sum_vel = [0, 0, 0]

                    for fly in xrange(int(num_fly)):
                        tokens = i_lines.next().strip().split(' ')
                        fly_pv = [int(token) for token in tokens]
                        # print fly_pv

                        sum_pos = [sumc + p for sumc, p in zip(sum_pos, fly_pv[:3])]
                        sum_vel = [sumc + v for sumc, v in zip(sum_vel, fly_pv[3:])]

                    pos_0 = [p/num_fly for p in sum_pos]
                    vel = [v/num_fly for v in sum_vel]
                    func_a = sum([a*b for a, b in zip(vel, vel)])
                    func_b = 2*sum([a*b for a, b in zip(vel, pos_0)])
                    func_c = sum([a*b for a, b in zip(pos_0, pos_0)])
                    d_min, t_min = self._solve_quadratic_min(func_a, func_b, func_c)

                    output.write("Case #%d: %f %f\n" % (case+1, d_min, t_min))

        except StopIteration:
            print "Unexpected stop. Check input file."
        except IOError:
            print "Error opening file"
        pass

    def _solve_quadratic_min(self, a, b, c):
        # print a, b, c
        if a == 0.0:
            t_min = 0.0
        else:
            t_min = max(0.0, -b/2.0/a)
        d_squared = a * t_min * t_min + b * t_min + c
        if d_squared > 0:
            d_min = math.sqrt(d_squared)
        else:
            # if d_squared is close to zero, it could be less than zero
            # due to floating point error.
            d_min = 0.0
        return d_min, t_min


def main():
    pass


if __name__ == "__main__":
    main()