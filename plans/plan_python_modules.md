# Plan, Part 1: Python Modules


### What is a Module?

* most simple: file on disk, import or shell to use
* composed of data, functions, imports, i/o, etc
* building blocks to construct a package
* modules versus packages
* example: import math, math.pi, math.sqrt()

### Why Create Modules?

* why build a python module?
* organized: optimized for the human interpreter
* code reuse: structured and modular programming
* debugging and isolation/locating problems
* collaboration, division of labor
* project management, time estimation
* communication, structured thought structured code
* unit testing, units to test
* integration, well defined interfaces

### Roadmap

1. HOWTO build a module
2. shell to file, script as transitional
3. organize data into containers/classes
4. organize actions into functions/methods
5. organize scope/namespace, optional: `__name__` test

### Shell to File

* interactive shells = bash, python, ipython, jupyter
* from interactive shell history to file on disk
* the history() command
* workflow-1: type commands into terminal, dumb history later
* workflow-2: edit file, execute file from terminal

### Organizing Data

organizing script data into containers

* before you roll-your-own class, use built in stuff
* dicts, lists, ndarrays, dataframes
* tuples, namedtuples, import collections
* composition, lists of dicts, lists of tuples 
* functions to create containers, locals()

### Organizing Actions

organizing script actions into functions

* GNU philosophy: do one thing well, no more 
* refactoring for testing
* refactoring for dependencies
* input args
* return args
* scope and name-binding
* locals(), globals()

### Using a Module

* script-module duality: importing any file
* dunder name, dunder main, and arguments
* running your script
* importing your module
* imports, namespaces, and locals()
* WARNING! from pollution import *
* argparse

### Installing a Module

* not yet, we'll do that with packages
* start with a package composed of a single module
* then make a package out of several modules
