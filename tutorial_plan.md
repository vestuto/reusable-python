# Course Plan

The course is organized into 4 parts, with roughly one hour to be spent on each part, and that hour being composed of about...

* 20 minutes of instructor overview and demonstration
* 30 minutes of student exercises
* 10 minutes for other (e.g. questions, walking, stretching, coffee) 

### Part 1: Python Modules

* why build a python module?
* from terminal history to python script  
* organizing script data into containers
* organizing script actions into functions
* script-module duality: importing any file
* running your script vs importing your module
* imports, namespaces, and locals()
* dunder name, dunder main, and arguments

### Part 2: Python Packages

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

### Part 3: Using Conda

* why use conda?
* installing conda with Miniconda
* conda create environments
* conda install packages, with/without versions
* switching environments, source activate every time
* conda export, for sharing and reproducing
* pip install into a conda environment
* conda search for finding packages, available versions
* conda channels, local package installs

### Part 4: Conda Build ***(optional)***

*In the case that another proposal for a more advanced tutorial on conda-build is accepted, this present section on Conda Build could be optionally (1) removed with more emphasis spent on previous sections outlined above (2) kept minimal, limited to pure python packages.  The two proposed talks could then potentially serve as a "Part 1, Part 2" pairing, with the present one being "Part 1" which would introduce reusable code and the use of conda, and then "Part 2" in another tutorial covering conda-build and conda-forge in much greater detail at an advanced level.* 

* why build a conda package?
* conda package distributions, Anaconda
* write a conda recipe: meta.yaml, build.sh, bld.dat
* conda build a pure python package
* conda install your local conda package
* importing your conda installed package
* upload your conda recipe and package to conda-forge
