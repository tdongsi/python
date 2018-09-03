---
layout: post
title: "Effective Python Pt. 2: Comprehensions & Generators"
date: 2018-08-12 00:19:30 -0700
comments: true
categories: 
---

This post corresponds to Lesson 2 "Comprehensions & Generators" of ["Effective Python" course](https://www.safaribooksonline.com/videos/effective-python/9780134175249).

<!--more-->

### Item 8: Use list comprehension instead of MAP and FILTER

List comprehension offers the more intuitive way to transform a list to another list.
Note that in Python 3, the `map` function now returns an iterator instead of a list like Python 2.
Therefore, you have to add an extra step to convert to a list.

``` python List comprehension
a = range(10)
# Recommended
squares = [x**2 for x in a]
# Old way: map in Python 2
squares = map(lambda x: x**2, a)
# Old way: map in Python 3
squares = list(map(lambda x: x**2, a))
print(squares)
```

In addition, list comprehension makes it easy to add a condition for filtering.
Using `filter` and `map`, it becomes very "noisy" with multiple enclosing functions and lambdas, as shown below.

``` python List comprehension with filtering
b = range(5)
# Recommended
squares = [x**2 for x in b if x % 2 == 0]
# Old way in Python 2
squares = map(lambda x: x**2, filter(lambda x: x % 2 == 0, b))
```

Dictionary and set also have similar comprehension expressions for similar purposes.
The final note is that for very complex transformations and filtering that is not easy to pack into comprehension expressions, it is recommended to explicitly use the `for` loop instead.

