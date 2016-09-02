---
layout: post
title: "Tutorial: Protocols"
date: 2016-09-05 23:50:24 -0700
comments: true
categories: 
- Tutorial
- Python
- TODO
---

Python uses "duck typing". 
It does not have interfaces like Java to enforce certain behaviors: 
`Iterable` iterface means that you can iterate an object of that class in a `for each` loop.
In Python, to do that, you have to override magic functions like `__iter__` to achieve some behaviors.
Each behavior is called "protocol" in this post since some involves overriding multiple magic funtions.

<!-- Reference:
Evernote: "OOP in Python"
-->

<!--more-->

### Iterator

Here, `__iter__` just returns self, an object that has the function next(), which (when called) either returns a value or raises a StopIteration exception.
We’ve actually already met several iterators in disguise; in particular, `enumerate` is an iterator. 
To drive home the point, here’s a simple reimplementation of `enumerate`:

``` python Implement enumerator() as iterator
>>> class my_enumerate:
...   def __init__(self, some_iter):
...      self.some_iter = iter(some_iter)
...      self.count = -1
...
...   def __iter__(self):
...      return self
...
...   def next(self):
...      val = self.some_iter.next()
...      self.count += 1
...      return self.count, val
>>> for n, val in my_enumerate(['a', 'b', 'c']):
...   print n, val
0 a
1 b
2 c
```

#### Generator and Iterator protocol

It is also much easier to write routines like enumerate as a generator than as an iterator:

``` python Implement enumerate() using generator
>>> def gen_enumerate(some_iter):
...   count = 0
...   for val in some_iter:
...      yield count, val
...      count += 1
```

But you can do things with generators that you couldn’t do with finite lists. 
Consider two full implementation of Eratosthenes’ Sieve for finding prime numbers. 
Full discussion is [here](http://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/idiomatic-python.html). 
Most of these are from "Python tutorial".

### Container

