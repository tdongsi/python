#!/usr/buildtools/bin/python2.7

'''
Created on Feb 20, 2014

@author: cuongd

USAGE: python scriptName -infile agent.logfile

Take the given agent log file, find the starting and ending time.
The time is marked with the following message "No pipeline work found... agent idle".
Print out the times and elapsed time in seconds. 
'''

import argparse
import re
from datetime import datetime

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Compute average time')
    parser.add_argument('-inputfile', action='store', default='../data/sampleTime.txt', dest='filename')
    args = parser.parse_args()
    
    
    print ('Processing file %s' % args.filename)
    
    findTime = re.compile('\d{2}:\d{2}:\d{2}')
    startString = ''
    endString = ''
    idleString = 'No pipeline work found... agent idle'
    startFlag = True
    
    try:
        with open( args.filename, "r") as f:
            lines = f.readlines()
            
            for line in lines:
                if ( line.find(idleString) >= 0 ):
                    if ( startFlag ):
                        startFlag = False
                        startString = line
                    endString = line
                    
            startTimeString, = findTime.findall(startString)
            endTimeString, = findTime.findall(endString)
            startTime = datetime.strptime( startTimeString, '%H:%M:%S' )
            endTime = datetime.strptime( endTimeString, '%H:%M:%S' )
            diff = endTime - startTime
            
            print ( 'Agent time: %s %s diff: %d sec \n' % (startTimeString, endTimeString, diff.total_seconds()) )
            
    except IOError:
        print ('Error opening file')
