'''
Created on Aug 11, 2014

@author: cuongd
'''

import shutil
from shutil import Error
import re

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


if __name__ == "__main__":
    '''
    Test functions
    '''
    installDir = 'C:/objydev'
    out = searchAndReplace('test.txt', r'INSTALL_DIR\s+=.+', 'INSTALL_DIR = %s' % installDir)
