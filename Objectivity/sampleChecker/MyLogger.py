'''
Created on Aug 1, 2014

@author: cuongd
'''

import logging
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


def runCommand(cmdStr, logger):
    # Print out the caller module and its line number
    logger.debug( 'Calling from %s' % str(inspect.stack()[1][1:3]))
    logger.info( '> %s', str(cmdStr))
    try:
        output = subprocess.check_output( cmdStr, stderr=subprocess.STDOUT )
        logger.debug(output)
    except subprocess.CalledProcessError as e:
        logger.error( "Error code: %d" % e.returncode)
        logger.error(e.output)
        
        
if __name__ == "__main__":
    print "My configured logging module."