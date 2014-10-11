The solution uses Python version: 2.7

Answers to
Question 1: src/QuestionOne.py

============================
Directory listing
============================

src/
MyLogger.py: my logging configuration. In summary, info to screen and debug to file.

QuestionOne.py: answer to Question 1.
The answer is encoded as class AnswerOne. The main() function demonstrates how to use
the class.

test/
QuestionOneTest.py: Test cases for answer to QuestionOne, using python unittest module.

============================
How to run
============================
It is easier to run in Eclipse with PyDev plug-in.

Question 1: From src folder
Run solution from Terminal: python QuestionOne.py
Run test cases from Terminal: python ../test/QuestionOneTest.py

============================
Discussion
============================

How to test Answer to Question 1:
Q1:
The tests for answer to Question 2 are organized as unit tests, based on unittest module.
This answer assumes that there is no dependency cycle, such as (two rows X1 X2, X2 X1).
The unit tests and test case files check for correctness for standard tree as well as
special tree structures (e.g., multiple parents) and special cases (e.g., invalid key).


