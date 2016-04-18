"""
Created on Oct 2, 2014

@author: tdongsi
"""

import collections
import os

import logging

logging.basicConfig(level=logging.DEBUG)


class DirWalker(object):
    """
    An object of this class will walk a directory structure and create a list
    of files with the given extensions.
    """
    
    def __init__(self, rootDir):
        self._rootDir = rootDir
        self._fileList = collections.defaultdict(list)
    
    def search(self, fileExtList):
        """
        Find all files with the given extension.
        Input:
        A list of file extensions, in format '.ext', e.g. .cpp, .h.
        Output:
        List of file lists, each list for each extension.
        """
        
        self._fileList.clear()
        
        for dirName, subdirList, fileList in os.walk(self._rootDir):
            logging.debug( 'Found directory: %s', dirName )
            for fname in fileList:
                logging.debug( '\t%s', fname )
                name, ext = os.path.splitext(fname)
                # Use forward slash instead of native slash
                self._fileList[ext].append( os.path.join(dirName, fname) )
        
#         logging.debug( '%s', self._fileList)
        
        return [self._fileList[ext] for ext in fileExtList]
    
    @staticmethod
    def searchPath(self, filePath):
        pass
    
    @staticmethod
    def printRelativePath(filePath):
        """
        Print the relative paths of all files while walking a directory.
        """
        
        outString = ""
        for dirName, subdirList, fileList in os.walk(filePath):
            relPath = os.path.relpath(dirName, filePath)
            
            outString += " ".join([os.path.join(relPath, fname).replace("\\", "/") 
                                   for fname in fileList])
            outString += "\n"
        return outString
    

def main():
    my_path = 'C:/datatest/DataApi/Functional/'
    walker = DirWalker(my_path)
    cppList, hList = walker.search(['.cpp', '.h'])
    
    # Obtain relative path 
    cppRelPaths = [os.path.relpath(path, my_path).replace("\\","/") for path in cppList]
    hRelPaths = [os.path.relpath(path, my_path).replace("\\","/") for path in hList]
    
    cppFiles = [os.path.split(path)[1] for path in cppList]
    objFiles = [os.path.splitext(file)[0] + ".obj" for file in cppFiles]
    
    # Print
    with open('paths.txt', 'w') as f:
        print >>f, "CXX_SRCS = " + " ".join(cppRelPaths)
        print >>f, "HEADER_FILES = " + " ".join(hRelPaths)
        print >>f, "CXX_OBJS = " + " ".join(objFiles)
    
    print DirWalker.printRelativePath( my_path )


if __name__ == '__main__':
    main()
