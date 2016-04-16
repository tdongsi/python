#!/usr/local/bin/python
import sys

from collections import deque


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


def main():
    PROJECT_HOME = "/Users/cdongsi/Hub/python/CodeJam"
    solver = LastWord(PROJECT_HOME + "/data/A-large.in")
    with open("out.txt", "w") as f:
        solver.solve(output=f)

if __name__ == "__main__":
    main()