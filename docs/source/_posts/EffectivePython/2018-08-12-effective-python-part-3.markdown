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

Original problem.

* Intention and Expectation
* found is not True

Reason:

* Variable reference. Example.
* Variable assignment. Example.

Solution:

* In Python 3, nonlocal. Problem: it can be confusing if the variable is declared a couple of layers away.
* In Python 2, using array. It is a trick.
* In both Python versions and recommended way, use the helper class.
  * We have a state to keep track of it. It is better to keep it in an object and update the object accordingly.

