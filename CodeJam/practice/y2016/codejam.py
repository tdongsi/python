"""
Practice for Code Jam 2016
"""

import sys


class ReverseWords(object):
    """
    https://code.google.com/codejam/contest/351101/dashboard#s=p1
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


class StoreCredit(object):
    """
    https://code.google.com/codejam/contest/351101/dashboard#s=p0
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


def main():
    pass


if __name__ == "__main__":
    main()