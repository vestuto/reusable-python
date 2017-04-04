
# Shells

In this prelude, we review the concept of a shell and different shells relevant to working with python. This introduction takes some liberties with the use of the term for the benefit of the new learner.

One of the original motivations for developing python was that before it existed, many developers used shells such as Bash and compiled code such as C, together, yet found some limitations. 

Python was partly created span both use cases, and making it easier to write scripts and libraries, and easier to integrate the shell with compiled C code. So many of the "idioms" seen in python show the influence of both the shell and C.

# Table of Contents

* [Workflows](#Workflows)
	* [Working with a shell](#Working-with-a-shell)
	* [Working with a script](#Working-with-a-script)
* [What is a Shell?](#What-is-a-Shell?)
	* [Kernel](#Kernel)
	* [Shell](#Shell)
	* [Shells: CLI vs GUI](#Shells:-CLI-vs-GUI)
* [System Shells](#System-Shells)
	* [Windows](#Windows)
	* [Mac](#Mac)
	* [Linux](#Linux)
* [Python Shells](#Python-Shells)
	* [python shell (>>>)](#python-shell-%28>>>%29)
	* [IPython shell (In [1]:)](#IPython-shell-%28In-[1]:%29)
	* [IPython Notebook](#IPython-Notebook)
	* [Jupyter Notebook](#Jupyter-Notebook)
* [Portable Shell Interactions](#Portable-Shell-Interactions)
	* [Files and Paths](#Files-and-Paths)
	* [Exercise: Tree](#Exercise)
	* [Solution: Tree](#Solution)


# Workflows

One of the first steps in writing reusable python code is to get out of the interactive shell and start keeping your code in a file, ideally under version control!


## Working with a shell

* Working in the shell can be like using a calculator
* The work is not preserved after you turn off
* Reproducibility is unlikely

## Working with a script

* Write code in a file
* Execute the file from a shell
* Code is saved for reuse, automation, reproducibility
* Scripts can interact with the system shell in powerful ways

# What is a Shell?

The terms "shell" and "kernel" come from nuts or seeds and provide a nice metaphor: 

* e.g. pistachio nuts have an outer husk (shell) and edible center (kernel).

The phrases "kernel" and "shell" are used loosely in many contexts:

* operating systems: e.g. "the NT kernel inside the Windows shell"
* python: e.g. "the python3 kernel inside the python shell"
* Jupyter: e.g. "the IPython kernel inside the Jupyter shell"
* nuts: e.g. "pistachio kernel inside the pistachio shell"

Example: What are the kernel and shell in an operating system?

* Every operating system has some form of "shell" and "kernel"
* The kernel mediates interactions between the hardware (cpu, ram, hdd, keyboard, monitor) and the programs running
* The shell is how you interact with the kernel and running programs


> human > (keyboard,screen) > shell > kernel > (cpu,ram,hdd)

## Kernel

> "kernel is the lowest-level, or "inner-most" component of most operating systems."

> "kernel is a program that manages input/output requests from software, and translates them into instructions for the CPU"

> <https://en.wikipedia.org/wiki/Kernel_(operating_system)>

Example OS Kernels:

* Linux: FreeBSD
* OSX: XNU (2000-present), Darwin, Mach
* Windows: [MS-DOS (1981-2000)](https://en.wikipedia.org/wiki/MS-DOS), [9x kernel (1990-1999)](https://en.wikipedia.org/wiki/Architecture_of_Windows_9x), [NT kernel (2000-present)](https://en.wikipedia.org/wiki/Architecture_of_Windows_NT)

Example Language Kernels "inside" the Jupyter Notebook shell:

* Python
* R
* Julia
* MATLAB
* Javascript
* Ruby
* Perl
* Bash

## Shell

In context of operating systems:
> "A shell is a user interface for access to an operating system's services."
> <https://en.wikipedia.org/wiki/Shell_(computing)>

*Note: Common usage of the word, "shell" usually implies "CLI Shell", but...*


There are both "CLI" and "GUI" shells.

* CLI = Command Line Interface
* GUI = Graphical User Interface

Example CLI Shells:

* Linux/OSX/Posix: sh, bash, csh, tcsh, zsh
* Windows: DOS, Command Prompt

Example GUI Shells:

* Linux: Gnome, KDE, Xwindows
* OSX: Quartz, Aqua
* Windows: "Windows shell" (desktop environment, start menu, and task bar)

*Note: Herein, the system CLI shell "prompt" is assumed to be the character `$`, but yours may be different*

##  Shells: CLI vs GUI

Advantages of CLI shells:

* Often more efficient if you like to type
* Easy to script (reproducibility and automation)
* Easy to automate repetitive tasks
* Very efficient use of system resources
* Very efficient for remote connections, slow networks
* Often easier for the seeing impared

Advantages of GUI shells:

* Often more efficient if you hate to type
* Humans are really good at processing visual information
* Often easier for the mobility impared

# System Shells

Throughout the course, we'll be using your system shell, so let's take a moment to make sure you can launch it.

## Windows

The most commonly available (CLI) shell is `cmd.exe`, commonly called `Command Prompt`:

* Start Menu > Command Prompt
* Common path location to this program is `C:\Windows\System32\cmd.exe`

**Practice:** use your Windows system CLI shell to determine the location of python

```
where python3
```

**Practice:** Create a script to launch python:

* Create a new text file on desktop called `launch_ipython.txt`
* Enter the following text in the file:

```
ipython
```

* Rename the file to `launch_ipython.bat`
* double-click on the file to launch python

**Practice:** Create a script to launch the ipython notebook:

* Create a new text file on desktop called `launch_notebook.txt`
* Enter the following text in the file:

```
cd course_folder
jupyter notebook
```

* Rename the file to `launch_notebook.bat`
* double-click on the file to launch python

## Mac

OSX comes with the Terminal.app

* Use the Finder to launch `/Applications/Terminal.app`
* The terminal application is a shell for running various shells
* The default shell is `bash`

**Practice:** Add the Terminal app to your Dock

**Practice:** use your OSX system CLI shell (Terminal.app or iTerm.app) to determine the location of python

```
which python3
```

**Practice:** use your OSX system CLI shell (Terminal.app or iTerm.app) to determine the location of ipython

```
which ipython
```

**Practice:** Create a script to launch ipython:
* Create a new text file on your Desktop called `launch_ipython.txt`
* Enter the following text in the file:

```
ipython
```

* Rename the file to `launch_ipython.sh`
* use the terminal to change the file permissions

```bash
chmod a+x launch_ipython.sh
```

* in Finder, right-click your file and select "Open with" and then "Other...".
* switch from "Recommended Applications" to "All Applications".
* Select "Terminal" as the application to associate all ".sh" files.
* check "Always Open With"
* double-click on script to run it

## Linux

There are too many variants of Linux to provide specific directions:

* Most linux users use a terminal application or a shell daily
* Linux can boot straight into a CLI shell, usually bash
* When in the GUI shell, like Gnome, right-click on the desktop often provides a context menu with an item called "Terminal"

**Practice:**
Use any CLI shell to determine the location of the system install of python3

```
which python3
```

```
which ipython
```

# Python Shells

Python shells allow you to interact with a "python intepreter" which is often spoken of as a "python kernel".

There are both CLI and GUI shells for python:
* python (CLI)
* IPython (CLI)
* Jupyter notebook (GUI and CLI)

## python shell (>>>)


The CLI program called `python` is installed by default on almost all operating systems.


```python
# Where is the program "python" installed and what version is it?

import sys
print( sys.executable )
print( sys.exec_prefix )
!python --version
```

To launch the python shell from your system terminal/command-prompt:
```bash
$ python3
```

In the python shell:
```python
Python 3.4.3 |Anaconda 2.3.0 (x86_64)| (default, Mar  6 2015, 12:07:41)
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> print("Hello")
Hello

>>> 1 + 2
3
```

## IPython shell (In [1]:)

The CLI program called `ipython` is not installed by default, but comes with Anaconda. It has manay advantages over the regular `python` shell.

To launch the IPython shell from your system shell:
```bash
$ ipython
```

In the IPython shell:

```python
Python 3.4.3 |Anaconda 2.3.0 (x86_64)| (default, Mar  6 2015, 12:07:41)
Type "copyright", "credits" or "license" for more information.

IPython 3.2.1 -- An enhanced Interactive Python.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: print("Hello")
Hello

In [2]: 1 + 2
Out[2]: 3

In [3]:
```

## IPython Notebook

The IPython Notebook is an interactive GUI shell, that supports CLI shell commands, all providing a way to interact with the python kernel.

To launch the ipython notebook from your system shell:

```bash
ipython notebook
```

Then wait for the notebook interface to open as a webpage in your default web-browser. This web session is entirely contained on your local system. 

## Jupyter Notebook

Eventually, developers of the **"IPython Notebook"** added support for interactive with **other kernels**, not just the python kernel. Some of the first language kernels added were Julia and R. From those names, (Ju)lia, (Pyt)hon, (R). Thus, the project and the technology was **renamed "Jupyter"**, in part to emphasize that this interactive environment is no longer limited to just python.

Also, the developers were mostly scientists, many of whom have spoken to the **inspiration of Galileo**, the first modern physicist, and his notebooks which he used to document both calculations and visual observations of **the moons of Jupiter**.

# Portable Shell Interactions

When writing python that must interact with your operating system shell, use the python modules `os` and `sys` so that your python code is **portable**, i.e. reusable on other operating systems without change to your code.


## Files and Paths

One of the most common uses for a system shell, is to interact with files.

Python can interact with the system shell and files in a platform-independent way!


```python
# Useful for dealing with files and paths

import os
```


```python
# Check you platform name:
# What did you get?
#     'posix', 'nt', 'os2', 'ce', 'java', 'riscos'

os.name
```


```python
# The sys module gives finer granularity:
# What did you get?
#     'linux2','win32','cygwin','darwin','os2','riscos','atheos'

import sys

sys.platform
```


```python
# Here's the problem: system shell commands vary from system to system

if os.name is "posix" or sys.platform is "cygwin":
    !pwd
elif os.name is "nt":
    !chdir
else:
    print("Beep. Boop.")
```

The python module `os` provides **platform-independent** tools for handling files and paths


```python
# Get current working directory

cwd = os.getcwd()
print(cwd)
```


```python
dir_list = os.listdir(cwd)
dir_list[0:6]
```


```python
# Get absolute path

os.path.abspath('README')
```


```python
# Exists?

os.path.exists('README')
```


```python
os.path.isfile(cwd)
```


```python
os.path.isdir(cwd)
```


```python
# DEMO: Not important to understand all the syntax for now.
# Purpose: Show how to test for file, dir, not found.

data_file = os.path.join(cwd,'data','exoplanets.csv')

if os.path.isfile( data_file ):
    print( "IS FILE: " + data_file )
    file_found = True
elif os.path.isdir( data_file ):
    print( "IS DIR: " + data_file )
    file_found = True
else:
    print( "NOT FOUND: " + data_file )
    file_found = False
```


```python
# Demo: Explore your file tree with os.path.join and os.listdir

data_dir  = os.path.join(cwd,'data')
data_list = os.listdir( data_dir )
data_list[0:8]
```


```python
# Method 1: Create directory
if not os.path.exists('tmp'):
    os.mkdir('tmp')
```


```python
# Method 2: Better
if not os.path.exists('tmp'):
    os.makedirs('tmp')
```

## Exercise

Write a platform-independent directory tree list function.

```python
# Takes 2 inputs:
#     1. the top-level dir "root" to be inspected, default root="."
#     2. the number "levels" of levels to look down into, default: L=2
# Returns 0 outputs:
# Prints:
#    list of files and dirs with indention indicating dir tree level or "depth"
#        if L=1, the list returned will only include files and dirs in top-level
#        if L=2, return the contents of top level dir, 
#                plus the contents of any dirs in the top-level, 
#                and the contents of any dir below that.
# Example: if you have this on disk: /dir0/dir1/dir2/file3, 
#          then you would have to set L=3 to get file3 in the returned list
#
# Bonus: write this function using recursion, i.e. the function calls itself
```

## Solution

```python
# Solution 1: Functional Programming with Recursion 

import os

def tree(thing=os.getcwd(), indent="", level=2):
    print(indent + thing)
    if os.path.isdir(thing) and level > 0:
        level = level - 1
        indent = indent + "    "
        for item in os.listdir(thing):
            # if item[0] not in "._":
            tree(item, indent, level)
tree()
```


```python
# Solution 2: Cheating on Linux!
! tree -L 2
```



# Recap

* Shells and Kernels
* CLI vs GUI
* System shells
* Python shells
* Portable shell interactions
* Files and Paths, os and sys

