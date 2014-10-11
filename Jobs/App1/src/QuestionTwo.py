'''
@author: tdongsi
'''

# create logger
import logging
import MyLogger
myLogger = logging.getLogger('AnswerTwo')

import os
import re
import collections

class AnswerTwo(object):
    
    def __init__(self, rootDir):
        '''
        Specify the directory path as constructor parameter.
        '''
        
        self._rootDir = rootDir
        self._ipFileList = collections.Counter()
        
 
        self._pattern = re.compile(r'^\s?(\d{1,3}\.){3}\d{1,3}\s?$')
        # Test
#         print self._pattern.match(' 127.0.0.1').span()
        
        # Start searching
        self.search()
    
    
    def search(self):
        '''
        Start traversing directories from the rootDir and search for IPv4 addresses.
        '''
        
        myLogger.debug('Start traversing directory: %s', self._rootDir)
#         # DEBUG
#         self.listRoot()
        
        # Reset the internal dict
        self._ipFileList.clear()
        
        for dirName, subdirList, fileList in os.walk(self._rootDir):
            myLogger.debug('In directory: %s', dirName)
            for fname in fileList:
                self._processFile(dirName, fname)
    
    def getFileList(self):
        '''
        Get an alphabetically sorted list of files with a count of valid IPv4 
        addresses for each file.
        '''
        
        keys = self._ipFileList.keys()
        
        # Natural ordering happens to be sufficient
        keys.sort()
        
        _list = [(key, self._ipFileList[key]) for key in keys]
        return _list
        
    
    def _processFile(self, path, fName):
        '''
        Read the file based on the path and file name.
        Process the file content for IPv4 addresses.
        '''
        
        try:
            with open(os.path.join(path,fName)) as f:
                lines = f.readlines()
                # Remove the trailing newline
                # TRICKY: "\r\n" is more portable. 
                # os.linesep is NOT portable. E.g.: A Windows file copied to Mac.
                lines = [line.rstrip("\r\n") for line in lines]
                
                for line in lines:
                    if self._isIpv4(line):
                        myLogger.debug( 'IPv4 YES: [%s]', line)
                        self._ipFileList[fName] += 1
                    else:
                        myLogger.debug( 'IPv4 NOT: [%s]', line)
        except IOError:
            myLogger.error( 'Cannot open file %s/%s', path, fName)
        
    
    def _isIpv4(self, input_string):
        '''
        Check if the given input string is a valid IP4 address
        '''
        
        if self._pattern.match(input_string):
            tokens = input_string.strip().split('.')
            
            for token in tokens:
                num = int(token)
                if num > 255 or num < 0:
                    return False
            
            return True
        else:
            return False
    
    def listRoot(self):
        '''
        Print all directories and files from the given root directory. 
        '''
        
        for dirName, subdirList, fileList in os.walk(self._rootDir):
            myLogger.debug('Found directory: %s', dirName)
            for fname in fileList:
                myLogger.debug( '\t%s', fname )

def main():
    '''
    Example usage
    '''
    
    rootDir = u'../test/Q2Test2'
    answer = AnswerTwo(rootDir)
    
    for pair in answer.getFileList():
        print "%s %s" % pair
    
    # Add some files to rootDir ...
    print '\nFiles may be added or updated... \n'
    
    # The same object can perform the directory traversal again
    answer.search()
    for pair in answer.getFileList():
        print "%s %s" % pair


if __name__ == '__main__':
    main()