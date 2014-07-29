'''
Created on Jul 28, 2014

@author: cuongd
'''

import argparse

import MyLogger
import logging
import os
import time

# create logger
myLogger = logging.getLogger('IgInstaller')

# Common global variables

INSTALLER_APP_EXT = ''
INSTALLATION_DIR = ''
UNINSTALLER = ''
LICENSE_LOCATION = ''

INSTALL_LOG_DIR = ''
# UNINSTALL_LOG_DIR = ''

OOCHECKAMS = ''
OOCHECKLS = ''
OOCHECKQS = ''

CLASS_PATH_ADD = ''
PYTHON_PATH_ADD = ''
PATH_SEPARATOR = ''

def setup(installDir, osString):
    '''
    Setup some global variables based on different OS.
    Human is better in identifying his current platform than a script.
    Avoid adding complexity to the script.
    '''
    global INSTALLATION_DIR, INSTALL_LOG_DIR, UNINSTALLER, LICENSE_LOCATION
    global INSTALL_LOG_DIR
    global OOCHECKAMS, OOCHECKLS, OOCHECKQS
    global CLASS_PATH_ADD, PYTHON_PATH_ADD, PATH_SEPARATOR
    
    INSTALLATION_DIR = installDir
    INSTALL_LOG_DIR = installDir
    
    OOCHECKAMS = "%s/bin/oocheckams" % installDir
    OOCHECKLS = '%s/bin/oocheckls' % installDir
    OOCHECKQS = '%s/bin/ooqueryserver -check' % installDir
    
    CLASS_PATH_ADD = os.path.normpath('%s/lib/oojava.jar' % installDir)
    PYTHON_PATH_ADD = os.path.normpath('%s/bin' % installDir)
    
    if (osString == 'win_x64' or osString == 'intelnt' or osString == 'win' ):
        INSTALLER_APP_EXT = '.exe'
        UNINSTALLER = '%s/uninstall%s' %(installDir, INSTALLER_APP_EXT)
        LICENSE_LOCATION = 'C:/windows/oolicense.txt'
        PATH_SEPARATOR = ';'
        
    elif (osString == 'mac86_64' or osString == 'mac' ):
        INSTALLER_APP_EXT = '.app'
        UNINSTALLER = "%s/uninstall%s/Contents/MacOS/installbuilder.sh"%(installDir, INSTALLER_APP_EXT)
        LICENSE_LOCATION = '~oqa/oolicense.txt'
        PATH_SEPARATOR = ':'
        
    else:
        '''Linux and Unix distributions'''
        INSTALLER_APP_EXT = '.run'
        UNINSTALLER = '%s/uninstall' %(installDir)
        LICENSE_LOCATION = '~oqa/oolicense.txt'
        PATH_SEPARATOR = ':'

    # Logging all the setup variables     
    myLogger.debug( 'INSTALLATION_DIR: %s', INSTALLATION_DIR)
    myLogger.debug( 'INSTALL_LOG_DIR: %s', INSTALL_LOG_DIR)
    myLogger.debug( 'UNINSTALLER: %s', UNINSTALLER)
    myLogger.debug( 'LICENSE_LOCATION: %s', LICENSE_LOCATION)
    
    myLogger.debug( 'CLASS_PATH_ADD: %s', CLASS_PATH_ADD)
    myLogger.debug( 'PYTHON_PATH_ADD: %s', PYTHON_PATH_ADD)
    
    myLogger.debug( 'OOCHECKAMS: %s', OOCHECKAMS)
    myLogger.debug( 'OOCHECKLS: %s', OOCHECKLS)
    myLogger.debug( 'OOCHECKQS: %s', OOCHECKQS)


def uninstallLocal( installDir ):
    '''Perform uninstallation for the localhost'''
    myLogger.info( "Uninstalling from %s", installDir )
    
    if (not os.path.exists(UNINSTALLER) ):
        myLogger.error( "Uninstaller %s file not found", UNINSTALLER )
        return
    
    MyLogger.runCommand([UNINSTALLER, '--mode', 'unattended'],
                        myLogger)


def installLocal( installer, installDir ):
    '''Perform installation for the localhost'''
    myLogger.info( "Installing %s to %s", installer, installDir )
    
    MyLogger.runCommand([installer, '--mode', 'unattended', 
                         '--prefix', installDir,
                         '--installenv', '1'], myLogger)
    

def countEnvironmentPath(path, pathList):
    myLogger.debug('Target path: %s', path)
    myLogger.debug('Path list: %s', pathList)
    count = 0
    
    for p in pathList.split(PATH_SEPARATOR):
        if (path == p):
            count += 1
    
    return count


def main():
    '''Returns the paths in environment variables CLASSPATH and PYTHONPATH, 
    then install and uninstall multiple times.'''
    parser = argparse.ArgumentParser(description='Script to run installer and ' 
                                     'uninstall multiple times.')
    
    parser.add_argument('-installer', action='store', required=True,
                        dest='installer', help='Name of one-file installer.')
    
    parser.add_argument('-installDir', action='store', required=True,
                        dest='installDir', help='Path to installation directory.')
    
    parser.add_argument('-repeat', action='store', dest='repeatTimes', 
                        required=True, type=int,
                        help='Number of installation and uninstallation loop.')
    
    parser.add_argument('-osString', action='store', dest='osString', 
                        required=True,
                        help='String that represents the current OS. '\
                        'Windows: win, win_x64, intelnt. '\
                        'Mac: mac, mac86_64. '\
                        'Unix/Linux: linux86_64, solaris86_64, and others. ')
    
    args = parser.parse_args()
    myLogger.debug( "Installer file: %s", args.installer )
    myLogger.debug( "Number of repeat times: %s", args.repeatTimes )
    myLogger.debug( "Installation directory: %s", args.installDir )
    
    if (not os.path.exists(args.installer) ):
        myLogger.error( "Installer %s file not found", args.installer )
        return
    
    # Setup global variables before installing and uninstalling
    setup(args.installDir, args.osString)
    
    envi = {}
    envi[CLASS_PATH_ADD] = countEnvironmentPath( CLASS_PATH_ADD, os.environ['CLASSPATH'])
    envi[PYTHON_PATH_ADD] = countEnvironmentPath( PYTHON_PATH_ADD, os.environ['PYTHONPATH'])
    
    # Install on localhost
    for i in xrange(args.repeatTimes):
        myLogger.debug("Time %s", i)
        installLocal(args.installer, args.installDir)
        time.sleep(15)
        uninstallLocal(args.installDir)
    
    return envi

if __name__ == "__main__":
    '''
    Usage:
    This script is used to verify:
    1. if environment variables CLASSPATH and PYTHONPATH are properly updated 
    during installation and uninstallation of the product.
    
    Run this script with 0 to print out paths
    '''
    out = main()
    print out