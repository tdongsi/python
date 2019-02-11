---
layout: post
title: "Effective Python Pt. 5: Concurrency and Parallelism"
date: 2018-08-18 16:24:30 -0700
comments: true
categories: 
- Book
- Python
---

This post corresponds to Lesson 5 "Concurrency and Parallelism" of ["Effective Python" course](https://www.safaribooksonline.com/videos/effective-python/9780134175249).

<!--more-->

### Item 23: Use subprocess to manage child processes

``` python Typical usage of subprocess module
import subprocess

proc = subprocess.Popen(
    ['echo', 'Hello World'],
    stdout=subprocess.PIPE
)
out, err = proc.communicate()
print(out.decode('utf-8'))
```

``` python Simple forking example
proc = subprocess.Popen(['sleep', '0.3'])
while proc.poll() is None:
    print('Working...')
    # Time consuming process
    time.sleep(0.2)

print('Exit status: %d' % proc.poll())
```

In the forking example above, note that `proce.poll()` is used to check for and obtain the status of the child process.

``` python Parallelism wtih subprocess
def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc


start = time.time()
procs = []
for _ in range(10):
    proc = run_sleep(0.3)
    procs.append(proc)

for proc in procs:
    proc.communicate()

end = time.time()
print('Takes %f seconds' % (end - start))
```

In the parallisim example above, the time it takes is approximately 0.3 seconds, no matter how many processes you create.

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

Note that in this piping example above, you can use `os.environ.copy` to shield current process's environment from modifications of its variables.
You can use the new copy of environment by specifying `env=my_env` in `Popen` constructor. 
In addition, you can use the environment variable as parameters in the `Popen` command by using `env:password`.
To pipe data from Python into the subprocess, you need to set `stdin=subprocess.PIPE` and transfer data by using `proc.stdin.write(data)`.

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

It's not available in Python 2, and if you want to reproduce its functionality in Python 2, you actually have to use the `select` module and poll the input and output file descriptors of the subprocess. 
It is a little bit more complicated and it's hard to get right.

``` python Stop-gap alternative in Python 2
class Command(object):
    """ Stop-gap alternative for subprocess's timeout in Python 3.
    Based on https://stackoverflow.com/questions/1191374/using-module-subprocess-with-timeout
    """

    def __init__(self, process):
        self.process = process

    def run(self, timeout):
        def target():
            self.process.communicate()

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            print 'Terminating process'
            self.process.terminate()
            thread.join()

        print(self.process.returncode)

proc = subprocess.Popen(['sleep', '2'])
command = Command(proc)
command.run(timeout=3)

# NOTE: the following will not work since the subprocess already ran.
# command = Command(proc)
command = Command(subprocess.Popen(['sleep', '2']))
command.run(timeout=1)
```

### Item 24: Use threads for blocking I/O, NOT for parallelism

Python has the GIL, or Global Interpreter Lock. 
It means that only one Python thread will ever actually run at a time. 
A common mistake is to use threads to speed up a computation-intensive program in Python.
You will be usually disappointed and end up with similar, if not worse, performance.
In other words, you might find that your complicated parallel version will have similar performance as the serial one.

In Python, threads are good for two main use cases. 
The first use case is, if you want something looks running simultaneously (concurrency).
A common example is to respond to user inputs while doing network I/O.
In this case, the threads will cooperate with each other to obtain GIL fairly.
The second use case for threads in Python is for IO-intensive applications such as those with lots of (blocking) network, system calls.
A common example is to use threads to query multiple REST endpoints concurrently.
The following example illustrate such use case:

``` python Use Python threads for network I/O
import threading
import requests
import time

def get_response(url):
    r = requests.get(url)
    return r.status_code, r.text

class RequestThread(threading.Thread):

    def __init__(self, url):
        super(RequestThread, self).__init__()
        self._url = url

    def run(self):
        self.output = get_response(self._url)

urls = ['https://www.google.com',
        'https://www.facebook.com',
        'https://www.apple.com',
        'https://www.netflix.com',
        'https://www.salesforce.com',
        'https://www.intuit.com',
        'https://www.amazon.com',
        'https://www.uber.com',
        'https://www.lyft.com']

threads = []
for url in urls:
    thread = RequestThread(url)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
```

TODO: Explain GIL and under the cover, `request` release the control of GIL.

TODO: mistake

TODO: Note about how to call constructor.
