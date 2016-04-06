'''
Created on May 11, 2014

@author: tdongsi
'''

from __future__ import print_function
import sys
from fractions import gcd

def generation_count(num, dem):
    MAX_COUNT = 40
    count = 0
    # Normalize num and dem
    my_gcd = gcd(num,dem)
    num //= my_gcd
    dem //= my_gcd
#     print ("%d %d" % (num, dem))

    gen = 0
    found_ancestor = False
    if num == dem:
        return 0
    
    while count <= MAX_COUNT:
        num *= 2
        count += 1
        if (num > dem):
            gen = gen if found_ancestor else count
            found_ancestor = True
            num -= dem
        elif (num == dem):
            gen = gen if found_ancestor else count
            found_ancestor = True
            break
        else:
            pass

    if (count == MAX_COUNT+1):
        return 'impossible'
    else:
        return str(gen)
#     if num == 1:
#         count = math.log2(dem)
#         if float(count).is_integer():
#             return str(int(count))
#         else:
#             return 'impossible'
#     else:
#         pass


def solve( input_filename, f = sys.stdout):
    try:
        with open( input_filename, "r") as input:
            test_case_num = int(input.readline().strip())
            
            for i in range(test_case_num):
                
                # parsing input
                fraction = [int(x) for x in input.readline().split('/')]
                    
                # call methods to solve problem
                solution = generation_count(fraction[0], fraction[1])
                print( "Case #%d: %s" % (i+1, solution), file = f)
            
    except IOError:
        print ("Error opening file %s" % input_filename, file=sys.stderr)


if __name__ == '__main__':
    
    f = open("output.txt", 'w')
    input_filename = "../../data/PartElfSample.txt"
#     input_filename = "../data/A-small-attempt0.in"
#     input_filename = "../data/A-large.in"
    
    solve(input_filename, f)
    solve(input_filename)