#!/usr/buildtools/bin/python2.7

'''
Created on Apr 1, 2014

@author: cuongd

USAGE: plotMemoryLogs.py -output plot.png -logFile1 file1.log -logFile2 file2.log
NOTE: the plot file name must have png extension.

TODO: We can extend to arbitrary list of log files. 
However, given the current log structure, 2+ log files are not presentable.

This script will plot memory usage parsed from log files into a png file.
The png file name is specified by the first argument.
The data files can be supplied as a list from the following arguments.
NOTE: It assumes certain knowledge of structure and format of the log file.


LOGGING: the script is ad-hoc, based on the log file
Need to adjust logging to make the script for robust 
Assume the memory log is at the end of the file.
Setting threadNum to 4 and it will fail.
'''



import re
import matplotlib.pyplot as plt
import argparse

def parseDataFile(filename, threadNum):

    f = open(filename)
    lines = f.readlines()
    
    searchThreadPhrase = 'Number of Threads: '
    searchThreadPhrase += str(threadNum)
    
    startingMemoryPhrase = 'Starting Memory Usage:'
    endingMemoryPhrase = 'End Memory Usage Log'
    
    # Flag of starting a test: "Number of Threads" entry in log.
    startFlag = False
    # Flag of starting memory recording: "Starting Memory Usage" in log.
    grabFlag = False
    startingMemory = 0
    # dataArray is an LoL
    dataArray = []
    # newRow is a row entry in that LoL
    newRow =[]
    count = 0
    
    # Find all positive floating integer
    # NOTE: To make this regex robust, when logging,
    # stringstream should use << std::fixed << std::setprecision(5)
    p = re.compile("\d+\.\d+")
    
    for line in lines:
        if line.find('QA_MEMORY_LOG') >= 0:
            # DEBUG
#             print count, line
            
            if not startFlag and line.find(searchThreadPhrase) >= 0:
                startFlag = True
                count += 1
                newRow = []
#                 print line

            elif startFlag and line.find(endingMemoryPhrase) >= 0:
                startFlag = False
                grabFlag = False
                dataArray.append(newRow)
                
            elif startFlag:                
                if not grabFlag and line.find(startingMemoryPhrase) >= 0:
                    grabFlag = True
                    floats = p.findall(line)
                    startingMemory = float(floats[0])
                    
                elif grabFlag:
                    floats = p.findall(line)
                    allocatedMemory = (float(floats[0]) - startingMemory)
                    newRow.append(allocatedMemory)
    #                 print allocatedMemory
                
    return dataArray      



if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description='Plot memory usage from log files.')
    # The default values are for testing
    parser.add_argument('-output', dest = 'plotFilename', action='store', default = 'MemoryLogging.png', help = 'File name of the plot (must end with .png)')
    parser.add_argument('-logFile1', dest = 'lcFilename', default = r"..\data\PerfLog_feature_OFF.txt", help = 'First log file with pre-defined structure')
    parser.add_argument('-logFile2', dest = 'scFilename', default = r"..\data\PerfLog_feature_ON.txt", help = 'Second log file with pre-defined structure')
    args = parser.parse_args()
    
    
    threadNumList = range(2,6)
    figure, plots = plt.subplots(len(threadNumList), 1, True )
    for num in threadNumList:
        
        idx = num - threadNumList[0]
        
        # Reading the data from file
        lcData = parseDataFile(args.lcFilename, num)
        scData = parseDataFile(args.scFilename, num)
        
        # Plotting local cache memory logging as red
        for row in lcData:
            p1, = plots[idx].plot(row, 'r-')
        
        # Plotting shared cache memory logging as green
        for row in scData:
            p2, = plots[idx].plot(row, 'g-')
            
        plots[0].legend( [p2, p1], ["Feature ON", "Feature OFF"], loc=9)
    #     if num == threadNumList[-1]:
    #         ax.xlabel('Snapshots (per 100 reads)')
            
        plots[idx].grid(True)
        plots[idx].set_ylabel( str(num) + ' threads')
    
     
    plt.xlabel('Snapshots (per 1000 reads)')
    # plt.ylabel('Allocated memory (MB)')
    figure.text(0.05, 0.5, 'Allocated memory (MB)', ha='center', va='center', rotation='vertical')
    plt.savefig( args.plotFilename, dpi = 300 )
    plt.show()