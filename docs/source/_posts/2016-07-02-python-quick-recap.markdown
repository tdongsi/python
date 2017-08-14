---
layout: post
title: "Python 2 quick recap"
date: 2016-07-02 00:23:27 -0700
comments: true
categories: 
- Tutorial
- Python
- TODO
---

What to review before a Python interview.
This blog post focuses on Python 2.7. 
Python 3 should be discussed in another blog post.

<!--more-->

### Basic

1. [Python tutorial](https://docs.python.org/2.7/tutorial/): especially ["Classes"](https://docs.python.org/2.7/tutorial/classes.html) and two ["Brief Tour of Standard Library"](https://docs.python.org/2.7/tutorial/stdlib.html) sections.
1. [String format](https://pyformat.info/) if you expect lots of string processing.
1. [Protocols](/blog/2016/09/05/tutorial-protocols/).

### Python decorator

Python decorator is a callable that takes a function as argument and returns a replacement function.

``` python Example decorator
>>> def outer(some_func):
...     def inner():
...         print "before some_func"
...         ret = some_func() # 1
...         return ret + 1
...     return inner
>>> def foo():
...     return 1
>>> decorated = outer(foo) # 2
>>> decorated()
before some_func
2
```

Python 2.4 provided support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol.

``` python A generic decorator
>>> def logger(func):
...     def inner(*args, **kwargs): #1
...         print "Arguments were: %s, %s" % (args, kwargs)
...         return func(*args, **kwargs) #2
...     return inner

>>> @logger
... def foo1(x, y=1):
...     return x * y
```

Note that decorators implemented as functions above are stateless.
For stateful decorators (e.g., counter), they should be implemented as a class (see [here](http://scottlobdell.me/2015/04/decorators-arguments-python/)).

#### Reference

RECOMMENDED:

* [Decorator tutorial](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)
* [Decorator with arguments](http://scottlobdell.me/2015/04/decorators-arguments-python/)

EXTRA READING:

* [Python-inspired decorator in Groovy](https://github.com/yihtserns/groovy-decorator)
* [Decorator library](https://wiki.python.org/moin/PythonDecoratorLibrary)

### Python generator

