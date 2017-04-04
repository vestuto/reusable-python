# Plan, Part 3: Conda

## Topics

* why use conda?
* installing conda with Miniconda
* conda create environments
* conda install packages, with/without versions
* switching environments, source activate every time
* conda export, for sharing and reproducing
* pip install into a conda environment
* conda search for finding packages, available versions
* conda channels, local package installs

## What is Conda?

* conda is not anaconda
* environment manager
* package manager
* package dependency solver
* package creator

## Why Use Conda?

* so many packages
* mixed languages
* maintaining a compiler toolchain is hard
* solving package dependency graph is hard

## Roadmap

1. install conda
3. conda create
4. conda env list
6. source activate
7. conda list
7. conda install, update, remove
8. conda export
9. pip install into conda env
9. conda search
10. condarc, channels, local pkgs

## Installing Conda

* git clone, setup.py
* Anaconda
* Miniconda
* test the install
* conda info
* /home/juser/anaconda/bin/conda

## Creating Environments

* conda create -n austin python=2.7
* conda env list, conda info --envs
* source activate, every new shell
* conda list, packages in env
* /home/juser/anaconda/pkgs/
* /home/juser/anaconda/envs/austin/
* source deactivate
* where's my system python? bashrc, etc

## Modifying Environments

* conda list
* conda install numpy
* conda install numpy 1.10
* conda install -n austin pandas=0.19
* conda create -n texas python=3 numpy=1.11.1 pandas=0.19 jupyter
* conda upgrade
* conda remove -n texas jupyter
* conda remove -n texas --all

## More on Environments
* conda export -n austin > austin.yml
* conda env create -f austin.yml
* source activate austin; pip install something

## Conda Channels

* conda search
* condarc file and "channels:" list
* internal pkg mirrors, external pkg mirrors 
* what are all these files.tar.bz2 ???

## Conda Build

* not yet
* next lesson