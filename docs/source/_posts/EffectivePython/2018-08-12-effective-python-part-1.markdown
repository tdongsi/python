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

Note that `a[:20]` or `a[-20:]` will quietly return the full list even when the list is smaller in size.
Meanwhile, `a[20]` or `a[-20]` will throw IndexError exception.
It could be pro or con, depending on the situation and if the programmer is aware of it.

Slice assignment can be used to truncate the list in the middle. Example: `a[2:7] = []`.

`b=a[:]` is the idiom to create a copy of a list.

Be careful with the following idiom to get the last `n` items of the list.

``` python WRONG: For input n, return the last n items from list
n = 3
print mlist[-n:]
```

The above code works in most cases. However, if `n` takes the value of 0, then it will return the whole list.

### Item 2: Avoid using start, end, and stride in a single slice

### Item 3: Prefer `enumerate` over `range`

### Item 4: Use `zip` to process iterators in parallel

### Item 5: Avoid `else` blocks after `for` and `while` loops

### Item 6: Take advantage of each block in `try`/`except`/`else`/`finally`

### Item 7: Consider context manager (contextlib) and `with` statements for `finally` behavior

