'''
Created on Aug 1, 2014

This script is to check many (not all) samples in Objectivity/DB product.

In Windows, the method runSqlSamples() uses nmake to compile the sample.
Therefore, the main script sampleChecker.py should be run in Visual Studio 
Command Prompt (instead of standard Command Prompt).

Usage:

0. Start the lock server by using the tool oolockserver.

1. Specify the install directory and OS string from command line:
python sampleChecker.py -installDir C:\objy -osString win
python sampleChecker.py -installDir /space/usr/objy -osString mac

2. Verify the sample output from ObjySample.log
    
NOTE: Make sure that the following tools/executables are in the PATH:
Objy tools, javac, java, nmake/make.

@author: cuongd
'''

import logging
import argparse
import os
import glob
import shutil
import re
import socket


###########################################################################
# Logger configuration
# From MyLogger module to make the script contained in one file.
###########################################################################
import subprocess
import inspect
from shutil import Error
 
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


def searchAndReplace( filename, oldString, newString):
    '''
    Open a file, search for oldString (regex) and replace with a new string.
    Raw string is recommended for oldString input.
    '''
    
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            f.close()
            
        # Create a backup copy
        try:
            shutil.copyfile(filename, '%s.bak' % filename)
        except Error:
            print 'Error backing up file %s' % filename
        
        with open(filename, 'w') as f:
            for line in lines:
                nline = re.sub(oldString, newString, line)
                f.write(nline)
            f.close()
    except IOError:
        print 'Error opening file %s' % filename

    return

###########################################################################
###########################################################################

# create logger
myLogger = logging.getLogger('Samples')

class SampleChecker:
    
    def __init__(self, installDir, osString):
        self._installDir = installDir
        self._osString = osString
        
    def runSamples(self):
        ''' Run all the samples '''
        # Java samples
        self.runJavaSamples()
          
        # Placement tutorial: storage locations
        self.runStorageLocationTutorial()
        
        # Python samples
        self.runPythonSamples()
        
        # C++ samples. Linux/Mac only
        # In Windows, use Visual Studio to run the sample
        self.runCppSamples()
        
        # SQL++ samples
        self.runSqlSamples()
        

    def runSqlSamples(self):
        '''
        Run Objy/SQL++ samples in samples/sql/ooisql
        In Windows, make sure the script is running in VS Command Prompt where
        nmake tool is available.
        '''
        
        myLogger.info('SQL++ SAMPLES')
        samplePath = 'samples/sql/ooisql'
        
        if self._osString == 'mac':
            myLogger.info('SQL samples are not available in Mac.')
            return
        
        try:
            if os.path.exists(os.path.join(self._installDir, samplePath + 'bak')):
                shutil.rmtree(os.path.join(self._installDir, samplePath + 'bak'), True)
            shutil.copytree(os.path.join(self._installDir, samplePath), 
                         os.path.join(self._installDir, samplePath + 'bak'))
        except Error as e:
            myLogger.error( 'Fail to backup %s', samplePath)
            myLogger.error(e)
        
        if self._osString == 'win':
            
            curPath = os.getcwd()
            
            try:
                # Copy Makefile
                myLogger.debug( '> cp %s/etc/sql/usr_proc/Makefile %s/%s/Makefile',
                            self._installDir, self._installDir, samplePath)
                shutil.copy(os.path.join(self._installDir, 'etc', 'sql', 'usr_proc', 'Makefile' ), 
                        os.path.join(self._installDir, samplePath, 'Makefile'))
            
                # Move to the sample folder
                os.chdir(os.path.join(self._installDir, samplePath))
                myLogger.debug( 'Current path: %s', os.getcwd())
                
                myLogger.info('Editing Makefile ...')
                searchAndReplace('Makefile', r'INSTALL_DIR\s+=.+', 
                                 'INSTALL_DIR = %s' % self._installDir)
                
                myLogger.info('Editing demo.bat ...')
                searchAndReplace('demo.bat', r'dummy', 'sql4eran')
                
                runCommand( myLogger, ['nmake', 'all'])
                runCommand( myLogger, ['demo.bat'])
                
                myLogger.debug( 'Check for "FC: no differences encountered"')
            except Error as err:
                myLogger.error( 'Error running SQL sample in Windows' )
                myLogger.error(err)                
            finally:
                # Reset the current directory
                os.chdir(curPath)
        
        else:
            curPath = os.getcwd()
            
            try:
                # Move to the sample folder
                os.chdir(os.path.join(self._installDir, samplePath))
                myLogger.debug( 'Current path: %s', os.getcwd())
                
                myLogger.info('Editing Makefile ...')
                searchAndReplace('Makefile', r'INSTALL_DIR\s+=.+', 
                                 'INSTALL_DIR = %s' % self._installDir)
                searchAndReplace('Makefile', r'LS_HOST\s+=.+', 
                                 'LS_HOST = %s' % socket.gethostname())
                searchAndReplace('Makefile', r'FDID\s+=.+', 'FDID = 1234')
                
                # This portion of Makefile will be fixed.
                # Temporary workaround
                searchAndReplace('Makefile', r'LDFLAGS\s+=.+', 
                     r'LDFLAGS = -L$(OBJY_LIB_DIR) -loo.11.2 -lrpcsvc -lnsl -lpthread -ldl')
                searchAndReplace('Makefile', r'\$\(OBJY_LIB_DIR\)\/liboo\.a', ' ')
                
                
                myLogger.info('Editing demo.sh ...')
                searchAndReplace('demo.sh', r'passwd=.+', 'passwd=sql4eran')
                
                runCommand( myLogger, ['make'])
                runCommand( myLogger, ['./demo.sh'])
                
                myLogger.debug( 'Check for "FC: no differences encountered"')
            except Error as err:
                myLogger.error( 'Error running SQL sample in Linux/Unix' )
                myLogger.error(err)                
            finally:
                # Reset the current directory
                os.chdir(curPath)
        
        return
    
    
    def runCppSamples(self):
        '''Run C++ samples in samples/cxx/helloWorld'''

        myLogger.info('C++ SAMPLES')
        samplePath = 'samples/cxx/helloWorld'

        if self._osString == 'win':
            myLogger.info('In Windows, C++ samples must be run with Visual Studio.')
            return
        else:
            curPath = os.getcwd()

            try:
                # Move to the sample folder
                os.chdir(os.path.join(self._installDir, samplePath))
                myLogger.debug( 'Current path: %s', os.getcwd())

                myLogger.info('Compiling sample')
                runCommand(myLogger, ['make', '-e'])
                myLogger.info('Compiling sample')
                runCommand(myLogger, ['./helloWorld', 'data/HelloWorld.boot'])

            finally:
                # Reset the current directory
                os.chdir(curPath)

        return
    
    
    def runPythonSamples(self):
        '''Run Python samples in samples/python'''
        
        myLogger.info('PYTHON SAMPLES')
        samplePath1 = 'samples/python/helloWorld'
        samplePath2 = 'samples/python/tutorial'
        
        envMap = dict(os.environ)
        if self._osString == 'win':
            envMap[ 'PYTHONPATH' ] = '.;%s' % str(os.path.join(self._installDir, 'bin'))
        else:
            envMap[ 'PYTHONPATH' ] = '.:%s' % str(os.path.join(self._installDir, 'lib'))
        
        curPath = os.getcwd()
        
        try:
            # Move to the sample folder
            os.chdir(os.path.join(self._installDir, samplePath1))
            myLogger.debug( 'Current path: %s', os.getcwd())
            runCommand(myLogger, ['python', 'main.py'], envMap)
            
            os.chdir(os.path.join(self._installDir, samplePath2))
            myLogger.debug( 'Current path: %s', os.getcwd())
            runCommand(myLogger, ['python', 'tutorial.py'], envMap)
            
        finally:
            # Reset the current directory
            os.chdir(curPath)
        
        return
    
    
    def storageCleanup(self, resetExec, dirs):
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
    
    def checkDbFiles(self):
        '''List all DB files in current directory and all sub-directories'''
        
    #     runCommand(myLogger, ['ls', '*.DB'])
    #     runCommand(myLogger, ['ls', '*/*.DB'])
        
        # More portable version
        fileList = glob.glob('*.DB')
        fileList.extend(glob.glob('*/*.DB'))
        myLogger.debug('\n'.join(fileList))
        return
    
    
    def storageExample4(self, resetExec, populatorExec, dirs, names, bootfile):
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
        
        self.checkDbFiles()
        myLogger.debug("Verify: Default_1.RentalComapnyData.DB created in LocationA")
        myLogger.debug("Verify: Customers_1.RentalComapnyData.DB created in LocationB")
        
        return
    
    
    def storageExample3(self, resetExec, populatorExec, dirs, names, bootfile):
        ''' Example 3 of the Storage Location tutorial '''
        runCommand(myLogger, [resetExec, '-msg'])
        runCommand(myLogger, [populatorExec, 
                               '-loadConfiguration', 'App1Prefs.config'])
        
        self.checkDbFiles()
        myLogger.debug("Verify: Default_1.RentalComapnyData.DB file created in LocationC")
        
        return
    
    
    def storageExample2(self, resetExec, populatorExec, dirs, names, bootfile):
        ''' Example 2 of the Storage Location tutorial '''
        
        runCommand(myLogger, [resetExec, '-Msg'])
        runCommand(myLogger, ['objy', 'ImportPlacement', 
                             '-inFile', 'VehicleRR.pmd', 
                             '-bootfile', bootfile])
        runCommand(myLogger, [populatorExec])
        
        self.checkDbFiles()
        myLogger.debug("Verify: Default* DB file and 5 Vehicles* DB files among 4 storage locations")
        
        return
    
    def storageExample1(self, resetExec, populatorExec, dirs, names, bootfile):
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
    
    
    def runStorageLocationTutorial(self):
        '''
        This script is to verify the tutorial 3: Specifying File Storage
        Run the samples in samples/placementTutorial/storageTasks
        '''
        
        myLogger.info('PLACEMENT TUTORIAL SAMPLES')
        samplePath = 'samples/placementTutorial/storageTasks'
        bootfile = 'RentalCompanyData.boot'
        
        resetExec = 'reset'
        populatorExec = 'populate'
        if self._osString == 'win':
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
            os.chdir(os.path.join(self._installDir, samplePath))
            myLogger.debug( 'Current path: %s', os.getcwd())
            
            # Setup
            mkdir = ['mkdir', '-p']
            mkdir.extend(dirs)
            runCommand(myLogger, mkdir)
            
            # Starting tutorial
            # Example 1
            self.storageExample1(resetExec, populatorExec, dirs, names, bootfile)
            
            # Example 2
            self.storageExample2(resetExec, populatorExec, dirs, names, bootfile)
            
            # Example 3
            self.storageExample3(resetExec, populatorExec, dirs, names, bootfile)
            
            # Example 4
            self.storageExample4(resetExec, populatorExec, dirs, names, bootfile)
            
            # Clean up
            self.storageCleanup(resetExec, dirs)
            
        finally:
            # Reset the current directory
            os.chdir(curPath)
    
    def runJavaSamples(self):
        '''Run Java samples in samples/java/helloWorld'''
        
        myLogger.info('JAVA SAMPLES')
        samplePath = 'samples/java/helloWorld'
        
        curPath = os.getcwd()
        classPathList = ['.', str(os.path.join(self._installDir, 'lib', 'oojava.jar'))]
        if self._osString == 'win':
            separator = ';'
        else:
            separator = ':'
        classPathString = separator.join(classPathList)
        
        try:
            # Move to the sample folder
            os.chdir(os.path.join(self._installDir, samplePath, 'data'))
            myLogger.debug( 'Current path: %s', os.getcwd())
            
            runCommand(myLogger, ['objy', 'CreateFd', '-fdname', 'HelloWorld'])
            
            os.chdir(os.path.join(self._installDir, samplePath, 'src'))
            myLogger.debug( 'Current path: %s', os.getcwd())
            
            runCommand(myLogger, ['javac', '-cp', classPathString, 
                                  'HelloObject.java', 'Main.java'])
            runCommand(myLogger, ['java', '-cp', classPathString, 
                                  'Main', '../data/HelloWorld.boot'])
            
            os.chdir(os.path.join(self._installDir, samplePath, 'data'))
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
    
    checker = SampleChecker(args.installDir, args.osString)
    checker.runSamples()
    
#     # Check individual sample run
#     checker.runSqlSamples() 
    

if __name__ == "__main__":
    '''
    See the top comment for usage.    
    '''
    out = main()
    