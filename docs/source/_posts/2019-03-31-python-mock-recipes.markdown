---
layout: post
title: "Python mock recipes"
date: 2019-03-31 22:49:05 -0700
comments: true
categories: 
- Python
---

Recipes for mocking with `unittest.mock` module when writing unit tests in Python.

<!--more-->

### Mock simple HTTP responses

When testing REST clients that use `requests` module, it is better to use this utility method to construct mock HTTP responses.

``` python Utility method to create mock response
def create_mock_response(status=200, content="{}"):
    """ Create mock HTTTP responses for "requests" module.

    :param status: override Response.status_code. Example: 200
    :param content: override Response.text and Response.content.
    :return: mock response object
    """
    mock_response = mock.Mock()
    mock_response.status_code = status
    mock_response.text = content
    mock_response.content = content

    return mock_response
```

By mocking HTTP (usually GET) responses, you can validate the REST client's behavior for a certain response.
This is useful as we can reproduce exceptional, failure scenarios such as those with 4xx error codes.

``` python Example test
    @mock.patch('requests.get')
    def test_get_deployments_429(self, mock_get):
        """ Failure case. """
        # Mock response
        mock_text = u'{"reponse": "Slow down."}'
        mock_response = base.create_mock_response(status=429, content=mock_text)

        mock_get.return_value = mock_response

        # REST client's function that sends GET request here
        # ...
        with self.assertRaises(ResponseRateException) as bg:
            method_under_test(**arguments)

        self.assertTrue('request not accepted' in bg.exception.message)

        pass
```

### Redirect `stdout` output to variable for validation

Some legacy codes tend to spam `print` statements and you probably need to check if the output is correct.
In that case, we can redirect `print`'s output to some variable and assert the value of that string variable.

There is a popular but complex way to redirect `stdout` to a string variable, thanks to being the [top and accepted answer on Stackoverflow](https://stackoverflow.com/questions/1218933/can-i-redirect-the-stdout-in-python-into-some-sort-of-string-buffer).

``` python Complex way
from StringIO import StringIO  # Python2
from io import StringIO  # Python3
 
 import sys
 
# Store the reference for restoring
 
old_stdout = sys.stdout
 
# This variable will store everything that is sent to the standard output
sys.stdout = StringIO()

call_method_under_test()
 
# Redirect again the std output to screen
sys.stdout = old_stdout
 
# Then, get the stdout like a string
result_string = result.getvalue()
 
assert(expected_output, result_string)
```

In the context of unit testing, to ensure that all unit tests are indepedenent, you have to set and reset `sys.stdout` in each unit test separately.
As a result, it is very inconvenient when you may have hundreds of unit tests and only tens of them need that output redirection for validation.
Instead, `mock` module makes it easy as follows:

``` python Mock print statements
        # Mock sys.stdout to redirect "print"'s output to a variable mock_stdout
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            method_under_test(**arguments)
            # result_string is what method_under_test print out
            result_string = mock_stdout.getvalue()
            # Compare two objects from two JSON strings
            self.assertEqual(expected_output, result_string)
```

### Skip waiting when testing

Many methods under test need to sleep while waiting for some external factor before proceeding to its next stage.
If the external components (e.g., HTTP responses) are already mocked out, such waiting maybe not necessary and we'd like to skip the waiting parts.
Using `mock.patch`, it is easy to mock out `time.sleep` to skip such waiting parts.

``` python Skip waiting
        # Mock time.sleep to skip sleeping
        with mock.patch('time.sleep', return_value=None):
            # Mock sys.stdout to redirect "print" statement's output to a variable mock_stdout
            with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                execute_long_running(0.25, {})

            # result_string is what _execute_canary_deployment prints out
            result_string = mock_stdout.getvalue()
            self.assertTrue('expected string' in result_string)
```
