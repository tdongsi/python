---
layout: post
title: "Effective Python Pt. 2: Comprehensions & Generators"
date: 2018-08-12 00:19:30 -0700
comments: true
categories: 
- Book
- Python
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

The problems with list comprehensions are that they may create a whole new list containing all the data.
For large inputs, it can consume a significant amount of memory and can even crash your program.

For a (very contrived) example, let's say you want to return the length of each line in a file and its squares.
You can easily achieve that with the following list comprehensions.

``` python List comprehension on a file
value = [len(x) for x in open('/tmp/my_file.txt')]
squares = [(x, x**2) for x in better]
```

However, list comprehension on a file like this is very risky.
The file can be really large or even never ending (such as a network socket).
To solve this problem, Python has generator expressions, which are a generalization of comprehensions and generators.
A generator expression gives you an iterator that you can go through that will yield one item at a time from the input and you can determine how many output items you want to return.
The above code can be rewritten as follows:

``` python Generator expression
better = (len(x) for x in open('/tmp/my_file.txt'))
roots = ((x, x**0.5) for x in better)
print(next(roots))
print(next(better))
print(next(roots))

### Example Output
[37, 20, 60, 38, 85, 65, 96, 4, 45, 44]
(37, 1369)
20
(60, 3600)
```

As you can see, another powerful outcome of using generator expressions is that they can be composed together.
When you call `next(roots)`, Python goes back up to the generator expression `better`, then realizes that it has to read another line out of the file. 
It has to read the line, then compute its length. 
That length value is then passed back to `roots` as `x` and for computing the tuple.
What's surprising is that chaining generators like this actually executes very quickly in Python.
When you're looking for a way to compose functionallity that's operating on a large stream of input, generator expressions are one of the best tools for the job.

### Item 11: Consider generator functions instead of returning lists

Let's say you want to find the index of every single words in a string.
The typical approach will be something as follows:

``` python Typical way
def index_words_typical(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result
```

The typical approach that returns a list of indices has a problem.
It is dense and noisy with all logistics related to `result` list: initializing the list, appending to the list whenever a result is found.
A better way to write this function is to use a generator function, with `yield` statements, as follows:

``` python Better way
def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index+1
```

``` python Equivalent outputs
address = 'The quick brown fox jumps over the lazy dog'
print(list(index_words(address)))
print(index_words_typical(address))

# Output
[0, 4, 10, 16, 20, 26, 31, 35, 40]
[0, 4, 10, 16, 20, 26, 31, 35, 40]
```

As you can see, the generator version of this function is much easier to read than the typical version that returns lists.
Most significantly, all of the interactions with the `result` list have been taken away.
Instead, you just have those `yield` statements, making it very obvious what is being returned.
That helps make it clear to new readers of the code.

The second problem of the typical approach is that it requires all results to be stored in the lists before being returned.
For huge inputs, this can cause your program to run out of memory and crash.
In contrast, the generator version of the function can handle any amount of output because it doesn't actually keep all of the results in memory that it found.
In the example above, if the input `address` is a huge text and you only need to display the first hundred indices, the typical approach `index_words_typical` might fail while the generator version works perfectly fine.

### Item 12: Be defensive when iterating over arguments

``` python Iterator as argument
def normalize_data(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100.0 * value / total
        result.append(percent)
    return result

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)
```

``` python Testing
path = '/tmp/my_numbers.txt'
with open(path, 'w') as f:
    for i in [15, 80, 35]:
        f.write('%d\n' % i)

print(normalize_data([15, 80, 35]))
print(normalize_data(read_visits(path)))
```

``` plain Output
[11.538461538461538, 61.53846153846154, 26.923076923076923]
[]
```

As you can see from the output, `normalize_data` works fine with a list of numbers but it does not work when we are supplying an iterator as input.
The main reason is that we iterate multiple times with the input iterator.
After the first traversal for `sum`, the iterator is already exhausted and that explains an empty list for the output `result`.

The most straight-forward fix for the function `normalize_data` is probably to add a line `numbers = list(numbers)` at the beginning to materialize the iterator.
However, such fix will defeat the purpose of using iterators and the function `read_visits`: they allow handling a arbitrarily large number of inputs without committing a large working memory.

Another possible fix for the function `normalize_data` is as folllows:

``` python Another fix
def normalize_data_2(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100.0 * value / total
        result.append(percent)
    return result

get_iter = lambda: read_visits(path)
print(normalize_data_2(get_iter))
```

In this approach, we recreate the iterator whenever we need to iterate the data.
So, if we need to traverse twice to normalize the data, we have to call `read_visits` twice, open the file, and read the data that many times.
The upside is that we have the correct behavior while still retaining the benefits of using iterators.
The problem of this approach is that it is very noisy and hard to read with `get_iter` and `lambda`.
A more Pythonic way to do the same thing is to use a container class for the behavior of `read_visits`, as follows:

``` python Converting read_visits to a class
class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits(path)
print(normalize_data(visits))
```

Here, `normalize_data` can be the same as before.
The idea is still the same, we recreate the iterator whenever we need to iterate the data.
In the example, when we iterate the `numbers` for computing `sum` or in `for` loop in `normalize_data` method, we effectively call `iter(numbers)` to retrieve the iterators.
It is defined in `__iter__` method, which will open the file and read the data whenver it is called.
However, it is much clearer and more readable than before since we encapsulate the behavior of `read_visits` method into the class `ReadVisits`.

Finally, one minor improvement that we can add is to validate if the input argument of `normalize_data` is a container, as opposed to plain old iterator.
If the argument is a plain old iterator, its data can be exhausted after first traversal and the `normalize_data` method will not behave correctly.
To check that, a simple check "iter(numbers) is iter(numbers)" will suffice.
For container-type arguments such as a list or `ReadVisits` object, each `iter` call returns a different iterator.
