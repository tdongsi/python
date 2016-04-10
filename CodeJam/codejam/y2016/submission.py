#!/usr/local/bin/python
import sys

import prime as pr

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


def main():
    PROJECT_HOME = "/Users/cdongsi/Hub/python/CodeJam"
    solver = CoinJam(PROJECT_HOME + "/data/CoinJam.txt")
    with open("out.txt", "w") as f:
        solver.solve(output=f)

if __name__ == "__main__":
    main()