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

def setup(installDir, osString):
    '''
    Setup some global variables based on different OS.
    Human is better in identifying his current platform than the script.
    '''
    INSTALLATION_DIR = installDir
    INSTALL_LOG_DIR = installDir
    
    OOCHECKAMS = "%s/bin/oocheckams" % installDir
    OOCHECKLS = '%s/bin/oocheckls' % installDir
    OOCHECKQS = '%s/bin/ooqueryserver -check' % installDir
    
    if (osString == 'win_x64' or osString == 'intelnt' or osString == 'win' ):
        INSTALLER_APP_EXT = '.exe'
        UNINSTALLER = '%s/uninstall%s' %(installDir, INSTALLER_APP_EXT)
        LICENSE_LOCATION = 'C:/windows/oolicense.txt'
        
    elif (osString == 'mac86_64' or osString == 'mac' ):
        INSTALLER_APP_EXT = '.app'
        UNINSTALLER = "%s/uninstall%s/Contents/MacOS/installbuilder.sh"%(installDir, INSTALLER_APP_EXT)
        LICENSE_LOCATION = '~oqa/oolicense.txt'
        
    else:
        '''Linux and Unix distributions'''
        INSTALLER_APP_EXT = '.run'
        UNINSTALLER = '%s/uninstall' %(installDir)
        LICENSE_LOCATION = '~oqa/oolicense.txt'

    # Logging all the setup variables     
    myLogger.debug( 'INSTALLATION_DIR: %s', INSTALLATION_DIR)
    myLogger.debug( 'INSTALL_LOG_DIR: %s', INSTALL_LOG_DIR)
    myLogger.debug( 'UNINSTALLER: %s', UNINSTALLER)
    myLogger.debug( 'LICENSE_LOCATION: %s', LICENSE_LOCATION)
    
    myLogger.debug( 'OOCHECKAMS: %s', OOCHECKAMS)
    myLogger.debug( 'OOCHECKLS: %s', OOCHECKLS)
    myLogger.debug( 'OOCHECKQS: %s', OOCHECKQS)


def uninstallLocal( installDir ):
    '''Perform IG installation for the localhost, update symlink'''
    myLogger.info( "Uninstalling from %s", installDir )
    
    pass


def installLocal( installer, installDir ):
    '''Perform IG installation for the localhost, update symlink'''
    myLogger.info( "Installing %s to %s", installer, installDir )
    
#     MyLogger.runCommand([installer, '--mode', 'unattended', 
#                          '--prefix', installDir], 
#                         myLogger)
    
    pass

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
    
    envi = [os.environ['CLASSPATH'], 
            os.environ['PYTHONPATH']]
    
    # Setup global variables before installing and uninstalling
    setup(args.installDir, args.osString)
    
    # Install on localhost
    for time in xrange(args.repeatTimes):
        myLogger.debug("Time %s", time)
        installLocal(args.installer, args.installDir)
        uninstallLocal(args.installDir)
    
    return envi

if __name__ == "__main__":
    '''
    Usage:
    Run this script with 0 to print out path repeat
    '''
    out = main()
    print out