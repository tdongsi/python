The solution uses Python version: 2.7

Answers to
* Question 1: src/QuestionOne.py
* Question 2: src/QuestionTwo.py

Directory listing
============================

**src/**

MyLogger.py: my logging configuration. In summary, info to screen and debug to file.

QuestionOne.py: answer to Question 1. 

The answer is encoded as class AnswerOne. The main() function demonstrates how to use
the class.

QuestionTwo.py: answer to Question 2.

The answer is encoded as class AnswerTwo. The main() function demonstrates how to use
the class.

**test/**

QuestionOneTest.py: Test cases for answer to QuestionOne, using python unittest module.

QuestionTwoTest.py: Test cases for answer to QuestionTwo, using python unittest module.

Q1Test1.txt: Test case 1 for Q1, specifying a tree structure based on the problem description.

Q1Test2.txt: Test case 2 for Q1, tree with two parent nodes sharing a child node. 

Q2Test1: Test case 1 for Q2: for cases of empty folder, folder with empty file, etc.

Q2Test2: Test case 2 for Q2, based on the problem description.

How to run
============================
It is easier to run in Eclipse with PyDev plug-in.

Question 1: From src folder
* Run solution from Terminal: python QuestionOne.py
* Run test cases from Terminal: python ../test/QuestionOneTest.py

Question 2:
* Run solution from Terminal: python QuestionTwo.py
* Run test cases from Terminal: python ../test/QuestionTwoTest.py

Discussion
============================

How to test Answer to Question 1:

The tests for answer to Question 2 are organized as unit tests, based on unittest module.
This answer assumes that there is no dependency cycle, such as (two rows X1 X2, X2 X1).
The unit tests and test case files check for correctness for standard tree as well as
special tree structures (e.g., multiple parents) and special cases (e.g., invalid key).


How to test Answer to Question 2:

The tests for answer to Question 2 are organized as unit tests, based on unittest module.
One functional aspect of the program is to validate the IPv4 address string in a file.
Tests for this functionality is included into the text files in Q2Test2 directory and its sub-
directory. Text files in Q2Test2 includes positive cases and negative cases such as:
* 256.12.36.198
* 0.0.0.0.0
* 127.1
* 127...1
* 0.0.0.-0

Because of that, there is no test for IPv4 validation in unit test QuestionTwoTest.py. Instead,
the module tests exceptional scenarios in terms of file system, such as empty directory.

Other corner test cases that are not feasible for the current assignment:
* Large text files.
* Long file paths.
* Files with different EOL.
