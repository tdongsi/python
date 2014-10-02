'''
Created on Oct 2, 2014

@author: tdongsi
'''

import collections

class DirWalker(object):
    '''
    An object of this class will walk a directory structure and create a list
    of files with the given extensions.
    '''
    
    def __init__(self, filePath):
        self._filePath = filePath
        self._fileList = collections.defaultdict(list)
    
    def search(self, fileExtList):
        '''
        Find all files with the given extension.
        Input:
        A list of file extensions
        Output:
        List of file lists, each list for each extension.
        '''
        
        self._fileList.clear()
        
        return [self._fileList[ext] for ext in fileExtList]
        

def main():
    walker = DirWalker('C:/datatest/DataApi/Functional')
    walker.search(['cpp', 'h'])
    pass

if __name__ == '__main__':
    main()
    
