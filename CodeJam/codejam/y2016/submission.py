#!/usr/local/bin/python
import sys

from collections import Counter


class GetDigits(object):
    """
    https://code.google.com/codejam/contest/11254486/dashboard#s=p0
    """

    WORDS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    CHAR_DIGIT_1 = {"Z" : 0, "W" : 2, "U": 4, "X": 6, "G": 8}
    CHAR_DIGIT_2 = {"R": 3, "F": 5, "S" : 7}
    CHAR_DIGIT_3 = {"O": 1, "I": 9}

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
        cnt = self._get_counter(istring)

        number = []

        # TODO: Use function to avoid duplicate codes
        # Find digits 0, 2, 4, 6, 8
        for key in self.CHAR_DIGIT_1.keys():
            word_count = self.counters[self.CHAR_DIGIT_1[key]]
            while cnt[key] > 0:
                cnt.subtract(word_count)
                number.append(self.CHAR_DIGIT_1[key])

        # Find digits 3, 5, 7
        for key in self.CHAR_DIGIT_2.keys():
            word_count = self.counters[self.CHAR_DIGIT_2[key]]
            while cnt[key] > 0:
                cnt.subtract(word_count)
                number.append(self.CHAR_DIGIT_2[key])

        # Find digits 1, 9
        for key in self.CHAR_DIGIT_3.keys():
            word_count = self.counters[self.CHAR_DIGIT_3[key]]
            while cnt[key] > 0:
                cnt.subtract(word_count)
                number.append(self.CHAR_DIGIT_3[key])

        number.sort()
        return ''.join([str(e) for e in number])

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
    PROJECT_HOME = "/Users/tdongsi/Hub/python/CodeJam"
    solver = GetDigits(PROJECT_HOME + "/data/GetDigits.txt")
    with open("out.txt", "w") as f:
        solver.solve(output=f)

if __name__ == "__main__":
    main()