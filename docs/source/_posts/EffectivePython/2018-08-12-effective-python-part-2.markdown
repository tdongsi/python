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

### Item 9: Avoid more than two expressions in list comprehensions

As examples, the transformations of two-dimensional matrices can be done easily with list comprehensions, as follows.

``` python Transforming matrices
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [x for row in matrix for x in row]
print(flatten)

squared = [[x**2 for x in row] for row in matrix]
print(squared)
```

However, for 3D (or more) matrices, such approach with list comprehensions can be really hard to read.

``` python 3D matrix
# 3D matrix
matrix = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
]
flatten = [x for sublist1 in matrix
           for sublist2 in sublist1
           for x in sublist2]
print(flatten)
```

As shown above, even a simple transformation of matrix flattening can make the code hard to read due to multiple levels of `for` loops.
Instead of using list comprehensions in those cases, it is recommended to explicitly use `for` loops when there are more than two expressions in such list comprehensions.

``` python 3D matrix
# Recommended way
flatten = []
for sublist1 in matrix:
    for sublist2 in sublist1:
        flatten.extend(sublist2)
print(flatten)
```

Another example of abusing list comprehension is to perform multiple filtering operations, such as:

``` python Multiple filtering operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
print(filtered)
```

In this example, the expression performs filtering not only on rows in the matrix but also on elements in rows.
Such expressions are really hard to understand since the code is not read in the natural order of logic and flow of thoughts (see [literate programming](https://en.wikipedia.org/wiki/Literate_programming)).
It is recommended to explicitly use `for` loops for such cases.

### Item 10: Consider generator expressions for large comprehensions


