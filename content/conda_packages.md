
# Conda Packages

Conda packages are the building blocks of working environments. 

They are the fundamental unit of organization and order in an otherwise disordered universe of working environments composed of many software library installs. They serve an organizational unit in a way very much analogous to that of python modules and python packages, as organizational units of collections of software.

In this lesson, we'll see how to create, install, and distribute your own conda packages, whether for use internally or in sharing with a broader, more open community.

The overview of creating and installing python packages which preceeded this served to prepare for conda packages in two ways:
* a python package provides the basic ingredient needed to create a conda package
* the process of python package creation introduces concepts needed to understand conda packaging

## Table of Contents

* [Before building a conda package](#Before-building-a-conda-package)
* [Building and Installing conda Packages](#Building-and-Installing-conda-Packages)
	* [Before you invoke conda](#Before-you-invoke-conda)
	* [Creating a Recipe from Scratch](#Creating-a-Recipe-from-Scratch)
	* [Creating a Recipe from Skeletons](#Creating-a-Recipe-from-Skeletons)
	* [Building a Conda Package from a Recipe](#Building-a-Conda-Package-from-a-Recipe)
	* [Install a conda package](#Install-a-conda-package)

* [Recap](#Recap)


# Before building a conda package

There are several things to keep in mind before building a conda package.


(1) A conda package is a file archive that contains ***executable*** programs.

* think of it as a container of a software library.

(2) Conda is ***not just for python***. A conda package may be composed of:

* purely interpreted programs, like Python or R
* purely compiled programs, like C++ or Fortran
* a mixture of interpreted and compiled programs.

(3) ***Building*** conda packages sometimes requires compiling

* This is an implication of point (1) and point (2)
* For our demonstration, we will make a conda package from pure Python: compiling in this case is not needed.
* If you wish to build a conda package for a software library which does contain source written in a compiled language (e.g. C, C++), the only change to the conda packaging process is that you must supply a build script capable of compiling your code. 

(4) ***Installing*** conda packages does NOT require compiling

* This is an implication of point (1)
* While creation of the conda package may require a compiler, installation of a conda package does not.
* Installing with conda means NOT having to install nor maintain your own set of compilers and build tools.
* Many conda packages have been created by Continuum Analytics and are available for free download and install using conda.


---

# Building and Installing conda Packages

Conda serves as an alternate method for installing packages for use with python. Conda does not create python packages for you, but it does help you install, uninstall, and manage them. 

All conda asks in return, is that you "wrap" your packages inside container called a "conda package" so that conda can keep track of a wide variety of packages ***and their interdependencies*** in a consistent way.

The outline of the process to create a conda package is as follows:

1. write a software library
2. write a script that builds and/or installs this library
3. write a conda recipe
4. create a conda package from the conda recipe using conda-build

---

## Before you invoke conda

Regardless or the languages involved, whether compiled or interpreted, to build a conda package, your code must already be **executable** and **installable** without conda. 

By **"executable"** we mean that it must run without error if written in an interpreted language, and must build without error if written in a compiled language.

---

## Creating a Recipe from Scratch

Once your code is executable, you are ready to start creating a conda recipe.

A conda recipe is very much what its name implies: a list of raw ingredients and a list of steps by which those ingredients are processed and combined so as to generate something new: in this case, a conda package.

```bash
Desktop/
    my_recipe/
        meta.yaml
        build.sh
        bld.bat
```

The files within the directory `my_recipe` make up the conda recipe:

```bash
meta.yaml
build.sh
bld.bat
```

The files of the recipe serve the following purposes:

* one `meta.yaml` file, which defines build and run-time dependencies
* two `build scripts`, which compile source code (if needed) and install executable programs
* notice that there is one build script `build.sh` for Linux, and one `bld.bat` for Windows. 

Example contents of the recipe files are as follows:

* Contents of `meta.yaml`:

```
package:
  name: constants
  version: "0.0.1"

source:
  path: ../my_package

requirements:
  build:
    - python
    - setuptools
  run:
    - python

test:
  imports:
    - constants

about:
  license: CC BY-NC-SA 4.0
  license_file: LICENSE.txt
```

* Contents of `build.sh`: 
	
```bash
python setup.py install
```

* Contents of `bld.bat`: 
	
```bash
"%PYTHON%" setup.py install
if errorlevel 1 exit 1
```

---

<div class='alert alert-success'>
<br>
<big>Exercise: Create a Conda Recipe<br><br></big>
Create the file tree shown above, and use a text editor to copy and paste the contents above into the files.
</div>

---

## Creating a Recipe from Skeletons

It is not always necessary to create a recipe from scratch.

There is a large collection of python packages at the site [Python Package Index](pypi.python.org). You can ask conda to build a recipe based on a package hosted on `pypi`.


---

<div class='alert alert-success'>
<br>
<big>Exercise: Skeleton Recipe<br><br></big>
Use the following command to create a conda recipe with the conda skeleton tool. This requires access to the website https://pypi.python.org/pypi
</div>

```bash
conda skeleton pypi pyinstrument
```

Confirm that you now have a directory with the following contents:

```bash
pyinstrument/
   meta.yaml
   build.sh
   bld.bat
```

Inspect the contents of the files created above with a text editor such as NotePad, TextEdit, or Emacs.



---


## Building a Conda Package from a Recipe

Now that you have a recipe, composed of the three files shown above, you can build the conda package from it. The process diagram might looks like this:

> (recipe + ingredients) > (conda-build) > (conda package)

The actual commands will be as follows:

* installing conda build, from your shell:

	```bash
	conda install conda-build
	```

* recall where your conda recipe was located:

	```bash
	Desktop
	    my_recipe
	        meta.yaml
	        build.sh
            bld.bat
	```

* using conda build to build from a recipe

    ```bash
    cd Desktop
    conda build my_recipe
    ```
* output from conda build is conda package, which takes the form of a compressed file archive with a name like `constants-0.0.1-py35_0.tar.bz2`

Likely output path will be:

* Linux or Mac-OSX:

	```bash
	 $HOME/anaconda/conda-bld/osx-64/`
	```

* Windows:

	```bash
	 %HOME%\anaconda\conda-bld\win-64\`
	```


---

<div class='alert alert-success'>
<br>
<big>Exercise: Build a Conda Package<br><br></big>
Install `conda-build`, and use it to build both recipes created above: `my_recipe` and `pyinstruments`. Compare the outputs.</div>

The output will be quite verbose, but should end with a message similar to the following block:

```
# If you want to upload this package to anaconda.org later, type:
#
# $ anaconda upload /Users/juser/anaconda/conda-bld/osx-64/constants-0.0.1-py35_0.tar.bz2
#
# To have conda build upload to anaconda.org automatically, use
# $ conda config --set anaconda_upload yes
```

---

<div class='alert alert-success'>
<br>
<big>Exercise: Build using `setup.py` instead of `build.sh`<br><br></big>
Remove the `build.sh` and `bld.bat` files from the recipe directory, and add the following block of code to the `meta.yaml`. Then try to rebuild the conda package from the resulting simplified recipe which contains only the updated `meta.yaml` file.
</div>

```python
    build:
        script: python setup.py install
```

---

## Install a conda package

As preparation, install `ipython` into the same environment in which you intend to install your new `constants` conda package, else you may get the system or `root` install of `ipython`

Before we install, let's make sure we remove to old "manually" installed version of the package:

```bash
/Users/juser/anaconda/lib/python3.5/site-packages/constants-0.0.1-py3.5.egg
```

Installing a locally created conda package is done as follows:

```bash
conda install --use-local constants
```

```
juser:~ ] $ conda install --use-local constants
Fetching package metadata .........
Solving package specifications: ..........
Using Anaconda Cloud api site https://api.anaconda.org

Package plan for installation in environment /Users/juser/anaconda:

The following NEW packages will be INSTALLED:

    constants: 0.0.1-py35_0 local

Proceed ([y]/n)?
```



---


<div class='alert alert-success'>
<br>
<big>Exercise: Installing your conda package<br><br></big>
Create a new conda environment called `test1`. Then use `conda install --use-local constants` to install the local package.
</div>

```bash
conda create -n test1
source activate test1
conda install --use-local constants
```

Then test the exercise install in two ways:

* Launch the system shell, and run `conda list`, and see if `constants` is listed.
* Launch the IPython shell, and import the package with `import constants`.



---


<div class='alert alert-success'>
<br>
<big>Exercise: Installing your package using the full path<br><br></big>
Create a new conda environment called `test2`. Then install the package by referencing the file path directly, as show below:
</div>

```bash
conda create -n test2 python=3.5 ipython
source activate test2
conda install /path/to/constants-0.0.1-py35_0.tar.bz2
```

In this case `/path/to/` is the location of the conda package output from running `conda-build`. Modify the actual package file name to match exactly what was output by `conda-build`.


---


<div class='alert alert-success'>
<br>
<big>Exercise: Test the previous install by importing<br><br></big>
Install this package using the command above and then open a python interpreter and test the install by trying to import and use the package as follows:
</div>

```python
>>> import constants
>>> constants.PI
3.14159
>>> constants.compute_pi()
3.1415926535897931
```

---

<div class='alert alert-success'>
<br>
<big>Exercise: Rebuild the package for python 2.7<br><br></big>
Create a new conda environment for python 2.7 and activate it. Then use `conda build --python=2.7 constants` to rebuild the conda package. Once built, install it and test it as done above with python3.
<br>
<br>
*Hint: the `print()` function in the `constants.py` file is compatible with Python 3 but behaves differently in Python 2. Make any necessary syntax changes or imports needed.*
</div>



---

# Recap


* Writing a Conda package recipe
* Building a Conda package from scratch
* Building a Conda package from PyPI skeletons
* Installing a local conda package

---

