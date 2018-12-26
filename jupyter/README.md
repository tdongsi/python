### Summary

How to set up Jupyter with kernels for Python, R, Julia, and JavaScript scripting.

### Python setup

Python scripting is native in most Jupyter setup. 
However, for flexibility and reproducibility, we should use `virtualenv` when setting up Jupyter.

```
$ take jupyter
$ python3 -m venv venv3

$ . ./venv3/bin/activate

$ pip3 --version
pip 18.1 from /Users/tdongsi/Matrix/python/jupyter/venv3/lib/python3.7/site-packages/pip (python 3.7)
$ pip --version
pip 18.1 from /Users/tdongsi/Matrix/python/jupyter/venv3/lib/python3.7/site-packages/pip (python 3.7)

$ pip3 install jupyter
Collecting jupyter
  Downloading https://files.pythonhosted.org/packages/83/df/0f5dd132200728a86190397e1ea87cd76244e42d39ec5e88efd25b2abd7e/jupyter-1.0.0-py2.py3-none-any.whl

$ jupyter notebook
[I 02:23:51.216 NotebookApp] Writing notebook server cookie secret to /Users/tdongsi/Library/Jupyter/runtime/notebook_cookie_secret
[I 02:23:51.529 NotebookApp] Serving notebooks from local directory: /Users/tdongsi/Matrix/python/jupyter
[I 02:23:51.529 NotebookApp] The Jupyter Notebook is running at:
[I 02:23:51.529 NotebookApp] http://localhost:8888/?token=5605bab9f2b814062d2c06c6e22e3ebdc561b9d75ea6e655
...
```

In the same virtual environment, you can also install the most popular modules typically used with Jupyter, as follows.

```
$ pip install numpy scipy scikit-learn pandas matplotlib
Collecting numpy
...
```

### R setup

For R setup, [Anaconda](https://www.anaconda.com/download/) is recommended.
Anaconda is a package manager (similar to de facto Python package manager `pip`).
The difference is that Anaconda can install any software package (into some virtual env) while `pip` can only install **Python** packages.

NOTE: If you already set up your own Python envrionments, you might not want to add Anaconda installation into `PATH` envrionment variable and refer to its executables explicitly.

```
$ /anaconda3/bin/conda info --envs
# conda environments:
#
base                  *  /anaconda3
condaenv                 /anaconda3/envs/condaenv

$ source /anaconda3/bin/activate condaenv
(condaenv)

$ /anaconda3/bin/conda install -c r r-essentials
Solving environment: done

## Package Plan ##

  environment location: /anaconda3/envs/condaenv

  added / updated specs:
    - r
    - r-essentials
```

After R is installed into `conda` environment, you have to register [Jupyter's R kernel](https://github.com/IRkernel/IRkernel).

```
$ R

R version 3.5.1 (2018-07-02) -- "Feather Spray"
Copyright (C) 2018 The R Foundation for Statistical Computing
Platform: x86_64-apple-darwin13.4.0 (64-bit)

> install.packages('IRkernel')
--- Please select a CRAN mirror for use in this session ---
Secure CRAN mirrors
...

> IRkernel::installspec()
[InstallKernelSpec] Installed kernelspec ir in /Users/tdongsi/Library/Jupyter/kernels/ir
> q()
Save workspace image? [y/n/c]: n
(condaenv)
```

### Julia setup

Install Julia from [here](https://julialang.org/downloads/).
After installation, install the following packages.

```
$ julia

julia> using Pkg

julia> Pkg.add("IJulia”)

julia> Pkg.add("DataFrames”)

julia> Pkg.add("RDatasets”)

julia> Pkg.add("Gadfly”)

julia> quit();
```

### JavaScript setup

JavaScript support for Jupyter comes from `ijavascript` module.
Follow [its instruction](http://n-riesco.github.io/ijavascript/doc/install.md.html#macos) to install.

TIPS: Note that the build tool `node-gyp` (which is part of Node.js and is used to compile native modules) requires Python 2.
Therefore, you might want to run `npm install -g ijavascript` outside of `conda` environment (where `python` is usually linked to Python 3) to force `python` referring to Python 2.

To start a notebook that supports JavaScript scripting, use command `ijs` instead of typical `jupyter notebook`.

```
$ ijs
```

### Recap

To start a Jupyter notebook that supports Python/R/Julia/JavaScript scripting.

1. Activate conda environment (to have R/Julia setup)
2. Activate Python virtualenv (to have Python setup)
3. Run command `ijs` (to have Javascript setup)

```
$ source /anaconda3/bin/activate condaenv
(condaenv)

$ . ./venv3/bin/activate
(condaenv)

$ ijs
[I 23:18:04.324 NotebookApp] Serving notebooks from local directory: /Users/tdongsi/Matrix/python/jupyter
[I 23:18:04.324 NotebookApp] The Jupyter Notebook is running at:
[I 23:18:04.324 NotebookApp] http://localhost:8888/?token=46fx
```

To properly stop working on such a Jupyter notebook:

1. Ctrl+C to stop the current `ijs` process.
2. Deactivate Python virtualenv.
3. Deactivate conda environment.

```
$ ijs
...
^C[I 16:54:27.888 NotebookApp] interrupted
Serving notebooks from local directory: /Users/tdongsi/Matrix/python/jupyter
0 active kernels
The Jupyter Notebook is running at:
http://localhost:8888/?token=8c2f
Shutdown this notebook server (y/[n])? y
[C 16:54:29.523 NotebookApp] Shutdown confirmed
[I 16:54:29.524 NotebookApp] Shutting down 0 kernels
(condaenv)

# This executable is from Python virtualenv
$ deactivate
(condaenv)

$ source /anaconda3/bin/deactivate
```

### References

* CSV data file is downloaded from [here](https://catalog.data.gov/dataset?q=&sort=views_recent+desc&res_format=CSV).

