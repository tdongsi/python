#!/usr/local/bin/python
import sys

from collections import Counter


class GetDigits(object):
    """
    https://code.google.com/codejam/contest/11254486/dashboard#s=p0
    """

    WORDS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

    def __init__(self, filename):
        """ Initialize with the given input file.

        :param filename: input file path
        :return:
        """
        self._filename = filename
        self.counters = self._get_word_counters()
        pass

    def solve(self, output=sys.stdout):
        """ Handle input and output before calling an internal method to solve the problem.

        :param output: specify output to file or screen.
        :return:
        """
        try:
            with open(self._filename, 'r') as f:
                lines = f.readlines()

                for case_num, line in enumerate(lines[1:], start=1):
                    number = self._solve_digits(line.strip())
                    output.write("Case #%d: %s\n" % (case_num, number))

        except IOError:
            print "Error opening file"
        pass

    def _solve_digits(self, istring):
        cnt = Counter()
        for c in istring:
            cnt[c] += 1

        number = []
        for digit in xrange(len(self.WORDS)):
            while any(cnt.values()) and self._found_word(cnt, digit):
                cnt.subtract(self.counters[digit])
                number.append(str(digit))

        return ''.join(number)

    def _found_word(self, total, digit):
        word_counter = self.counters[digit]
        # print "%d: %s" % (digit, str(word_counter))
        for key in word_counter:
            if total[key] < word_counter[key]:
                return False

        return True

    def _get_word_counters(self):
        counters = [self._get_counter(word) for word in self.WORDS]
        # print counters
        return counters

    def _get_counter(self, word):
        counter = Counter()
        for c in word:
            counter[c] += 1
        return counter


def main():
    PROJECT_HOME = "/Users/cdongsi/Hub/python/CodeJam"
    solver = GetDigits(PROJECT_HOME + "/data/A-small-attempt0.in")
    with open("out.txt", "w") as f:
        solver.solve(output=f)

if __name__ == "__main__":
    main()