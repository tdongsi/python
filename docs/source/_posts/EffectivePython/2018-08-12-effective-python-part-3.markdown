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

For this item's discussion, let's say that we have a list of integers that needs to be sorted, with the twist that some of those integers are in a special group (higher prirority) and has to be placed in front of the list (referred as **Problem-1**).
For example, those integers could be IDs of different UI components, with those of higher priority belong to the foreground and the rest are in the background.
One solution to this problem is as follows:

``` python Solution to Problem-1
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

Now, the **additional requirement** is that we want to know if any item in the input list belongs to the special `GROUP` (now referred as **Problem-2**).
To accommodate this new requirement, one can naively modify Problem-1's solution as follows:

``` python Naive solution to Problem-2
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
However, this solution proves not working as expected: the above `sort_priority` method always returns `False`, regardless of the input list of numbers.

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

However, variable assignment has a slightly different treatment.
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

Going back to our Problem-2, the problem of our naive solution is that we have assignment to the variable `found` in the inner scope.
Python will create a new variable in `helper`'s scope and ignore the variable `found` already defined in the outer scope `sort_priority`.
After `helper` method is done, `found` in `sort_priority` scope still has the original value `False` and it is what the method returns.

There are many ways to work around the scope problem with variable assignment described above.
In Python 3, `nonlocal` keyword is introduced exactly for this situation.
The keyword `nonlocal`, similar to `global` keyword, allows you to assign to variables in outer, but non-global, scope.

``` python Using nonlocal keyword for Problem-2
def sort_priority_python_3(numbers, group):
    """ Sort the input numbers but put those in "group" first."""
    found = False

    def helper(x):
        if x in group:
            nonlocal found
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found
```

However, using `nonlocal` keyword can be confusing and is generally not recommended, especially if the variable is declared a couple of scopes/layers away from the assignment.
In addition, such approach would not work in Python 2.
In another approach that would work for both Python 2 and 3, one can use the following trick:

``` python Using array for Problem-2
def sort_priority_python_2(numbers, group):
    """ Sort the input numbers but put those in "group" first."""
    found = [False]

    def helper(x):
        if x in group:
            found[0] = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found[0]
```

In this trick, instead of using a boolean variable `found`, you use a singleton (one-element) array `found`. 
Because `found` is now an array, the variable reference rules, instead of variable assignment rules, apply and the `found` variable in the outer scope is used.
Although it is a great trick, such code is not really clear.

The final and recommended solution is to extract the `helper` function into a CheckSpecial class instead.
The original `helper` method used for **Problem-1** can be converted to a Helper/CheckSpecial class as follows:

``` python Using CheckSpecial class for Problem-1
class CheckSpecial(object):

    def __init__(self, group):
        self.group = group

    def __call__(self, x):
        if x in self.group:
            return (0, x)
        return (1, x)

def sort_priority_solved(numbers, group):
    helper = CheckSpecial(GROUP)
    numbers.sort(key=helper)
```

In the solution to starting **Problem-1** shown above, the origial `helper` function's logic has been encapsulated into a CheckSpecial class, in the `__call__` method specifically.
When the additional requirement "check if special number encountered" comes in, it is apparent that `helper` function has to become a stateful closure.
Since we already has it converted to `CheckSpecial` class, it would be easier to keep the state as a new `CheckSpecial` object's attribute `found` and update the object state accordingly, as follows:

``` python Updating CheckSpecial class for Problem-2
class CheckSpecial(object):

    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

def sort_priority_solved(numbers, group):
    helper = CheckSpecial(GROUP)
    numbers.sort(key=helper)
    return helper.found
```

IMHO, this approach is much clearer and works for both Python 2 and 3.

### Item 14: Accept callables for stateful closures

Many of Python APIs allow you to customize behavior by passing in a function, such as `sort(key=...)` method in the last section "Item 13".
We also see that it is possible to pass stateful closure as a function into those hooks for record-keeping purposes, for example.
We showed different ways to do that in Python 2 and 3: `nonlocal` keyword, `list` trick, and a helper class.
Using a class to encapsulate a stateful closure is the highly recommended approach.

``` python Another version of CheckSpecial class for Problem-2
class CheckSpecial(object):

    def __init__(self, group):
        self.group = group
        self.found = False

    def check(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

def sort_priority_solved(numbers, group):
    helper = CheckSpecial(GROUP)
    numbers.sort(key=helper.check)
    return helper.found
```

Let us consider an alternative version of CheckSpecial class where we use standard method name `check` instead of special method `__call__`.
And it works perfectly fine if you pass `helper.check` as a function: `sort` has no idea that we are passing a method of a stateful object and it does not care.

However, for programmer new to the code, the `CheckSpecial` class is really awkward: it is not clear the purpose of the class in isolation and that its instances are never to be created and used alone.
Instead, in the last section, we intentionally use `__call__` method to make each CheckSpecial a stateful "callable".
In that way, the intention of the class is clearer: it is a stateful closure that is meant to be passed into the hook of another function (e.g., `sort`, `defaultdict`).

