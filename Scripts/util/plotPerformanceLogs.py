#!/usr/buildtools/bin/python2.7

"""
Created on Apr 1, 2014

@author: cuongd

USAGE: plotPerformanceLogs.py -output plot.png {list of log myfile paths}
NOTE: the plot myfile name must have png extension.

This script will plot data parsed from log files into a png myfile.
The png myfile name is specified by the first argument.
The data files can be supplied as a list from the following arguments.
NOTE: It assumes certain knowledge of structure and format of the log myfile.

It will parse for scan time, disk reads, and buffer reads for each test with different number of threads.
Parsed data of each metric, e.g. scan time, of all log files will be plotted into a subplot.
The legends will be based on the myfile name (last 45 chars of filename), so pick a meaningful log myfile name.

The Python script used Matplotlib library.
Please install the following Python libraries: matplotlib, numpy, dateutil, pytz, pyparsing, six.
(optionally pillow, pycairo, tornado, wxpython, pyside, pyqt, ghostscript, miktex, ffmpeg, mencoder, avconv, or imagemagick)

I believe installation of these Python libraries are straight-forward on Linux and Win32.
On Win64, please find installers here: http://www.lfd.uci.edu/~gohlke/pythonlibs/
"""

import matplotlib.pyplot as plt
import numpy as np
import argparse

# # global setting for font size
# font = {'family' : 'normal',
#         'weight' : 'normal',
#         'size'   : 6}
# 
# plt.rc('font', **font)


def parseDataThread(filename, threadNum):
    """
    parse data for all trials with given thread number
    Input:
    filename: the log myfile
    threadNum: the given thread number
    Output:
    1 x 3 array: average time, disk reads, buffer reads
    """

    f = open(filename)
    lines = f.readlines()
    
    searchThreadPhrase = 'Thread: '
    searchThreadPhrase += str(threadNum)
    
    endingMemoryPhrase = 'CPU usage:'
    
    # Flag of starting a test: "Thread: ? Attempt: ?" entry in log.
    startFlag = False
    time = []
    diskReads = []
    bufferReads = []
    
    for line in lines:
        # Ignore the first attempt because of outlier time numbers
        if line.startswith(searchThreadPhrase) and (line.find('Attempt: 1') < 0 ):
#             print line
            startFlag = True
            
        elif line.startswith(endingMemoryPhrase):
            startFlag = False
            
        elif startFlag and line.startswith('Time'):
            tokens = line.split()
#             print tokens
            
            time.append(float(tokens[1]))
            diskReads.append(int(tokens[3]))
            bufferReads.append(int(tokens[5]))
            
#     print time
#     print diskReads
#     print bufferReads      
            
    return [np.mean(time), np.mean(diskReads), np.mean(bufferReads)]

  
def parseDataRange(filename, threadNums):
    """
    parse data for all trials with the given range of thread numbers
    Input:
    filename: the log myfile
    threadNums: the given range of thread numbers
    Output:
    n x 3 array: average time, disk reads, buffere reads for each thread number
    """  
    
    data = []
    
    for idx in range(0,len(threadNums)):
        num =threadNums[idx]
        
        row = parseDataThread(filename, num)
        data.append(row)

    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot data parsed from log files into a png myfile')
    parser.add_argument('-output', action='store', default='LogPlot.png', dest='pngFilename')
    parser.add_argument('fileList', metavar='myfile', nargs='*', help='log myfile to be plotted')
    args = parser.parse_args()
    
    # For testing and debugging
    lcFilename = r"..\data\results_firstrun.txt"
    scFilename = r"..\data\results_secondrun.txt"
    r112Filename = r'..\data\results_baseline.txt'
        
    fileList = args.fileList
    pngFilename = args.pngFilename
    
    if ( len(fileList) == 0 ):
        fileList = [lcFilename, scFilename, r112Filename]
        
    print (fileList)
    
    threadNumList = range(1,6)
    # 3 subplots for average time, disk reads, and buffer reads
    # Another one for legends
    figure, plots = plt.subplots(3, 1, True )
    # Adjust this number so that the ylabels of the subplots are aligned
    labelx = -0.11
    
    # This fileList will be replaced by command-line arguments
    fileLegend = []
    # Only use the last 45 chars for legend
    for myfile in fileList:
        fileLegend.append( myfile[-45:])
    
    colors = ['bo-', 'g*-', 'rs-', 'c8-', 'm<-', 'kv-']
    
    for idx in range(0,len(fileList)):
        data = parseDataRange(fileList[idx],threadNumList)
    #     print data
        
        matrix = np.array(data)
        
        # Plotting
        timePlot, = plots[0].plot( threadNumList, matrix[:,0], colors[idx] )
        plots[0].set_ylabel( "Scan time" )
        
        diskPlot, = plots[1].plot( threadNumList, matrix[:,1], colors[idx] )
        plots[1].set_ylabel( "Disk reads" )
        
        bufferPlot, = plots[2].plot( threadNumList, matrix[:,2], colors[idx] )
        plots[2].set_ylabel( "Buffer reads" )
        
    # Common settings for the subplots
    for idx in range(0,3):
        plots[idx].yaxis.set_label_coords(labelx, 0.5)
        plots[idx].set_xticks(range(0,7))
        plots[idx].grid(True)
    
    # Add legend
    # plots[0].legend(fileLegend, bbox_to_anchor=(0.025, 0.92, 0.95, .102), loc=3, mode="expand", borderaxespad=0.)
    lgd = plots[0].legend(fileLegend, bbox_to_anchor=(0., 1.02, 1., .102), loc=3, mode="expand", borderaxespad=0.)
    
    plt.xlabel('Thread number')
    plt.savefig(pngFilename, dpi = 300, bbox_extra_artists=(lgd,), bbox_inches='tight' )
    plt.show()
