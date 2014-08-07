'''
Created on Aug 1, 2014

This script is to check many (not all) samples in Objectivity/DB product.

Usage:
python sampleChecker.py -installDir C:\objy -osString win
python sampleChecker.py -installDir /space/usr/objy -osString mac
    
NOTE: Make sure that the following tools/executables are in the PATH:
Objy tools, javac, java

@author: cuongd
'''

import logging
import argparse
import os
import glob


###########################################################################
# Logger configuration
# From MyLogger module to make the script contained in one file.
###########################################################################
import subprocess
import inspect
 
# set up logging to file
LOG_FILENAME = 'ObjySample.log'
# Additional logging info: %(asctime)s %(name)-12s 
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s {%(name)-12s} %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=LOG_FILENAME,
                    filemode='w')
 
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)
 
 
def runCommand(logger, cmdStr, envMap = None):
    # Print out the caller module and its line number
    logger.debug( 'Calling from %s' % str(inspect.stack()[1][1:3]))
    logger.info( '> %s', ' '.join(cmdStr))
    try:
        output = subprocess.check_output( cmdStr, stderr=subprocess.STDOUT,
                  env = envMap )
        logger.debug(output)
    except subprocess.CalledProcessError as e:
        logger.error( "Error code: %d" % e.returncode)
        logger.error(e.output)
    return
 
###########################################################################
###########################################################################

# create logger
myLogger = logging.getLogger('Samples')


def runPythonSamples(installDir, osString):
    '''Run Python samples in samples/python'''
    
    myLogger.info('PYTHON SAMPLES')
    samplePath1 = 'samples/python/helloWorld'
    samplePath2 = 'samples/python/tutorial'
    
    envMap = dict(os.environ)
    if osString == 'win':
        envMap[ 'PYTHONPATH' ] = '.;%s' % str(os.path.join(installDir, 'bin'))
    else:
        envMap[ 'PYTHONPATH' ] = '.:%s' % str(os.path.join(installDir, 'bin'))
    
    curPath = os.getcwd()
    
    try:
        # Move to the sample folder
        os.chdir(os.path.join(installDir, samplePath1))
        myLogger.debug( 'Current path: %s', os.getcwd())
        runCommand(myLogger, ['python', 'main.py'], envMap)
        
        os.chdir(os.path.join(installDir, samplePath2))
        myLogger.debug( 'Current path: %s', os.getcwd())
        runCommand(myLogger, ['python', 'tutorial.py'], envMap)
        
    finally:
        # Reset the current directory
        os.chdir(curPath)
    
    return


def storageCleanup(resetExec, dirs):
    '''Clean up the sample'''
    myLogger.info( 'Cleaning up storage location tutorial')
    
    runCommand(myLogger, [resetExec, '-clean'])
    
    dirCommand = ['rm', '-r']
    dirCommand.extend(dirs)
    runCommand(myLogger, dirCommand)
    
    dirCommand = ['mkdir', '-p']
    dirCommand.extend(dirs)
    runCommand(myLogger, dirCommand)
    return

def checkDbFiles ():
    '''List all DB files in current directory and all sub-directories'''
    
#     runCommand(myLogger, ['ls', '*.DB'])
#     runCommand(myLogger, ['ls', '*/*.DB'])
    
    # More portable version
    fileList = glob.glob('*.DB')
    fileList.extend(glob.glob('*/*.DB'))
    myLogger.debug('\n'.join(fileList))
    return


def storageExample4(resetExec, populatorExec, dirs, names, bootfile):
    ''' Example 4 of the Storage Location tutorial '''
    runCommand(myLogger, [resetExec, '-MSG'])
    runCommand(myLogger, ['objy', 'ImportPlacement', 
                         '-inFile', 'Customers.pmd', 
                         '-bootfile', bootfile])
    runCommand(myLogger, ['objy', 'AddStorageLocation', 
                         '-name', 'LocB', 
                         '-dbPlacerGroup', 'Customers',
                         '-bootfile', bootfile])
    runCommand(myLogger, [populatorExec])
    
    checkDbFiles()
    myLogger.debug("Verify: Default_1.RentalComapnyData.DB created in LocationA")
    myLogger.debug("Verify: Customers_1.RentalComapnyData.DB created in LocationB")
    
    return


def storageExample3(resetExec, populatorExec, dirs, names, bootfile):
    ''' Example 3 of the Storage Location tutorial '''
    runCommand(myLogger, [resetExec, '-msg'])
    runCommand(myLogger, [populatorExec, 
                           '-loadConfiguration', 'App1Prefs.config'])
    
    checkDbFiles()
    myLogger.debug("Verify: Default_1.RentalComapnyData.DB file created in LocationC")
    
    return


def storageExample2(resetExec, populatorExec, dirs, names, bootfile):
    ''' Example 2 of the Storage Location tutorial '''
    
    runCommand(myLogger, [resetExec, '-Msg'])
    runCommand(myLogger, ['objy', 'ImportPlacement', 
                         '-inFile', 'VehicleRR.pmd', 
                         '-bootfile', bootfile])
    runCommand(myLogger, [populatorExec])
    
    checkDbFiles()
    myLogger.debug("Verify: Default* DB file and 5 Vehicles* DB files among 4 storage locations")
    
    return

def storageExample1(resetExec, populatorExec, dirs, names, bootfile):
    runCommand(myLogger, [resetExec])
    runCommand(myLogger, ['objy', 'AddStorageLocation', 
                         '-name', names[0], 
                         '-storageLocation', './%s' % dirs[0],
                         '-bootfile', bootfile])
    runCommand(myLogger, ['objy', 'AddStorageLocation',
                       '-storageLocation', './%s' % dirs[1],
                       '-storageLocation', './%s' % dirs[2],
                       '-storageLocation', './%s' % dirs[3],
                       '-bootfile', bootfile])
    runCommand(myLogger, [populatorExec])
    runCommand(myLogger, ['objy', 'ListStorage',
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
        runCommand(myLogger, mkdir)
        
        # Starting tutorial
        # Example 1
        storageExample1(resetExec, populatorExec, dirs, names, bootfile)
        
        # Example 2
        storageExample2(resetExec, populatorExec, dirs, names, bootfile)
        
        # Example 3
        storageExample3(resetExec, populatorExec, dirs, names, bootfile)
        
        # Example 4
        storageExample4(resetExec, populatorExec, dirs, names, bootfile)
        
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
        
        runCommand(myLogger, ['objy', 'CreateFd', '-fdname', 'HelloWorld'])
        
        os.chdir(os.path.join(installDir, samplePath, 'src'))
        myLogger.debug( 'Current path: %s', os.getcwd())
        
        runCommand(myLogger, ['javac', '*.java'])
        runCommand(myLogger, ['java', 'Main', '../data/HelloWorld.boot'])
        
        os.chdir(os.path.join(installDir, samplePath, 'data'))
        myLogger.debug( 'Current path: %s', os.getcwd())
        runCommand(myLogger, ['objy', 'DeleteFd', '-boot', 'HelloWorld.boot'])
        
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
                        'Windows: win. '\
                        'Mac: mac. '\
                        'Unix/Linux: linux86_64, solaris86_64, and others. ')
    
    args = parser.parse_args()
    myLogger.debug( "Installation directory: %s", args.installDir )
    myLogger.debug( "Operating system: %s", args.osString )
    
    # Java samples
    runJavaSamples(args.installDir, args.osString)
      
    # Placement tutorial: storage locations
    runStorageLocationTutorial(args.installDir, args.osString)
    
    # Python samples
    runPythonSamples(args.installDir, args.osString)
    

if __name__ == "__main__":
    '''
    See the top comment for usage.    
    '''
    out = main()
    