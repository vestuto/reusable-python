
# HOWTO Conda

**Open-source, cross-platform, package and environment management, for any language**

# Outline

* Quick Start
* Installing Conda
* Configuring Conda
* Using Conda
* Create and switch between conda environments
* Install, upgrade, and remove conda packages
* Document, share, and recreate conda environments
* Uninstalling Conda


# Quick Start: Set-Up


1. Download MiniConda installer

    ```bash
    http://conda.pydata.org/miniconda.html
    ```
2. Install MiniConda under user home (no admin, no sudo):

    ```bash
    http://conda.pydata.org/docs/install/quick.html
    ```
3. Create config file `$HOME/.condarc` for local channel:

	```bash
	allow_other_channels : false
	channels:
	  - http://hostname/conda/pkgs/free
	```


# Quick Start: Use


4. Create a conda env:

	```bash
	$ conda create -n py34 python=3.4.1 \
    ipython=5 numpy=1.10 scipy matplotlib h5py pandas
	```
5. Activate conda env:

   ```bash
   $ source activate py34  # Windows: "activate py34"
   ```
6. Run code to test:

   ```
   $ python -c \
   "import numpy as np; print(np.__version__)"
   ```


# Install Conda


* Easiest way to install conda is via MiniConda:

* [Download MiniConda Installer](http://conda.pydata.org/miniconda.html) with browser
* You can create and use both py2 and/or py3 envs with "MiniConda for Python 3"
* Check [MD5 hash](https://repo.continuum.io/miniconda/) for the downloaded installer file.
* Launch MiniConda Installer (bash script with embedded binaries)
* Chose install path, default user home, e.g. `/home/juser/`


# Test Install

### Test install

```bash
# Linux/OSX (Win: replace "which" with "where")
$ which conda
$ which python
$ echo $PATH
```

### Test conda

List packages in default conda environment: should be ~ 10, including conda, python, setup tools, wheel (pip), zlib, etc.

```bash
$ conda list
```

# Repository Access

### Test access to an external package repository

* Test access to conda package repository at Continuum: [http://repo.continuum.io](http://repo.continuum.io)

* Other conda repos can be found at [https://anaconda.org](https://anaconda.org), e.g. [conda-forge](https://anaconda.org/conda-forge)

### Test access to the internal package mirror

* Inside your company, test access to the internal package mirror
* use browser to view this URL: [http://hostname/conda/pkgs/free](http://hostname/conda/pkgs/free)


# Repository Search


You should see the following directories in the browser:

```
linux-64/
osx-64/
win-64/
noarch/
```

Each will contain a long list of conda package `files.tar.bz2`. 


If you can see those, test `conda search` on that mirror:

```bash
$ conda search python --override-channels -c http://hostname/conda/pkgs/free
```

You should get several listings, including 2.7, 3.4, 3.5, 3.6 and any pkg with the string "python" in the name.


# Conda Channels

A conda "channel" is just file location (URL) where a conda package file repository is located.

To set up an internal channel, you need to:

* Create a specific dir tree containing packages (`http://hostname/conda/pkgs/free`)
* Build or copy a package index into the top of that dir tree (`repo.data.json`)
* Create a conda user config file pointing to dir tree (`.condarc`)


# Custom Channels

### Create a Config File

Create a `.condarc` file for your user in your home dir:

```bash
/home/juser/.condarc
```

Edit the `.condarc` file such that it contains only:

```bash
allow_other_channels : false
channels:
  - http://hostname/conda/pkgs/free
```

### Test the Config File

With your config in place, the following cmd will list python versions available from the pkg repo:

```bash
$ conda search python
```


# Listing Envs and Pkgs

### List environments

List conda environments, NOT their packages:

```bash
$ conda env list
```

### List packages

See a list of packages in the default "root" env:

```bash
$ conda list
```

See a list of packages in a named env:

```bash
$ conda list -n py34
```


# Create Environments

Here we show how to create three different environments:

```bash
$ conda create -n py27 python=2.7
$ conda create -n austin python=3.4
$ conda create -n texas python=3.6
```

Notice that the environment name can be anything, e.g. `texas`


# Activate Environments

* By default, every new shell you open uses what conda calls it's `root` environment. 
* This has nothing to do with "system root" or "root user".
* To use other environments you have created, you must `activate` them.
* To verify, test the path to python after switching.

  ```bash
  # Linux/OSX
  $ source activate py27
  $ which python
  ```

*...for Windows, drop word "source", use "where" not "which"*


# Switching Environments

* `activate` also used for switching between envs:

  ```bash
  # Linux/OSX
  $ source activate py34
  $ which python
  ```

* Use `deactivate` to "switch" to the "root" conda env:

  ```
  # Linux/OSX
  $ source deactivate
  $ which python
  ```

*...for Windows, drop word "source", use "where" not "which"*


# Config: conda vs. system, set-up

* How do you "switch" back to the system python?
* Easiest way is a shell config
* Define shell functions in your `~/.bashrc`:

  ```bash
  export ORIGINAL_PATH=$PATH
  
  use_conda(){
      CONDA_PATH="~/anaconda/bin"
      export PATH="$CONDA_PATH:$ORIGINAL_PATH"
      echo "Added conda to your PATH"
      python --version
  }

  use_original(){
      export PATH=$ORIGINAL_PATH
      echo "Restored original PATH"
      python --version
  }
  ```
  
*...for Windows, involves mucking with `%PATH%`*

# Config: conda vs. system, usage

If you use this approach...

* edit your `~/.bash_profile` to include `source ~/.bashrc`.
* after opening a new shell, to use `conda`, use cmd:

    ```bash
    $ use_conda
    ```

* to switch back to your original `PATH`, use cmd:

    ```bash
    $ use_original
    ```
*personally, I keep `.bashrc` mostly empty and use project-specific `config.sh` files that I source when needed, keep those under version control!*


# Under the Hood

Pieces of the machinery:

* cmds: `$ conda help`
* envs: `/home/juser/anaconda/envs/<tree-of-links>`
* pkgs: `/home/juser/anaconda/pkgs/*.tar.bz2`
* path: shell variable `$PATH` and `source` command


# Modify an Environment

Most common modifications to an existing env:

* add pkg: `conda install pkg`
* update pkg: `conda update pkg`
* remove pkg: `conda remove pkg`


# Add packages

* Activate an env to install into it...

  ```bash
  # Linux/OSX
  $ source activate py27
  $ conda install numpy scipy
  ```

* Alternatively, from any conda env...

  ```bash
  $ conda install -n py27 numpy scipy
  ```

*...again, for Windows, drop word "source"*


# Update packages


* Update individual packages...

  ```bash
  $ conda update -n py27 numpy scipy
  ```

* Update all pkgs while maintaining pkg-to-pkg compatibility...

  ```bash
  $ conda update -n py27 --all
  ```

* Update `conda` itself in `root` env before doing anything...

  ```bash
  $ conda update conda
  ```


# Remove packages

* To remove one or more pkgs:

  ```bash
  $ conda remove -n py27 numpy scipy
  ```
* Removing pkgs can leave dependency detritus. 
* Often better to remove entire env.
* Create a new env that only includes what you need. 


# Delete an environment

* To delete an env, remove all packages from it.

  ```bash
  $ conda remove -n py27 --all
  ```

* Creating and deleting entire envs is easy and fast.
* When in doubt, delete and create a new one...
* "It's the only way to be sure".


# Export and Recreate Environments

* You can `export` a "manifest", listing all pkgs, versions

* Conda can **recreate** an env from the `environment.yml`!

* To `export` your conda environment:

  ```bash
  $ conda env export -n py34 > environment.yml
  ```

* To recreate the env: (assumes `environment.yml`)

  ```bash
  $ conda env create
  ```
* To recreate an env from a non-default file name:

  ```bash
  $ conda env create -f analysis_2017.yml
  ```


# Uninstall Conda: 1-of-2 steps

1. Delete the anaconda/miniconda directory tree:

	```bash
	$ rm -rf $HOME/anaconda
	```
    ...or:

    ```bash
	$ rm -rf $HOME/miniconda3
	```

    Forgot where you installed conda? Just ask the shell:

    ```bash
    $ which python
    ```


# Uninstall Conda: 2-of-2 steps


2. Remove lines from your shell config files
    * review both `$HOME/.bash_profile` or `$HOME/.bashrc`
    * remove `PATH` changes by conda/Anaconda/MiniConda:
	  ```bash
	  # added by Anaconda3 4.2.0 installer
	  export PATH="/Users/juser/anaconda/bin:$PATH"
	  ```
    * remove any shell functions you added like `use_conda`


