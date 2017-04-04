# Reusable Packages

In this lesson, we'll see how to create, install, and distribute your own PYTHON packages, whether for use internally or in sharing with a broader, more open community.

An overview of creating and installing python packages serves to prepare for conda packages in two ways:
* a python package provides the basic ingredient needed to create a conda package
* the process of python package creation introduces concepts needed to understand conda packaging

---

## Table of Contents

* [Building a Python Package](#Building-a-Python-Package)
	* [Creating a python module](#Creating-a-python-module)
	* [Creating a python package](#Creating-a-python-package)
* [Installing a Python Package](#Installing-a-Python-Package)
	* [2-Step Install](#2-Step-Install)
		* [Step 1: Create a `setup.py` file](#Step-1:-Create-a-setup.py-file)
		* [Step 2: Execute the setup.py install command](#Step-2:-Execute-the-setup.py-install-command)
	* [Install Paths](#Install-Paths)
	* [Uninstalling Python Packages](#Uninstalling-Python-Packages)


# Building a Python Package


## Creating a python module

Below is an example of a simple python module called `constants.py`.

```bash
print("Welcome to the constants.py module")

import math

E = 2.71828
PI = 3.14159

def compute_pi():
    return 4.0*math.atan(1.0)
    
def compute_e():
    sum = 0
    for n in range(10):
        sum += 1/math.factorial(n)
    return sum

def print_const(x):
    print("The value of your constant is ", x)
    return None

```

---

<div class='alert alert-success'>
<br>
<big>Exercise: Create a python module<br><br></big>
Using your favorite text editor, create a new file `constants.py` within the `Conda` lesson directory, and paste the python code above into the file.
</div>

---

This module contains a print statement, one import, two "data attributes", `E` and `PI`, and three functions, `compute_pi()`, `compute_e()`, and `print_const()`.

This module is **executable** from the system shell.

```bash
cd Conda
python constants.py
```

This module is also **executable** from the python shell; it is not "compiled" before it is used.

```bash
cd Conda
python
```

```python
>>> exec( open("constants.py").read() )
```

---

<div class='alert alert-success'>
<br>
<big>Exercise: Execute the module as a script<br><br></big>
Instead of the python shell, execute the `constants.py` module using the IPython shell, using the `%run` magic followed by the file name.
</div>

From the python shell one can import this file as a python module, and thus access its attributes and call its functions:

```bash
cd Conda
python
```

```python
>>> import constants
>>> constants.PI
3.14
>>> constants.compute_pi()
3.1415926535897931
```

---

<div class='alert alert-success'>
<br>
<big>Exercise: Import the module<br><br></big>
Using the IPython shell, launched either from the Jupyter home tab or your system shell, import the constants file as a module. Test the import by calling the `constants.compute_e()` method.
</div>

---

## Creating a python package

In python, building a large library of reusable code starts with organizing your code into modules, which are then further organized into a python package.

A python package is a collection of 

* one or more python modules (like `constants.py`)
* a build/install file called `setup.py`
* other optional and customary "meta-data files" like `README.txt`

These are organized into a particular directory structure. An example of a very simple python package is given below:

```bash
Desktop/
    my_package/
        constants.py
        setup.py
        README.txt
        LICENSE.txt
```

---

<div class='alert alert-success'>
<br>
<big>Exercise: Create a python package<br><br></big>
Create the file tree shown above. Use the previously created constants.py. Create but otherwise leave all other files empty for now.
</div>

---

<div class='alert alert-success'>
<br>
<big>Exercise: Create a `setup.py` file<br><br></big>
Edit the empty `setup.py` file and paste into it the code shown below.
</div>

```python
from setuptools import setup
setup( name='constants', 
       version='0.0.1', 
       py_modules=['constants',], 
     )
```

---

<br>
<big>Exercise: Add meta-data to your python package<br><br></big>
Edit the `README.txt` and `LICENSE.txt` files. For the `README`, add a brief description of `constants.py`. For the `LICENSE` file, add the following text within it:


> *Licensees may copy, distribute, display and perform the work and make derivative works and remixes based on it only if they give the author or licensor the credits (attribution) in the manner specified by these.*

---

# Installing a Python Package

The complete details of the process by which a python package is installed are beyond the scope of this present lesson. But the basics are simple: the contents of the `my_package` directory are in essense copied into a directory whose location will be known to any instance of the python interpreter you launch on your computer.

## 2-Step Install

The most common method for safely and reproducibly installing a python package are outlined as follows:

### Step 1: Create a `setup.py` file

```python
from setuptools import setup
setup( name='constants',
       version='0.0.1',
       py_modules=['constants',], 
     )
```

### Step 2: Execute the setup.py install command

```bash
python setup.py install
```

or

```bash
pip install .
```

...not yet!

For a software package that includes compiled source code, like a python "extension" package or a C library, your "build" process would include an actual compilation step, possibly involving a Makefile (Linux), CMake file (Linux, Mac, Windows), or a VS Project file (Windows).

---

<div class='alert alert-success'>
<br>
<big>Exercise: Make a more complete `setup.py`<br><br></big>
Edit your `setup.py` file so that it reads as shown below:
</div>

Here is a more complete `setup.py` example:

```python
from setuptools import setup
setup(
    name='constants',
    version='0.0.1',
    license='CC BY-NC-SA 4.0',
    long_description=open('README.txt').read(),
    py_modules=['constants',],
    )
```

---

<br>
<big>Exercise: Update your LICENCE.txt file<br><br></big>
Search online for the license called "CC BY-NC-SA 4.0" to discover what it is if you have not heard of it. Replace all text within your `LICENSE.txt` with that of the "CC" license found online.

Review the following description of Creative Commons as well: [`https://en.wikipedia.org/wiki/Creative_Commons_license`](https://en.wikipedia.org/wiki/Creative_Commons_license)

---

<div class='alert alert-success'>
<br>
<big>Exercise: Use `setup.py` to install the package<br><br></big>
Execute the `python setup.py install` command. Then test the install by moving to `Desktop`, launching a new python interpreter, and trying to `import constants`:
</div>

```
cd Desktop
python
```

```python
>>> import constants
Welcome to the constants.py module!
>>> constants.PI
3.14159
>>> constants.compute_pi()
3.1415926535897931
```

---

## Install Paths

How does the python `import` know where to find where the package was installed?

This is done through the `sys.path` directory list:

```python
>>> import sys
>>> sys.path
```

This `sys.path` is analogous to the system `PATH` variable. 

It is the list of directories on your file system wherein python will search for python modules or python packages when you try to `import` them.

When you installed your python package, its files will be located within one of the directories listed in `sys.path`. 

*Note: It is best to never try to copy files manually into any of the directories listed in `sys.path` as it is very easy to break something in the process, and it is very hard to reproduce the results even when successful.*

---

<div class='alert alert-success'>
<br>
<big>Exercise: View path order in `sys.path`<br><br></big>
Inspect the file path search order in `sys.path` by running the folling commands from the python shell:
</div>

```bash
python
```

```python
>>> import sys
>>> sys.path
```

---

<div class='alert alert-success'>
<br>
<big>Exercise: View python package install paths<br><br></big>
Compare the `sys.path` file paths to those of the python package `site`, execute the following commands from within your python interpreter:
</div>

```bash
python
```

```python
>>> import site
>>> site.USER_SITE

/Users/juser/.local/lib/python3.5/site-packages

>>> site.USER_BASE

/Users/juser/.local

>>> site.PREFIXES

/Users/juser/anaconda

```

## Uninstalling Python Packages

This is where things get painful. There is no `python setup.py uninstall`. You must find and manually delete all the installed files.

One helpful tool is to store the names of all the files at the time of install:

```
python setup.py install --record installed_files.txt
```

Contents of `installed_files.txt`
```
/Users/juser/anaconda/lib/python3.5/site-packages/constants-0.0.1-py3.5.egg
```

<br>
<big><big><b>Python package left-overs</b></big></big>

*It's even a bit more involved than that. Inspect the contents of the directory where the setup.py file lives, and you'll find many other intermediate file artifacts left-over from the build and install process.*

<br>
<big><big><b>The `.egg` file format</b></big></big>

*The `.egg` file is a distribution format for Python packages. It’s just an alternative to a source code distribution or an executable binary. For pure Python, the `.egg` file is completely cross-platform. The `.egg` file itself is like a `.zip` file. It contains source code, and meta-data, and other resources.*

<div class='alert alert-success'>
<br>
<big>Exercise: Manually remove the install file<br><br></big>
Uninstall the package by manually deleting the file listed in `installed_files.txt`. Test this "uninstall" by then launching a python shell and trying to import the package as `import constants`.
</div>



# Recap

In this lesson we saw....

* Building a Python module
* Building a Python package

---
