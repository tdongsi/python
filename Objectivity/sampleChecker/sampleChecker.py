'''
Created on Aug 1, 2014

@author: cuongd
'''

import logging
import MyLogger
import argparse
import os

# create logger
myLogger = logging.getLogger('Samples')

def runJavaSamples(installDir, osString):
    '''Run Java samples in samples/java/helloWorld'''
    
    myLogger.info('JAVA SAMPLES')
    samplePath = 'samples/java/helloWorld'
    
    curPath = os.getcwd()
    
    try:
        # Move to the sample folder
        os.chdir(os.path.join(installDir, samplePath, 'data'))
        myLogger.debug( 'Current path: %s', os.getcwd())
        
        MyLogger.runCommand(['objy', 'CreateFd', '-fdname', 'HelloWorld'], myLogger)
        
        os.chdir(os.path.join(installDir, samplePath, 'src'))
        myLogger.debug( 'Current path: %s', os.getcwd())
        
        MyLogger.runCommand(['javac', '*.java'], myLogger)
        MyLogger.runCommand(['java', 'Main', '../data/HelloWorld.boot'], myLogger)
        
        os.chdir(os.path.join(installDir, samplePath, 'data'))
        myLogger.debug( 'Current path: %s', os.getcwd())
        MyLogger.runCommand(['objy', 'DeleteFd', '-boot', 'HelloWorld.boot'], myLogger)
        
    finally:
        # Reset the current directory
        os.chdir(curPath)
    

def main():
    '''Automatically run as many samples as it can in the installation directory.'''
    
    parser = argparse.ArgumentParser(description='Script to run installer and ' 
                                     'uninstall multiple times.')
        
    parser.add_argument('-installDir', action='store', required=True,
                        dest='installDir', help='Path to installation directory.')
    
    parser.add_argument('-osString', action='store', dest='osString', 
                        required=True,
                        help='String that represents the current OS. '\
                        'Windows: win, win_x64, intelnt. '\
                        'Mac: mac, mac86_64. '\
                        'Unix/Linux: linux86_64, solaris86_64, and others. ')
    
    args = parser.parse_args()
    myLogger.debug( "Installation directory: %s", args.installDir )
    myLogger.debug( "Operating system: %s", args.osString )
    
    # Java samples
    runJavaSamples(args.installDir, args.osString)
    

if __name__ == "__main__":
    '''
    Usage:
    
    NOTE: Make sure that the following tools/executables are in the PATH:
    Objy tools, javac, java
    
    '''
    out = main()
    