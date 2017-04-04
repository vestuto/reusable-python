# Introduction to Conda

**Open-source, cross-platform, package and environment management, for any language**


> **NumFOCUS says:** *"Conda is an [open source](https://github.com/conda/conda) package management system and environment management system for installing multiple versions of software packages and their dependencies and switching easily between them. It works on Linux, OS X and Windows, and was created for Python programs but can package and distribute any software."*


# The Plan

1. Who should care about conda?
2. What is the problem?
3. What are the other solutions?
4. What is conda?


# The Users

* **Computational Scientist** (numerical science, modeling)
* **Data Analyst** (ETL, EDA, data viz, comp stats, machine learning)
* **Developer** (re-usable code, testable, reproduceable results)
* **SysAdmin/DevOps** (install, config, audit, test, security)


# The User Stories

1. get started using Python for data analysis.
2. experiment with pkgs ***without affecting system*** installs.
3. run ***others' code*** with ***different versions, dependencies***.
4. ***test against multiple versions*** for portability testing.
5. run pre-deployment testing, ***before using it in production***.
6. reproduce old analysis env for regression/migration testing.


# Example User Story: The User

* You are a data analyst with e.g. strong skills in statistics and domain knowledge.
* want to give up proprietary solution. 
* need a quick way to set-up a scientific python stack.
* want an extensible ecosystem, reuse community code.
* need reproducible envs to rerun old analyses, reproduce results, regression test code in new envs.
* need the ability to switch between multiple versions, to collaborate with others.


# Example User Story: The Tools

You may need to build from source and install:

* python interpreter (IPython)
* vectorized array library (numpy, xarray)
* data store and file I/O library (h5py, pytables, netcdf4)
* visualization library (matplotlib, seaborn, bokeh)
* math, statistics library (scipy, statsmodels, scikit-learn)
* maybe mapping/GIS library (bokeh-geo, datashader)
* maybe an IDE (spyder, jupyter)
* a compiler tool-chain, or two (gcc, g++, gfortran, ifort, absoft, make, auto-conf, CMake, python, perl, bash)


# The Problem

### Open-Source Stacks are Hard to Manage

* **fragmentation:** open-source ecosystems are composed of many independent projects developing in parallel
* **dependencies:** some packages depend on libraries written in MANY languages (e.g. numpy and LAPACK/MKL)
* **versions:** Thing1 and Thing2 depend on incompatible versions of Thing3; dependency graph hell, collaboration hell
* **build:** maintaining/updating compiler tool-chains probably not the best use of a data analyst
* **install:** maintaining/updating an install process probably not the best use of a data analyst


# The Solutions

### Mileage may vary...

1. DIY
2. platform-specific package managers
3. pip+virtualenv
4. conda


# The Solutions: DIY

Do It Yourself: Build Everything from Source, Cross Fingers, then Link!

* total control! Mwahahaha.
* build everything yourself from source
* maintain build and install toolchains/frameworks
* manually solve "dependency hell", aka "trial-and-error"
* universe: "Oh, you needed that stack for another version/platform? LOL, start over!"


# The Solutions: platform-specific

Platform-specific package managers

* linux: apt, yum
* osx: macports, homebrew
* win: virtualbox? (gratuitous recursion joke?)
* VMs: `GOTO 2` (cf. bad joke: sure, why not?)
* not good if you need cross-platform consistency


# The Solutions: python-specific

### pip+virtualenv

* pip installs python packages within any environment
* does not precisely track non-python dependencies well
* great if you have an existing system Python installation and you want to install packages in or on it.
* not so great for multi-language dependency management and cross-platform binary installations.

# The Solutions: Conda

* Features
* Conda is not Anaconda
* Environment Manager
* Package Manager
* Package Builder
* Package Distributor
* Documentation


# Conda Features

* does both: a tool to manage packages and environments
* multi-language: any language, many languages
* cross-platform: "OS-agnostic", Linux, OSX, Windows
* open-source: github.com, BSD License, source is python
* supported: Continuum Analytics, NumFOCUS, conda-forge
* adopted: most of the SciPy/PyData communities
* multi-channel: can install pkgs from many "channels"
* works offline: package repo can be local, use file URL
* roll-your-own: building your own conda pkgs from source
* package-anything: not just for source, can pkg/version data


# Conda is Not Anaconda

**Conda is not Anaconda** 

* Conda is an open-source tool for creating and managing packages and environments. 
* Anaconda is a distribution of conda packages.
* Conda is a conda pkg included in the Anaconda distribution.

**Conda Myths**

* google search `"conda myths"`
* read the first hit: [https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/)

# Conda as Environment Manager

* Conda environments contain a collection of conda or pip packages
* Conda envs isolated from system installs, other user installs
* You can have many envs, each with different versions
* Modify one env, other envs NOT affected. 
* Easily switch between environments
* Share/document/recreate your envs with `export` cmd

# Conda as Package Manager

* Command line tool (CLI vs GUI) as primary interface
* Query and search the package index and user installation 
* Add, update, and remove packages from Conda environments
* Installs pkgs under user home path (default), no admin needed
* Installs and updates packages and their dependencies
* You tell conda the high level package names you want
* Conda solves dependency problem for mutual compatibility

# Conda Package Distribution

* [repo.continuum.io](https://repo.continuum.io/pkgs/) is a large repository of conda packages, curated and distributed by [Continuum Analytics](https://www.continuum.io/), used as the default channel for installs and updates by all conda distributions.
* [Anaconda](https://docs.continuum.io/anaconda/) is a complete conda package distribution for science, with hundreds of python packages for science.
* [MiniConda](http://conda.pydata.org/docs/install/quick.html) is a minimum conda package distribution, with about 10 packages.
* [conda-forge](https://conda-forge.github.io) is a "community led collection of recipes, build infrastructure and distributions for the conda package manager."


# Conda Documentation

For more on using conda see the following resources:

* [Conda Myths, Comparison with Pip](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/)
* [Conda documentation](http://conda.pydata.org/docs/index.html)
* [Admin Configurations](http://conda.pydata.org/docs/install/central.html)
* [Advanced Conda Configurations](https://www.continuum.io/blog/developer/advanced-features-conda-part-1)