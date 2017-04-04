# Plan, Part 4: Conda Build


## Topics


* why build a conda package?
* conda package distributions, Anaconda
* write a conda recipe: meta.yaml, build.sh, bld.dat
* conda build a pure python package
* conda install your local conda package
* importing your conda installed package
* upload your conda recipe and package to conda-forge
* repositories, repo.continuum.io, anaconda.org, conda-forge

## What is a conda package?

* executable code, e.g. python package
* conda recipe: meta.yml, build.sh, bld.dat
* conda build
* conda install --local
* files.tar.bz2

## Conda Package Distributions

* distributions
* anaconda, miniconda
* conda-forge

## Roadmap

1. write an installable python package
2. write a conda recipe
3. write a meta.yml
4. write a build.sh
5. install conda-build
6. conda build my_pkg_dir
7. conda install --use-locals
8. conda upload
9. condarc file and channels

## What is a Conda Recipe

* your code, python package
* conda recipe directory
* meta.yml file
* build.sh, bld.dat

## How to write a Recipe

* parts of a meta.yml
* import depends
* run depends
* test depends

## How to build

* write a build.sh
* python setup.py --install
* bld.dat and `conda convert`
* `conda build my_pkg_dir`
* path to local builds

## How to install

* source activate
* `conda install --use-locals`
* import my_pkg

## How to share

* condarc file and "channels:" list
* conda config --channels
* conda upload
* conda forge
* anaconda.org
