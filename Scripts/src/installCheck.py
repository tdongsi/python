'''
Created on Jul 28, 2014

@author: cuongd
'''

import argparse

import MyLogger
import logging
import os

# create logger
myLogger = logging.getLogger('IgInstaller')

def uninstallLocal( installDir ):
    '''Perform IG installation for the localhost, update symlink'''
    
    pass


def installLocal( installer, installDir ):
    '''Perform IG installation for the localhost, update symlink'''
    
    MyLogger.runCommand([installer, '--mode', 'unattended', 
                         '--prefix', installDir], 
                        myLogger)
    
    pass

def main():
    '''Returns the paths in environment variables CLASSPATH and PYTHONPATH, 
    then install and uninstall multiple times.'''
    parser = argparse.ArgumentParser(description='Script to run installer and ' 
                                     'uninstall multiple times.')
    
    parser.add_argument('-installer', action='store', required=True,
                        dest='installer', help='Name of one-file installer.')
    
    parser.add_argument('-prefix', action='store', required=True,
                        dest='installDir', help='Path to installation directory.')
    
    parser.add_argument('-repeat', action='store', dest='repeatTimes', 
                        required=True, type=int,
                        help='Number of installation and uninstallation loop.')
    
    args = parser.parse_args()
    myLogger.debug( "Installer file: %s", args.installer )
    myLogger.debug( "Number of repeat times: %s", args.repeatTimes )
    myLogger.debug( "Installation directory: %s", args.installDir )
    
    if (not os.path.exists(args.installer) ):
        myLogger.error( "Installer %s file not found", args.installer )
        return
    
    envi = [os.environ['CLASSPATH'], 
            os.environ['PYTHONPATH']]
    
    # Install on localhost
    for time in xrange(args.repeatTimes):
        myLogger.debug("Time %s", time)
        installLocal(args.installer, args.installDir)
        uninstallLocal(args.installDir)
    
    return envi

if __name__ == "__main__":
    out = main()
    print out