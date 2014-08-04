Each Objy test is specified by its test folder, a QAS file, and a CFG file.
The purpose of this TestRunner framework is to update the QAS and CFG file accordingly,
based on the user inputs, and run the test.

It will read the test suite file name.suite that has the following format, 
for each line corresponding to a test:

TEST_PATH;QAS_FILE_NAME;CFG_FILE_NAME  
