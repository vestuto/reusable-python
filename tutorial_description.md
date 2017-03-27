# Tutorial Proposal

## Course Title: 

"Introduction to Reusable Python"

A tutorial on how to organize and distribute python code in reusable units, including building packages and using conda.

## Course Abstract:

How to organize your python code into reusable units such as containers, functions, modules, and packages; and then with the use of pip and conda, how to share it locally and globally, so that it can be reused by others.

## Instructor Biography

### Public Biography

**Jason Vestuto** is a scientist and python developer working with the Space and Geophysics Laboratory at the University of Texas in Austin. He uses the scientific python stack daily to develop software tools and perform analysis of GNSS data. He holds degrees in both physics and science education. He has taught science, math, and coding at high schools, colleges, universities, and has trained scientific python and conda at large private companies and national science labs. 

## Prerequisite Skills:

### Summary List

Prerequisite Skills:

* Basic computer use
* Basic text editor use
* Basic to Intermediate terminal/command-prompt use
* Basic python use

### Detailed List

* Basic computer use:  
    * find and launch applications
    * turn on and off WIFI
    * use a web browser to download files
    * access to a user account
    * ability to write files to user home paths
    * ability to run installer files as the same user
    * test by downloading and installing Chrome to your laptop
* Basic text editor use: 
    * locate and open a text editor, e.g. [sublime text](https://www.sublimetext.com)
    * use a text edit to create, modify, and save files to known locations 
* Basic to Intermediate terminal use:
    * any: Linux, Mac, or Windows
    * open a terminal or command-prompt
    * use a terminal to list current working directory
    * use a terminal to list contents of a directory 
    * use a terminal to change current directory
    * use a terminal to execute/run a script
    * use a terminal to change file permissions
* Basic python use:
    * assign a value to a variable name
    * call a function, passing input parameters, storing return values
    * define a simple function using def and return
    * create a dictionary, and inspect its contents

## Attendee Preparation

Before the tutorial you should...

* download and install the trial version of text editor [sublime text](https://www.sublimetext.com/3)
* download an [Anaconda3 installer file](https://www.continuum.io/downloads) for your system.
* [Install Anaconda](https://docs.continuum.io/anaconda/install) under your user account home directory
* download [Miniconda3 installer file](https://conda.io/miniconda.html) for Python3 (~25 MB)
* Do NOT install Miniconda before class
* We will install Miniconda to a custom/secondary directory as a student exercise in class, so ***ALL*** students need the installer file, even those that already have e.g. Anaconda/Miniconda installed. I will provide uninstall instructions as part of the course material
* We will also create conda environments as a student exercise, so no need to do so before hand.
* download ZIP or clone "scipy2017-tutorial" project content from [github.com/vestuto/reusable-python](github.com/vestuto/reusable-python), to be updated prior to the class.


## Intended Audience

Intermediate 

*If you are a beginner in python, but very comfortable with use of the terminal (Linux or Mac) or command prompt (Windows), you are encouraged to attend.*


## Course Description

This tutorial introduces the basics of organizing and sharing your python code for reuse through a series of student exercises that build on each other. 

We start with code written in a python terminal, turn it into a module to import, use that as part of creating a python package, installing it with pip and conda, create a conda package, and finally uploaded the packages to PyPI and conda-forge.

This tutorial is intentionally limited to only the core aspects of python scope, packaging, pip, and conda that best illustrate the most import concepts and machinery needed to get you started using and contributing to the shard ecosystem of reusable scientific python tools from which we all benefit.