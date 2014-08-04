'''
Created on Aug 1, 2014

@author: cuongd
'''

import logging
import MyLogger
import argparse
import os
import glob

# create logger
myLogger = logging.getLogger('Samples')

def storageCleanup(resetExec, dirs):
    '''Clean up the sample'''
    myLogger.info( 'Cleaning up storage location tutorial')
    
    MyLogger.runCommand(myLogger, [resetExec, '-clean'])
    
    dirCommand = ['rm', '-r']
    dirCommand.extend(dirs)
    MyLogger.runCommand(myLogger, dirCommand)
    
    dirCommand = ['mkdir', '-p']
    dirCommand.extend(dirs)
    MyLogger.runCommand(myLogger, dirCommand)
    return

def checkDbFiles ():
    '''List all DB files in current directory and all sub-directories'''
    
#     MyLogger.runCommand(myLogger, ['ls', '*.DB'])
#     MyLogger.runCommand(myLogger, ['ls', '*/*.DB'])
    
    # More portable version
    fileList = glob.glob('*.DB')
    fileList.extend(glob.glob('*/*.DB'))
    myLogger.debug('\n'.join(fileList))
    return


def storageExample2(resetExec, populatorExec, dirs, names, bootfile):
    ''' Example 2 of the Storage Location tutorial '''
    
    MyLogger.runCommand(myLogger, [resetExec, '-Msg'])
    MyLogger.runCommand(myLogger, ['objy', 'ImportPlacement', 
                         '-inFile', 'VehicleRR.pmd', 
                         '-bootfile', bootfile])
    MyLogger.runCommand(myLogger, [populatorExec])
    
    checkDbFiles()
    myLogger.debug("Verify: Default* DB file and 5 Vehicles* DB files among 4 storage locations\n")
    
    return

def storageExample1(resetExec, populatorExec, dirs, names, bootfile):
    MyLogger.runCommand(myLogger, [resetExec])
    MyLogger.runCommand(myLogger, ['objy', 'AddStorageLocation', 
                         '-name', names[0], 
                         '-storageLocation', './%s' % dirs[0],
                         '-bootfile', bootfile])
    MyLogger.runCommand(myLogger, ['objy', 'AddStorageLocation',
                       '-storageLocation', './%s' % dirs[1],
                       '-storageLocation', './%s' % dirs[2],
                       '-storageLocation', './%s' % dirs[3],
                       '-bootfile', bootfile])
    MyLogger.runCommand(myLogger, [populatorExec])
    MyLogger.runCommand(myLogger, ['objy', 'ListStorage',
                                   '-bootfile', bootfile])
    return


def runStorageLocationTutorial(installDir, osString):
    '''
    This script is to verify the tutorial 3: Specifying File Storage
    Run the samples in samples/placementTutorial/storageTasks
    '''
    
    myLogger.info('PLACEMENT TUTORIAL SAMPLES')
    samplePath = 'samples/placementTutorial/storageTasks'
    bootfile = 'RentalCompanyData.boot'
    
    resetExec = 'reset'
    populatorExec = 'populate'
    if osString == 'win':
        resetExec = 'reset.exe'
        populatorExec = 'populate.exe'
    else:
        resetExec = './reset'
        populatorExec = './populate'
        
    dirs = ['LocationA', 'LocationB', 'LocationC', 'LocationD']
    names = ['LocA', 'LocB', 'LocC', 'LocD']
    
    curPath = os.getcwd()
    
    try:
        # Move to the sample folder
        os.chdir(os.path.join(installDir, samplePath))
        myLogger.debug( 'Current path: %s', os.getcwd())
        
        # Setup
        mkdir = ['mkdir', '-p']
        mkdir.extend(dirs)
        MyLogger.runCommand(myLogger, mkdir)
        
        # Starting tutorial
        # Example 1
        storageExample1(resetExec, populatorExec, dirs, names, bootfile)
        
        # Example 2
        storageExample2(resetExec, populatorExec, dirs, names, bootfile)
        
        # Example 3
        
        # Clean up
        storageCleanup(resetExec, dirs)
        
    finally:
        # Reset the current directory
        os.chdir(curPath)

def runJavaSamples(installDir, osString):
    '''Run Java samples in samples/java/helloWorld'''
    
    myLogger.info('JAVA SAMPLES')
    samplePath = 'samples/java/helloWorld'
    
    curPath = os.getcwd()
    
    try:
        # Move to the sample folder
        os.chdir(os.path.join(installDir, samplePath, 'data'))
        myLogger.debug( 'Current path: %s', os.getcwd())
        
        MyLogger.runCommand(myLogger, ['objy', 'CreateFd', '-fdname', 'HelloWorld'])
        
        os.chdir(os.path.join(installDir, samplePath, 'src'))
        myLogger.debug( 'Current path: %s', os.getcwd())
        
        MyLogger.runCommand(myLogger, ['javac', '*.java'])
        MyLogger.runCommand(myLogger, ['java', 'Main', '../data/HelloWorld.boot'])
        
        os.chdir(os.path.join(installDir, samplePath, 'data'))
        myLogger.debug( 'Current path: %s', os.getcwd())
        MyLogger.runCommand(myLogger, ['objy', 'DeleteFd', '-boot', 'HelloWorld.boot'])
        
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
    
    # Placement tutorial: storage locations
    runStorageLocationTutorial(args.installDir, args.osString)
    

if __name__ == "__main__":
    '''
    Usage:
    
    NOTE: Make sure that the following tools/executables are in the PATH:
    Objy tools, javac, java
    
    '''
    out = main()
    