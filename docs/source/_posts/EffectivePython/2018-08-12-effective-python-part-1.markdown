---
layout: post
title: "Effective Python: Part 1"
date: 2018-08-12 00:19:06 -0700
comments: true
categories: 
---

This post corresponds to Lesson 1 "Using Expressions and Statements" of ["Effective Python" course](https://www.safaribooksonline.com/videos/effective-python/9780134175249).

<!--more-->

### Item 1: Slice sequences

Use `mlist[start:end]`.

1) Note that `a[:20]` or `a[-20:]` will quietly return the full list even when the list is smaller in size.
Meanwhile, `a[20]` or `a[-20]` will throw IndexError exception.
It could be pro or con, depending on the situation and if the programmer is aware of it.

2) Slice assignment can be used to truncate the list in the middle. Example: `a[2:7] = []`.

`b=a[:]` is the idiom to create a copy of a list.

3) Be careful with the following idiom to get the last `n` items of the list.

``` python WRONG: For input n, return the last n items from list
n = 3
print mlist[-n:]
```

The above code works in most cases. However, if `n` takes the value of 0, then it will return the whole list.

### Item 2: Avoid using start, end, and stride in a single slice

Sequences can be sliced with the following syntax `a[start:end:stride]`.

1) `a[::-1]` is the common idiom to reverse a sequence. However, be careful when using the idiom with string, esepcially UTF-8 string.

``` python WRONG: Reverse UTF-8 string
w = 'hello'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')
```

In this case, if the input `w='谢谢'` with non-ASCII characters, `UnicodeDecodeError` might be thrown.

2) The author cautions against using all `start:end:stride` in a slice since it will be very confusing, especially with negative numbers.
For example, `a[-2:2:-2]` is very unintuitive to figure out which items will be selected.
The best practices are:

1. If you must use stride, use positive number only.
1. Split `start:end:stride` into two operations: stride first `b=a[::-2]`, followed by truncation `c=b[-2:2]`. The order can be changed to get smallest intermediate subsequence.

### Item 3: Prefer `enumerate` over `range`

Instead of `for` loop over `range(len(mlist))` to get the index, use this:

```python enumerate example
for idx, item in enumerate(mlist, 1):
    print idx, item
```

### Item 4: Use `zip` to process iterators in parallel

``` python Example of zip
def main():
    names = ['Kelly', 'Lise', 'Marie', 'Alexander']
    letters = [len(e) for e in names]

    # Better way: use zip
    print better_way(letters, names)

    # In Python2, zip returns a list instead of a generator.
    print zip(letters, names)
    # In Python3, the above will print some "<zip object at 0x12345>".

    # To get something similar to Python3,
    # Use izip in itertools
    print python3_way(letters, names)

    pass


def python3_way(letters, names):
    """Find the longest name"""
    from itertools import izip
    longest_name = None
    current_max = 0
    for length, name in izip(letters, names):
        if length > current_max:
            current_max = length
            longest_name = name
    return longest_name


def better_way(letters, names):
    """Find the longest name"""
    longest_name = None
    current_max = 0
    for length, name in zip(letters, names):
        if length > current_max:
            current_max = length
            longest_name = name
    return longest_name
```

1) Note that, in Python2, `zip` returns a list instead of a generator object like in Python3.
To simulate that behavior in Python3, use `izip` from `itertools` module.

2) The default behavior of `zip` is to stop after reaching the end of the shortest iterator.
To iterate until the end of the longest iterator, use `itertools.zip_longest` in Python3 and `itertools.izip_longest` in Python2.

### Item 5: Avoid `else` blocks after `for` and `while` loops

If you don't know that you can add an `else` block after `for` or `while` loops, you're better off that way.
The `else` block after loops are really confusing to all programmers who write or read the code.

The `else` block is originally intended for searching something in a loop, break if the search fails.
However, the name `else` is probably extremely poor choice, given the semantics of `else` in other constructs such as `if` or `try`. 
Because of that, it is clearer to simply write a helper function before checking in a loop.

### Item 6: Take advantage of each block in `try`/`except`/`else`/`finally`

``` python Function of each block
try:
    print "Main action"
except:
    print "Handle exception"
else:
    print "When there is no exception"
finally:
    print "Always"
```

1) In Python 3, reading and writing Unicode to file is simple.
In Python2, you have to use `io` module.
In addition, the string is not Unicode by default. 
You have to mark Unicode literals with prefix u (e.g., u’Hello’).

``` python Unicode read/write in Python3
handle = open('/tmp/random_data.txt', 'w', encoding='utf-8')
handle.write('success\nand\nnew\nlines')
handle.close()

handle = open('/tmp/random_data.txt')  # Raise IOError
try:
    data = handle.read()   # Raise UnicodeDecodeError
finally:
    handle.close()
```

``` python Unicode read/write in Python2
import io

handle = io.open('/tmp/random_data.txt', mode='w', encoding='utf-8')
handle.write(u'success\nand\nnew\nlines')
handle.close()

handle = io.open('/tmp/random_data.txt', encoding='utf-8')  # Raise IOError
try:
    data = handle.read()   # Raise UnicodeDecodeError
finally:
    handle.close()
```

2) The above code is the correct way to handle file opening/closing.
One common mistake is as follows:

``` python WRONG: Common mistake in file handling
try:
    handle = io.open('/tmp/bad_path.txt', encoding='utf-8')  # Raise IOError
    data = handle.read()   # Raise UnicodeDecodeError
finally:
    handle.close()   # Raise IOError
```

In this code, in the event of file can't be opened, an IOError exception will be thrown. 
However, after the exception is handled, in the `finally` block, another exception will be thrown since file is not open and `handle` is `None`.
This exception is now unexpected and can't be handled properly.
Instead of committing the above mistake, we should open the file outside the `try` block and if file opening fails, finish code execution since we can't really do anything without file open.
If you want to explicitly handle IOError exception, enclose it with another `try` block.

### Item 7: Consider context manager (contextlib) and `with` statements for `finally` behavior

