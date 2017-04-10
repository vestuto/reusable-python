# Course Plan

### Overview

The course is organized into 4 main parts, plus 2 optional parts, with roughly one hour to be spent on each part, and that hour being composed of about...

* 20 minutes of instructor overview and demonstration
* 30 minutes of student exercises
* 10 minutes for other (e.g. questions, walking, stretching, coffee) 

### Required Parts

Parts 

### Optional Parts

These are included to allow for flexibility given possible overlap with other tutorials and possible variation in student abilities and prior knowledge.

* Shells and Scripts: This material can be read before class to allow the potential student to self-assess whether they are ready, or to ramp up in preparation.
* Conda Build: In the case that another proposal for a more advanced tutorial on conda-build is accepted, this present section on Conda Build could be optionally
    1. removed with more emphasis spent on previous sections outlined above
    2. kept minimal, limited to pure python packages.
* Conda Build: The two proposed talks could then potentially serve as a "Part 1, Part 2" pairing, with the present one being "Part 1" which would introduce reusable code and the use of conda, and then "Part 2" in another tutorial covering conda-build and conda-forge in much greater detail at an advanced level.
* Conda Channels: as time permits

# Course Parts

### Part 0: Shells and Scripts

***Remediation material to read and practice before class***

* introduction to system shells and python shells
* writing and running simple python scripts
* from terminal history to python script, with `save` and `load`
* simple command line interfaces (CLI) for python scripts using `sys.argv` and `argparse`
* OS-independent system interactions for python script using `os` and `sys` modules


### Part 1: Writing Python Modules

* why build a python module? reuse and composition
* script-module duality: importing any file
* imports and name-space pollution
* organizing script data into containers
* organizing script actions into functions
* running your script vs importing your module
* imports, namespaces, and locals()
* dunder name, dunder main,
* names with underscores and consnesual privacy

### Part 2: Building Python Packages

* why build and install a python package?
* writing a simple setup.py
* installing your module with setup.py
* importing, using your installed module
* sys.path, PYTHONPATH, PATH
* composing a package: modules, dirs, and init files
* installing a python package with setup.py and pip
* importing, using your installed python package
* upload your package to PyPI
* what is pip?

### Part 3: Using Conda Environments

* why use conda?
* installing conda with Miniconda
* conda create environments
* conda install packages, with/without versions
* switching environments, source activate every time
* conda export, for sharing and reproducing
* pip install into a conda environment
* conda search for finding packages, available versions
* conda channels, local package installs

### Part 4: Building Conda Packages

* why build a conda package?
* conda package distributions, Anaconda
* write a conda recipe: meta.yaml, build.sh, bld.dat
* conda build a pure python package
* conda install your local conda package
* importing your conda installed package
* upload your conda recipe and package to conda-forge


### Part 5: Channeling Conda Packages

* why create or use a conda channel?
* package distribution locally and globally
* what is a conda channel?
* how to configure conda to use differnet channels
* how to build an internal channel to host packages
* how to HTTP serve a local/custom channel
* how to upload packages to a local or remote channel 
