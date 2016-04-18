"""
Created on Jul 28, 2014

@author: cuongd
"""

import logging
import subprocess
import inspect
from contextlib import contextmanager
import os

# set up logging to file
LOG_FILENAME = 'installCheck.mylog'
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


# create logger
myLogger = logging.getLogger('IncrementalLoad')


def runCommand(cmdStr, logger = myLogger, envMap = None):
    # Print out the caller module and its line number
    logger.debug( 'Calling from %s', str(inspect.stack()[1][1:3]))
    logger.info( '> %s', ' '.join(cmdStr))
    try:
        output = subprocess.check_output( cmdStr, stderr=subprocess.STDOUT,
                  env = envMap )
        logger.debug(output)
    except subprocess.CalledProcessError as e:
        logger.error( "Error code: %d", e.returncode)
        logger.error(e.output)
    return

@contextmanager
def working_directory(path):
    """
    Switch to a new working directory and back to the current, using with statement.
    """
    
    current_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(current_dir)
        
        
if __name__ == "__main__":
    print "My configured logging module."