'''
@author: tdongsi
'''
import unittest
from QuestionTwo import *

class Test(unittest.TestCase):
    '''
    The IPv4 validation aspect of AnswerTwo class is tested by many test cases
    in the file content of files in Q2Test2 directory.
    
    Only test exceptional scenarios in terms of file system here.  
    '''

    def test_functional(self):
        answer = AnswerTwo(u'../test/Q2Test2')
        expected = [(u'1_File.txt', 5), (u'A_File.rtf', 4), (u'C_File.log', 7), (u'a_File.txt', 6)]
        self.assertEqual(answer.getFileList(), expected)


    def test_NonExistentPath(self):
        '''
        An empty file list is expected
        '''
        
        answer = AnswerTwo(u'NonExistent')
        self.assertEqual(answer.getFileList(), [])

    def test_SpecialCases(self):
        '''
        Exceptional scenarios (that result in empty file list)
        '''
        
        # Emtpy folder
        answer = AnswerTwo(u'../test/Q2Test1/2nd_level')
        self.assertEqual(answer.getFileList(), [])
        
        # Empty file and file with space
        answer = AnswerTwo(u'../test/Q2Test1')
        self.assertEqual(answer.getFileList(), [])
        
        # The input is a file
        answer = AnswerTwo(u'../test/Q2Test2/2nd_level/A_file.rtf')
        self.assertEqual(answer.getFileList(), [])
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()