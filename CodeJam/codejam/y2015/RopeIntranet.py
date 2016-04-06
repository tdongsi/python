"""
Created on May 10, 2014

"""

from __future__ import print_function
import sys

def prod(pos1, pos2):
    return (pos1[0]-pos2[0])*(pos1[1]-pos2[1])

def intersect_count(wires):
    """
    Naive solution for counting number of intersections
    """
    count = 0
    for i in range(len(wires)):
        for j in range(i+1, len(wires)):
            if prod(wires[i], wires[j] ) < 0:
                count += 1
    return count


def solve( input_filename, f = sys.stdout):
    try:
        with open( input_filename, "r") as input:
            test_case_num = int(input.readline().strip())
            
            for i in range(test_case_num):
                
                # parsing input
                N = int(input.readline().strip())
                wires=[]
                for j in range(N):
                    wire = [int(x) for x in input.readline().split()]
#                     print (wire, file=f)
                    wires.append(wire)
                    
                # call methods to solve problem
                print( "Case #%d: %d" % (i+1, intersect_count(wires)), file = f)
            
    except IOError:
        print ("Error opening file %s" % input_filename, file=sys.stderr)


if __name__ == '__main__':
    
    f = open("output.txt", 'w')
    input_filename = "../../data/RopeIntranet.txt"
#     input_filename = "../data/A-small-practice.in"
#     input_filename = "../data/A-large-practice.in"
    
    solve(input_filename, f)
    solve(input_filename)