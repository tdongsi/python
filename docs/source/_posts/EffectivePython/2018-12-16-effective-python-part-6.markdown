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

### Item 30: Debugging with `pdb`

``` python Use debugger
# Code before
import pdb; pdb.set_trace()
# Code after
```

A few debugger commands when you are already in the debugger:

``` plain
next
step
locals()
bt  # back trace
up
down
```

The Python debugger `pdb` is very similar to C debugger in Linux.
However, you are probably better off with debugger in proper IDEs such as PyCharm with better visualization.

### Iten 31: Profile before optimizing

In summary, how to do CPU profiling in Python.

Dynamic nature of Python programs can lead to surprising performance impact.
Profiling is easy to do in Python with built-in modules, as shown below, and allows us to focus on measurable sources of performance bottlenecks.

``` python Profiling in Python
from cProfile import Profile
from pstats import Stats

profiler = Profile()
# profiler.runcall(insertion_sort, data)
profiler.runcall(lambda: insertion_sort(data))

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
```

``` plain Profiler output
         20003 function calls in 0.791 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.791    0.791 item31.py:27(<lambda>)
        1    0.002    0.002    0.791    0.791 item31.py:7(insertion_sort)
    10000    0.780    0.000    0.789    0.000 item31.py:14(insert_value)
     9989    0.010    0.000    0.010    0.000 {method 'insert' of 'list' objects}
       11    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

Another print method `stats.print_callers()` can reorganize the same information in a different way.

``` plain
   Ordered by: cumulative time

Function                                          was called by...
                                                      ncalls  tottime  cumtime
item31.py:25(<lambda>)                            <-
item31.py:8(insertion_sort)                       <-       1    0.002    0.023  item31.py:25(<lambda>)
item31.py:15(insert_value)                        <-   10000    0.004    0.021  item31.py:8(insertion_sort)
{method 'insert' of 'list' objects}               <-   10000    0.011    0.011  item31.py:15(insert_value)
{_bisect.bisect_left}                             <-   10000    0.006    0.006  item31.py:15(insert_value)
{method 'disable' of '_lsprof.Profiler' objects}  <-
```

More details can be found in [Python documentation](https://docs.python.org/2/library/profile.html).

### Item 32: Use tracemalloc to undertand memory usage and leaks

In summary, this item is about how to do memory profiling in Python.

Python has automatic garbage collection: reference counting and cycle detection for looping references.
Despite that, memory leaks still happen and it's hard in practice to figure out why references are held.

``` python gc module
import gc

found_objects = gc.get_objects()
print('%d objects before' % len(found_objects))

import waste_memory
x = waste_memory.run()

found_objects = gc.get_objects()
print('%d objects after' % len(found_objects))
```

`gc` module allows you to interact with garbage collectors and take a look into how many objects created, as shown above.
However, such information is usually not enough to figure out what went wrong: objects of the same class can be created in various ways.
You need more information to figure out where the allocation and the memory leak happens.

In Python 3, we have `tracemalloc` module that allows comparing between two memory snapshots and trace back to the code lines where such memory allocations happen. 
See [more examples](https://pytracemalloc.readthedocs.io/examples.html).
For Python 2.7, it is not part of the Standard Library.
Therefore, we have to patch and compile Python 2.7 to use the 3rd party `pytracemalloc` module.
The instructions to do it can be found in [here](http://carsonip.me/posts/debugging-memory-usage-python-tracemalloc/).
