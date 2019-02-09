---
layout: post
title: "Effective Python Pt. 4: Using Classes"
date: 2018-08-12 00:19:36 -0700
comments: true
categories: 
- Book
- Python
---

This post corresponds to Lesson 4 "Using Classes" of ["Effective Python" course](https://www.safaribooksonline.com/videos/effective-python/9780134175249).

<!--more-->

### Item 19: Prefer helper classes over book-keeping with dict and tuples

In an example, the author illustrated the progressive evolution of a grade-book application.
In each iteration, the requirements are changed and interfaces are changed to accomodate that.
Consequently, dictionaries and tuples are added to accomodate those changes in implementation but the logic and code becomes so convoluting with all book-keeping with those built-int data structures.
The final version is shown as follows:

``` python Original code with dicts and tuples
class WeightedGradebook(object):
    """
    Change WeightedGradebook to make the score in each subject is weighted.
    For example, final is more weighted than homework.
    """

    def __init__(self):
        self._grade = {}

    def add_student(self, name):
        self._grade[name] = {}

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grade[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grade[name]
        total, count = 0.0, 0

        for grades in by_subject.values():
            subject_total, subject_weight = 0.0, 0
            for score, weight in grades:
                subject_total = score * weight
                subject_weight = weight

            total += subject_total / subject_weight
            count += 1

        return total / count


def main_weighted():
    book = WeightedGradebook()
    book.add_student('Isaac')

    book.report_grade('Isaac', 'Math', 90, 0.90)
    book.report_grade('Isaac', 'Math', 85, 0.10)
    book.report_grade('Isaac', 'Gym', 95, 0.20)
    book.report_grade('Isaac', 'Gym', 80, 0.20)

    print(book.average_grade('Isaac'))
```

As you can see, the `average_grade` internal implementation is really complicated and hard to understand because of the nested dictionaries.
Externally, the class is not easy to use for clients with four positional arguments: it is easy to mix up the order of arguments, such as weight `0.90` with score `90`.

In those cases, it is recommended to unpack dictionaries into separate classes.
Tuples can be unpack into simple classes using `namedtuples` from `collections` module.
The line count may be much larger but it is worth it because 1) internally, implementation can be much easier to understand 2) externally, interface can be easier to use.

``` python Use helper classes
class Score(object):
    """Weighted score."""

    def __init__(self, score, weight):
        self.score = score
        self.weight = weight

    def weighted_score(self):
        return self.score * self.weight


class Subject(object):
    """Keeping track of weighted scores for a subject"""

    def __init__(self):
        self._grades = []

    def add_score(self, score, weight):
        self._grades.append(Score(score, weight))

    def average_score(self):
        total = sum(e.weighted_score() for e in self._grades)
        weight = sum(e.weight for e in self._grades)
        return total / weight


class Student(object):
    """Keeping track of subjects for a student"""

    def __init__(self):
        self._subjects = defaultdict(Subject)

    def subject(self, name):
        return self._subjects[name]

    def average_grade(self):
        """ Average grade over all subjects"""
        count = len(self._subjects)
        total = sum(e.average_score() for e in self._subjects.values())
        return total / count


class ClassGradebook(object):
    """
    Change WeightedGradebook to make the score in each subject is weighted.
    For example, final is more weighted than homework.
    """

    def __init__(self):
        self._book = defaultdict(Student)

    def student(self, name):
        return self._book[name]

    def report_grade(self, name, subject, score, weight):
        student = self._book[name]
        student.subject(subject).add_score(score, weight)

    def average_grade(self, name):
        student = self._book[name]
        return student.average_grade()

def main_class_2():
    """Helper classes help easier-to-use interface"""
    book = ClassGradebook()

    isaac = book.student('Isaac')
    math = isaac.subject('Math')
    math.add_score(90, 0.90)
    math.add_score(85, 0.10)
    gym = isaac.subject('Gym')
    gym.add_score(95, 0.20)
    gym.add_score(80, 0.20)

    print(isaac.average_grade())
    # Equivalent to the old interface
    print(book.average_grade('Isaac'))
```

### Item 20: Use plain attributes instead of getter and setter methods

For people migrating to Python from Java, they tend to explicit create getter and setter methods for every single attribute in the class.
In Python, it is not recommended and plain attributes should be directly used.

The reason that most people use setters and getters in Java is that in case of changes required for getting or setting an attribute, they can do it easily in corresponding setter or getter method.
In Python, such cases are covered in `@property` and `@setter` decorators.

For example, we have the following simple class:

``` python Simple class
class Resistor(object):

    def __init__(self, ohms):
        self.ohms = ohms

def main():
    res = Resistor(1e3)
    print(res.ohms)
    res.ohms += 2e3
    print(res.ohms)
```

Let's say at some point, we decide that we need special behaviors in getting and setting attribute `ohms` of Resistor objects.
In that case, we can easily add special behaviors (for example, printing message) as follows:

``` python Getter and setter with special behaviors
class Resistor(object):

    def __init__(self, ohms):
        self._ohms = ohms

    @property
    def ohms(self):
        print('Getter')
        return self._ohms

    @ohms.setter
    def ohms(self, value):
        print('Setter')
        self._ohms = value
```

The same `main()` method above will now have the following output:

``` plain Before and after output
# Before
1000.0
3000.0

# After
Getter
1000.0
Getter
Setter
Getter
3000.0
```

Note that such setter is also effective when the attribute is set in parent constructor, as shown in example below.
This ensures that any validation check in `setter` method for the attribute is also active at initialization of that object.

``` python Setter activated in parent constructor
class Resistor(object):

    def __init__(self, ohms):
        self.ohms = ohms


class LoudResistor(Resistor):

    def __init__(self, ohms):
        super(LoudResistor, self).__init__(ohms)

    @property
    def ohms(self):
        print('Getter')
        return self._ohms

    @ohms.setter
    def ohms(self, value):
        print('Check value')
        self._ohms = value

def main():
    # This will print "Check value"
    # Setter in subclass LoudResistor is activated 
    # although "ohms" attribute is set in superclass Resistor
    res2 = LoudResistor(1e3)
```

Tips:

* Do not modify internal states/attributes or any side effect in getter methods. Only change object's state in setter methods.
* Getter method should be fast. Avoid doing complex computations in getter methods.
* You can use `setter` to create unmodifiable objects in Python. See [here](https://github.com/tdongsi/effective_python).

### Item 21: Prefer internal attributes over private ones

In Python, there are only two types of attribute: public (e.g., `my_att`) and private attributes (e.g., `__my_att`).
In reality, there is no tight access control like other languages such as Jaza.
The private attribute names are prefixed with the class name (e.g., `_MyClass__my_att`) to create another "namespace" for private attributes.
This will complicate accessing the private attributes in the subclasses while not effectively preventing anyone from accessing the private attributes when the need arises.
In general, it is better to use protected/"internal" attributes `_my_att` with the assumption that someone can extend usage of those internal attributes later on.

The scenario where you should use private attributes is when you want to avoid accidental name clash in the subclass.

``` python Scenario for using private attribute
class ApiClass(object):

    def __init__(self):
        self._value = 5

    def get(self):
        return self._value


class Child(ApiClass):

    def __init__(self):
        super(Child, self).__init__()

        # Here, Child class author is not aware of
        # internal implementation of ApiClass
        # he accidentally override an internal attribute of ApiClass
        self._value = 'hello'

a = Child()
print(a.get())
```

In this case, `_value` in ApiClass should be a private attribute.


### Item 22: Use `@classmethod` polymorphism to construct objects generically

In other languages such as Java, you can have overloaded constructors to construct objects of the same class/interface in different ways.
However, in Python, the method `__init__` can't be overloaded.
Instead, you can use `@classmethod` polymorphism to construct objects generically.

``` python Example of @classmethod polymorphism
import os
from threading import Thread


class InputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(InputData):

    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'rb') as handle:
            return handle.read()

    @classmethod
    def generate_inputs(cls, config):
        """ Generic version of generate_inputs"""
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


def generate_inputs(data_dir):
    """ Original version of generate_inputs"""
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        """ Generic version of create_worker.

        :param input_class: class that implements InputData interface.
        :param config: dictionary of configs to be used by InputData.
        :return:
        """
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


def create_worker(input_list):
    """ Original version of create_worker"""
    workers = []
    for input_data in input_list:
        workers.append(LineCounter(input_data))
    return workers


class LineCounter(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count(b'\n')
        pass

    def reduce(self, other):
        self.result += other.result
        pass


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    first, rest = workers[0], workers[1:]
    for other in rest:
        first.reduce(other)
    return first.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_worker(inputs)
    return execute(workers)


def mapreduce_generic(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


import random
from backports.tempfile import TemporaryDirectory


def write_test_files(temp_dir):
    for i in range(100):
        with open(os.path.join(temp_dir, str(i)), 'w') as handle:
            handle.write('\n' * random.randint(0, 100))


with TemporaryDirectory() as temp_dir:
    write_test_files(temp_dir)
    # line_count = mapreduce(temp_dir)

    config = {'data_dir': temp_dir}
    line_count = mapreduce_generic(LineCounter, PathInputData, config)
    print line_count

```
