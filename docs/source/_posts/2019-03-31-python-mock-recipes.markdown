---
layout: post
title: "Python mock recipes"
date: 2019-03-31 22:49:05 -0700
comments: true
categories: 
- Python
---

Recipes for mocking when writing unit tests in Python.

<!--more-->

### Basic mocking

### Mock simple HTTP responses

When testing REST clients that use `requests` module, it is better to use this utility method to construct simple HTTP responses.

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
This is useful as we can reproduce those exceptional, failure scenarios such as those with 4xx error codes.

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

        pass
```


### Mock print statements

###
