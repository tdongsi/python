'''
Created on Aug 11, 2014

@author: cuongd
'''

import shutil
from shutil import Error
import re


'''
Given a file containing a list of ip addresses that have lost their dots(.'s), 
write a program to find the ip addresses, assume ipv4. 
input: 11111 output. 1.1.1.11, 11.1.1.1, etc
'''
def ipString(line):
    # return ipValid(line,3)
    for ipAddress in ipValid(line, 3):
        print ipAddress

def ipValid( numberString, dotLeft ):
    if dotLeft == 0:
        number = int(numberString)
        if number < 256 and number >= 0:
            return [numberString]
        else:
            return []
        
    else:
        all = []
        for idx in range(1, len(numberString)):
            prefix = numberString[:idx]
            if int(prefix) > 255 or int(prefix) < 0:
                break
            remain = numberString[idx:]
            for line in ipValid(remain, dotLeft-1):
                all.append( prefix + '.' + line )
        return all

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
#     out = searchAndReplace('test.txt', r'INSTALL_DIR\s+=.+', 'INSTALL_DIR = %s' % installDir)
    
#     out = searchAndReplace('test.txt', r'\$\(OBJY_LIB_DIR\)\/liboo\.a', ' ')


    filename = 'testIp.txt'
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            
        for line in lines:
            ipString(line.strip())
            print '======'
    except IOError:
        print "Cannot open file %s" % filename