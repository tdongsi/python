---
layout: post
title: "Effective Python Pt. 6: Robust Programs"
date: 2018-12-16 17:58:58 -0800
comments: true
categories: 
- Python
- Book
---

This post corresponds to Lesson 6 "Making Programs Robust" of ["Effective Python" course](https://www.safaribooksonline.com/videos/effective-python/9780134175249).

NOTE: While the book is about Python 3, my blog checks out its application in Python 2. 

<!--more-->

### Item 28: Use virtualenv

Use `pip` commands for virtual environment management.

``` plain

$ pip show flask
Name: Flask
Version: 1.0.2
Summary: A simple framework for building complex web applications.
Home-page: https://www.palletsprojects.com/p/flask/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD
Location: /Users/tdongsi/Matrix/python/venv/lib/python2.7/site-packages
Requires: Werkzeug, click, Jinja2, itsdangerous
Required-by:

$ pip install --upgrade Jinja2
Requirement already up-to-date: Jinja2 in ./venv/lib/python2.7/site-packages (2.10)
Requirement already satisfied, skipping upgrade: MarkupSafe>=0.23 in ./venv/lib/python2.7/site-packages (from Jinja2) (1.1.0)

$ pip list
Package                  Version
------------------------ ----------
alabaster                0.7.12
Babel                    2.6.0
certifi                  2018.11.29
chardet                  3.0.4
Click                    7.0
...

$ pip freeze
alabaster==0.7.12
Babel==2.6.0
certifi==2018.11.29
chardet==3.0.4
Click==7.0
...

$ pip freeze > requirements.txt

# In another virtualenv
$ pip install -r requirements.txt
```

Set up and use virtual environment in Python 2.

``` plain

# Create new virtual env
$ virtualenv venv
New python executable in /Users/tdongsi/Matrix/python/venv/bin/python
Installing setuptools, pip, wheel...
done.

# Activate new virual env
$ source venv/bin/activate

$ deactivate
```

#### Python 3

The difference in Python 3 is the dedicated command `pyvenv` and no separate installation of `virtualenv` is required.

``` plain virtualenv in Python 3
$ pyvenv -h

# Create new virtual env
$ pyvenv myproject

# Activate new virual env
$ source myproject/bin/activate

$ deactivate
```

### Item 29: Tests with unittest

Tests are even more important in Python (than Java) since it is a dynamic language.
`unittest` module can be used for both unit tests (isolated tests) and functional/integration tests (verifying interactions).

``` python unittest examples
from unittest import TestCase

class ExampleTest(TestCase):

    def setUp(self):
        print('Setup')

    def tearDown(self):
        print('Teardown')

    def test_a(self):
        print('a')

    def test_b(self):
        print('b')


if __name__ == '__main__':
    unittest.main()
```
