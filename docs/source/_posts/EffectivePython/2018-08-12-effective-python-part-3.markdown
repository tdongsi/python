---
layout: post
title: "Effective Python Pt. 3: Functions"
date: 2018-08-12 00:19:32 -0700
comments: true
categories: 
- Book
- Python
---

This post corresponds to Lesson 3 "Using Functions" of ["Effective Python" course](https://www.safaribooksonline.com/videos/effective-python/9780134175249).

<!--more-->

### Item 13: Know how closures interact with variable scope

For this item's discussion, let's say that we have a list of integers that needs to be sorted, with the twist that some of those integers are in a special group (higher prirority) and has to be placed in front of the list.
For example, those integers could be IDs of different UI components, with those of higher priority belong to the foreground and the rest are in the background.
One solution to this problem is as follows:

``` python Sort with priority
NUMBERS = [8, 3, 1, 2, 5, 4, 7, 6]
GROUP = {2, 3, 5, 7}

def sort_priority(numbers, group):
    """ Sort the input numbers but put those in "group" first.

    :param numbers: list of input numbers.
    :param group: set of numbers in priority group.
    """

    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    pass

def main_original():
    numbers = NUMBERS[:]
    print(sort_priority(numbers, GROUP))
    print(numbers)
```

Now, the additional requirement is that we want to know if any item in the input list belongs to the priority `GROUP`.
The naive modification to the original solution proves not working as expected:

``` python Naive solution
def sort_priority(numbers, group):
    """ Sort the input numbers but put those in "group" first.

    :param numbers: list of input numbers.
    :param group: set of numbers in priority group.
    :return: True if any number in priority is found.
    """
    found = False

    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found
```

In this naive (and incorrect) solution, an additional variable `found` is used to track if any element in the input list `numbers` is special and set accordingly.
However, the above `sort_priority` method always returns `False`, regardless of the input list of numbers.

The reason for this is a common mistake of Python users when using the same variable in different scopes.
In this example, `found` is found in two different scopes: in the enclosed `helper` method and in the enclosing `sort_priority` method.
In most cases, when we simply refer to a variable (i.e., read operation), Python will do its best to look up for that variable in different scopes, as shown below.

``` python Variable reference in different scopes.
meep = 23

def enclosing():
    """ Variable reference in different scopes.
    """
    foo = 15

    def my_func():
        bar = 10

        print(bar)      # local scope
        print(foo)      # enclosing scope
        print(meep)     # global scope
        print(str)      # built-in scope
        # print(not_exist)  # not found in any scopes

    my_func()

enclosing()

# Output:
# 10
# 15
# 23
# <type 'str'>
```

However, variable assignment has different treatment.
When we try to assign to a variable for the first time in the inner scope, Python will create a new local variable.
This will lead to subtle difference if we have variable assignment in the inner scope, as shown in the following example.

``` python Variable assignment in different scopes.
def enclosing_assignment():
    """ Variable assignment in different scopes.
    """

    foo = 15
    foo = 25

    def my_func():
        foo = 15
        bar = 5

        print(foo)
        print(bar)

    my_func()
    print(foo)

enclosing_assignment()

# Output:
# 15
# 5
# 25
```

Going back to our original problem in `sort_priority`, the problem of our naive solution is that we have assignment to the variable `found` in the inner scope.
Python will create a new variable in `helper`'s scope and ignore the `found` already defined in the outer scope `sort_priority`.
After `helper` method is done, `found` variable in `sort_priority` scope still has the original value `False` and it is what the method returns.




Solution:

* In Python 3, nonlocal. Problem: it can be confusing if the variable is declared a couple of layers away.
* In Python 2, using array. It is a trick.
* In both Python versions and recommended way, use the helper class.
  * We have a state to keep track of it. It is better to keep it in an object and update the object accordingly.

