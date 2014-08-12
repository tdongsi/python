'''
Created on Aug 12, 2014

The command line parameters are: sampleZip installDir platformCode
Valid platform codes: vc9x32 vc9x64 vc10x32 vc10x64
Valid vcVersion: vc9 vc10

Example usage:
python mediaManager.py -sampleZip sample\mediaManager.zip -installDir C:\objy -osString vc10x64

@author: cuongd
'''

import argparse
import logging

###########################################################################
# Logger configuration
###########################################################################
import subprocess
import inspect
from shutil import Error
 
# set up logging to file
LOG_FILENAME = 'MediaManager.log'
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
                  shell = True, env = envMap )
        logger.debug(output)
    except subprocess.CalledProcessError as e:
        logger.error( "Error code: %d" % e.returncode)
        logger.error(e.output)
    return


###########################################################################
###########################################################################

# create logger
myLogger = logging.getLogger('MediaManager')

class MediaManagerTester:
    def __init__(self, sampleZip, installDir, osString):
        self._sampleZip = sampleZip
        
        self._installDir = installDir
        
        self._osString = osString
        
    def runSample(self):
        print "Let's run"
        pass

def main():
    '''Automatically run as many samples as it can in the installation directory.'''
    
    parser = argparse.ArgumentParser(description='Script to run installer and ' 
                                     'uninstall multiple times.')

    parser.add_argument('-sampleZip', action='store', required=True,
                        dest='sampleZip', 
                        help='Path to MediaManager sample ZIP file.')
            
    parser.add_argument('-installDir', action='store', required=True,
                        dest='installDir', help='Path to installation directory.')
    
    parser.add_argument('-osString', action='store', dest='osString', 
                        required=True,
                        help='String that represents the current OS. '\
                        'Windows: vc9x32, vc9x64, vc10x32, vc10x64. '\
                        'Mac: mac86_64. '\
                        'Unix/Linux: linux86_64, solaris86_64, and others. ')
    
    args = parser.parse_args()
    myLogger.debug( "Sample zip file: %s", args.sampleZip )
    myLogger.debug( "Installation directory: %s", args.installDir )
    myLogger.debug( "Operating system: %s", args.osString )
    
    checker = MediaManagerTester(args.sampleZip, args.installDir, args.osString)
    checker.runSample()
    
#     # Check individual sample run
#     checker.runSqlSamples() 
    

if __name__ == "__main__":
    '''
    See the top comment for usage.    
    '''
    out = main()