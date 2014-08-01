'''
Created on Aug 1, 2014

@author: cuongd
'''

import logging
import MyLogger
import argparse

# create logger
myLogger = logging.getLogger('Samples')

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
    

if __name__ == "__main__":
    '''
    Usage:
    
    '''
    out = main()
    print out