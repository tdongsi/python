'''
Created on Apr 12, 2014

@author: EpipolarGineer

To solve the problem and submit, use the following:
python MagicTrick.py -inputfile A-small-attempt0.in > out.txt
'''

import argparse

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Google Code Jam 2014: Magic Trick')
    parser.add_argument('-inputfile', action='store', default='../data/MagicTrickSample.txt', dest='filename')
    args = parser.parse_args()
    
#     print ('Processing file %s' % args.filename)
    infile = open(args.filename, 'r')
    
    test_number = int(infile.readline())
#     print( 'Test number: %d' % test_number)
    
    SIZE = 4
    
    for i in range(0,test_number):
        
        # read the first annswer
        first_answer = int(infile.readline())
        first_row = []
        
        for j in range(0, SIZE):
            if (j == first_answer-1 ):
                first_row = infile.readline().split()
            else:
                infile.readline()
                
        
        # read the second answer
        second_answer = int(infile.readline())
        second_row = []
        
        for j in range(0, SIZE):
            if (j == second_answer-1 ):
                second_row = infile.readline().split()
            else:
                infile.readline()
                
        # Find the intersection
        intersect = set(first_row).intersection(second_row)
        
        if len(intersect) == 1:
            print ("Case #%d: %s" % (i+1, intersect.pop()))
        elif len(intersect) > 1:
            print ("Case #%d: Bad magician!" % (i+1))
        else:
            print ("Case #%d: Volunteer cheated!" % (i+1))
            
            