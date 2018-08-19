---
layout: post
title: "Effective Python Pt. 5: Concurrency and Parallelism"
date: 2018-08-18 16:24:30 -0700
comments: true
categories: 
---

This post corresponds to Lesson 4 "Using Classes" of ["Effective Python" course](https://www.safaribooksonline.com/videos/effective-python/9780134175249).

<!--more-->

### Item 23: Use subprocess to manage child processes

``` python Piping data from Python data to subprocess
# You can pipe data from Python program to subprocess
# In this way, you can call other programs to run in parallel with Python process.
# Run sub-processes on multiple CPUs.
def run_openssl(data):
    """A computing-intensive method, best for running separately on separate CPUs."""
    env = os.environ.copy()
    env['password'] = b'asdf'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc

procs = []
for _ in range(5):
    data = os.urandom(100)
    proc = run_openssl(data)
    procs.append(proc)

for proc in procs:
    out, _ = proc.communicate()
    print(out)
```

``` python Piping data from one subprocess to another
import os
```

``` python Subprocess timeout in Python 3
# Python 3 way
proc = subprocess.Popen(['sleep', '10'])
try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()

print('Exit status', proc.poll())
```
