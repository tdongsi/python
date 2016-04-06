'''
@author: tdongsi
'''
import unittest

from practice.app1.QuestionOne import *


class Test(unittest.TestCase):

    def test_fileOne_functional(self):
        answer = AnswerOne('Q1Test1.txt')
        self.assertEqual(answer._getValueSet('X1'), set(['X1', 'X2', 'X4', '1', '2', '3','X5', 'X3', 'X6', 'X7']))
        self.assertEqual(answer._getValueSet('X2'), set(['X2', 'X4', '1', '2', '3','X5']))
        self.assertEqual(answer._getValueSet('X3'), set(['X3', 'X6', 'X7']))
        self.assertEqual(answer._getValueSet('X4'), set(['X4', '1', '2', '3']))


    def test_fileOne_invalid(self):
        answer = AnswerOne('Q1Test1.txt')
        self.assertEqual(answer.getValueString('X5'),'')
        self.assertEqual(answer.getValueString('X6'),'')
        self.assertEqual(answer.getValueString('X7'),'')
        self.assertEqual(answer.getValueString('NonExistent'),'')
    
    def test_fileTwo_functional(self):
        answer = AnswerOne('Q1Test2.txt')
        self.assertEqual(answer._getValueSet('X1'), set(['X1', 'X2', 'X3', '1', '2', '3','X4', 'X5']))
        self.assertEqual(answer._getValueSet('X2'), set(['X2', 'X4', '1', '2', '3']))
        self.assertEqual(answer._getValueSet('X3'), set(['X3', 'X4', '1', '2', '3']))
        self.assertEqual(answer._getValueSet('X4'), set(['X4', '1', '2', '3']))


    def test_fileTwo_invalid(self):
        answer = AnswerOne('Q1Test2.txt')
        self.assertEqual(answer.getValueString('X5'),'')
        self.assertEqual(answer.getValueString('X6'),'')
        self.assertEqual(answer.getValueString('NonExistent'),'')
            
    def test_emptyfile(self):
        answer =  AnswerOne('Q1Test3.txt')
        self.assertEqual(answer.getValueString('NonExistent'),'')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()