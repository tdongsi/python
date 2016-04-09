#!/usr/local/bin/python
import sys


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


def main():
    PROJECT_HOME = "/Users/cdongsi/Hub/python/CodeJam"
    solver = RevengeOfPancakes(PROJECT_HOME + "/data/B-large.in")
    with open("out.txt", "w") as f:
        solver.solve(output=f)

if __name__ == "__main__":
    main()