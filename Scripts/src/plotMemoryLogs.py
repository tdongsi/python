#!/usr/buildtools/bin/python2.7

'''
Created on Apr 1, 2014

@author: cuongd
'''
# FIXEDBUG: the script is ad-hoc, based on the log file
# Need to adjust logging to make the script for robust 
# Assume the memory log is at the end of the file.
# Setting threadNum to 4 and it will fail.

import re
import matplotlib.pyplot as plt

lcFilename = r"..\data\PerfLog_feature_OFF.txt";
scFilename = r"..\data\PerfLog_feature_ON.txt";

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
    

threadNumList = range(2,6)
figure, plots = plt.subplots(len(threadNumList), 1, True )
for num in threadNumList:
    
    idx = num - threadNumList[0]
    
    # Reading the data from file
    lcData = parseDataFile(lcFilename, num)
    scData = parseDataFile(scFilename, num)
    
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
plt.savefig("MemoryLogging.png", dpi = 300 )
plt.show()