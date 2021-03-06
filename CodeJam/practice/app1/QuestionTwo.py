"""
@author: tdongsi
"""
import os
import re
import collections
# create logger
import logging

import practice.app1.MyLogger
myLogger = logging.getLogger('AnswerTwo')


class AnswerTwo(object):
    
    def __init__(self, rootDir):
        """
        Specify the directory path as constructor parameter.
        """
        
        self._rootDir = rootDir
        self._ipFileList = collections.Counter()
        
        """
        Explain the regex pattern:
        (\s+|\A): Has a space before it or starts at the beginning of a line
        (\d{1,3} \.){3} \d{1,3}: in the range 0.0.0.0 - 999.999.999.999
        (\s+|\Z): Has a space after it or finishes at the end of a line
        
        NOTE:
        IPv4 address will be further validated in Python
        The recommended practice is to use a simple regex and process in Python.
        Fully validating an IPv4 in regex will make the regex hard to maintain.
        """
        self._pattern = re.compile(r'(\s+|\A)(\d{1,3}\.){3}\d{1,3}(\s+|\Z)')
#         # Test
#         print self._pattern.match('  0.0.0.0').span()
        
        # Start searching
        self.search()
    
    def search(self):
        """
        Start traversing directories from the rootDir and search for IPv4 addresses.
        """
        
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
        """
        Get an alphabetically sorted list of files with a count of valid IPv4 
        addresses for each file.
        
        The sort order should be case sensitive. Files starting with integers 
        should be listed first, followed by files starting with upper case letters, 
        followed by files starting with lower case letters.
        """
        
        keys = self._ipFileList.keys()
        
        # Natural ordering happens to be sufficient
        keys.sort()
        
        _list = [(key, self._ipFileList[key]) for key in keys]
        return _list
        
    
    def _processFile(self, path, fName):
        """
        Read the file based on the path and file name.
        Process the file content for IPv4 addresses.
        """
        
        try:
            with open(os.path.join(path,fName)) as f:
                lines = f.readlines()
                # Remove the trailing newline
                # TRICKY: "\r\n" is more portable. 
                # os.linesep is NOT portable. E.g.: A Windows file copied to Mac.
                lines = [line.rstrip("\r\n") for line in lines]
                
                for line in lines:
                    matches = self._pattern.finditer(line)
                    
                    for match in matches:
                        if self._isIpv4(match.group(0)):
                            myLogger.debug( 'IPv4 YES: [%s]', line)
                            self._ipFileList[fName] += 1
                        else:
                            myLogger.debug( 'IPv4 NOT: [%s]', line)
        except IOError:
            myLogger.error( 'Cannot open file %s/%s', path, fName)
        
    
    def _isIpv4(self, input_string):
        """
        Check if the given input string is a valid IP4 address
        
        Assume a valid IPv4 address has the following criteria:
        1. Has a space before it or starts at the beginning of a line
        2. Has a space after it or finishes at the end of a line
        3. Is in the range 0.0.0.0 - 255.255.255.255 (inclusive)
        """
        
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
        """
        Print all directories and files from the given root directory. 
        """
        
        for dirName, subdirList, fileList in os.walk(self._rootDir):
            myLogger.debug('Found directory: %s', dirName)
            for fname in fileList:
                myLogger.debug( '\t%s', fname )

def main():
    """
    Example usage
    """
    
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