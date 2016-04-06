'''
@author: tdongsi
'''

# create logger
import logging
import MyLogger
myLogger = logging.getLogger('AnswerOne')

import collections

class AnswerOne(object):
    
    def __init__(self, filename):
        self._filename = filename
        self.ARROW = '-->'
        
        # NOTE: for this assignment, a default dict of list seems sufficient
        # More sophisticated data structure such as tree, graph may be required
        # to detect dependency cycle or remove duplicate path.
        self._dict = collections.defaultdict(list)
        
        self.init()
        
        
    def init(self):
        '''
        Process the specified input file in self._filename to construct the tree
        The tree is represented by self._dict.
        
        Assumption 1: The input file is well-formatted.
        
        Assumption 2: The structure specified by the file has a tree structure.
        Especially, no dependency cycle.
        '''
        
        try:
            with open(self._filename) as f:
                myLogger.debug('Opening and parsing file %s', self._filename)
                
                lines = f.readlines()
                for line in lines:
                    tokens = line.split()
                    
                    # First token is key
                    # Second token is values, separated by commas
                    key = tokens[0]
                    values = tokens[1].split(',')
                    self._dict[key].extend(values)
                    
        except IOError:
            myLogger.error('Cannot open file %s', self._filename)
            
        
    def getValueString(self, key_input):
        '''
        Print the values for the key input and its dependencies, based on the 
        constructed tree.
        '''
        
        if key_input in self._dict:
        
            # Method 1: Using string concatenation gives nice output but having
            # duplicate paths
            
            # Method 2: Using set. Ordering is not important, no duplicate.
            my_set = self._getValueSet(key_input)
            
            # Extra steps to make the key as the first item
            my_set.remove(key_input)
            _list = []
            _list.append( key_input )
            _list.extend(my_set)
            
            my_string = self.ARROW.join(_list)
            return my_string
        else:
            myLogger.debug( 'Cannot find key: %s', key_input )
            return ''
    
    def _getValueSet(self, key):  
        '''
        Iterate over the nodes of the tree (represented as dict of list) from the
        given node and get the UNIQUE node value.
        '''
        my_set = set()
        my_set.add(key)
        
        if key in self._dict:
            for e in self._dict[key]:
                if e in self._dict:
                    my_set |= self._getValueSet(e)
                else:
                    # At the leaf nodes
                    my_set.add(e)
        else:
            myLogger.error('Cannot find key: %s', key)
        return my_set    


def main():
    '''
    A sample program to print values and dependencies for a given key. 
    Initialize with a given file. The file content is based on the assignment.
    Read from command line for input and print out the values.
    Press Enter from command-line to terminate.
    '''
    
    answer = AnswerOne('../test/Q1Test1.txt')
    key_input = 'ready'
    
#     print answer.getValueString('X1')
#     print answer.getValueString('X2')
#     print answer.getValueString('X4')
    
    while( True ):
        key_input = raw_input('Enter the key (e.g., X2):')
        if key_input != '':
            output = answer.getValueString(key_input)
            print output
        else:
            break
    

if __name__ == '__main__':
    main()