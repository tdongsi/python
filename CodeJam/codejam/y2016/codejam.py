
import sys


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