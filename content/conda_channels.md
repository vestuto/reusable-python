
# Conda Channels

Conda Channels are the the means of distributing entire repositories of conda packages. From a user point of viw, they are represented by file paths (http://, file://) that conda uses to search, find, download, and upload packges. 

In this lesson, we'll see how to configure both local and external channels, how to create a custom channel, and how to spin up our own HTTP services to serve out conda packages.

## Table of Contents

* [Installing from Channels](#Installing-from-Channels)
	* [Default Channels](#Default-Channels)
	* [Uploading Packages](#Uploading-Packages)
	* [Uploading to Anaconda Cloud](#Uploading-to-Anaconda-Cloud)
* [Custom Channels](#Custom-Channels)
	* [Repository Channels](#Repository-Channels)
	* [Local Channels](#Local-Channels)
		* [Preparing the Local Chanel](#Preparing-the-Local-Chanel)
		* [Searching Local Channels](#Searching-Local-Channels)
		* [Installing from Local Channel](#Installing-from-Local-Channel)
	* [HTTP Serving Local Channels](#HTTP-Serving-Local-Channels)
		* [Prepared your conda config](#Prepared-your-conda-config)
		* [Start HTTP Server](#Start-HTTP-Server)
		* [Test HTTP Service](#Test-HTTP-Service)
	* [Exercise: Install from your HTTP Server](#Exercise:-Install-from-your-HTTP-Server)
	* [Exercise: Have others Install from your HTTP Server](#Exercise:-Have-others-Install-from-your-HTTP-Server)
* [Recap and Preview](#Recap-and-Preview)

# Conda Channels

* Conda packages are usually installed from channels, not just from local builds.
* Channels are the paths (URLS, really) that conda searches for packages.
* The easiest way to use channels is to use a private (Anaconda Repository) or public (`anaconda.org`) repository with pre-existing channels.
* Custom channels can be constructed locally, and installed from using `file://` URLs, using just conda.

## Default Channels

* `anaconda.org` is the default repository from which conda installs packages
* `defaults` defines the default channels on `anaconda.org` which conda searches when asked to install a package.
* in the previous example we had to force conda to **not** look for `anaconda.org`
* we used the `--use-local` flag to install the local constants package. 

> For example, if want to install `numpy`, run `conda install numpy`. The numpy package file would be copied from from a channel called `default` that is hosted by Continuum Analytics at `repos.continuum.io`

## Uploading Packages

Recall the message that was seen at the end of a successful conda package build:

```
# If you want to upload this package to anaconda.org later, type:
#
# $ anaconda upload /Users/juser/anaconda/conda-bld/osx-64/constants-0.0.1-py35_0.tar.bz2
#
# To have conda build upload to anaconda.org automatically, use
# $ conda config --set anaconda_upload yes
```

## Uploading to Anaconda Cloud

This is very common way of sharing conda packages with the community of conda users. It first requires creating a account on `anaconda.org`.

* uploading to anaconda.org personal account
* installing from anaconda.org personal account
* how your distant collaborators can also install from anaconda.org

The steps are as follows:

* `conda install anaconda-client`
* `anaconda login`
* `conda config --set anaconda_upload yes`
* `anaconda upload $HOME/anaconda/conda-bld/osx-64/constants-0.0.1-py27_0.tar.bz2`

<div class='alert alert-success'>
<br>
<big>Exercise: Install your package using anaconda.org<br><br></big>
Install your recently uploaded package from anaconda.org using the following command:
</div>

```bash
conda install constants --channel <YOUR-ANACONDA-USERNAME>
```

# Custom Channels

## Repository Channels

You can use channels that are not the defaults on repositories like Anaconda Cloud or a private instance of Anaconda Repository.

To do so, you must add the channel to your conda figuration as follows:

```bash
conda config --add channels http://anaconda.org/<USERNAME>
```

## Local Channels

You can create custom local channels as well. 

While it is best to use Anaconda Cloud or Anaconda Repository, this example is useful in understanding how channels work.

*This demonstration was developed and tested using `conda 4.1.11`*

### Preparing the Local Chanel

Preparing the local channel requires the following steps:
* find or build at least one conda package
* create a file tree for your channel:
    * top level dir is the channel name
    * sub-dirs for platform specific packages
* place your conda packages (files.tar.bz2) into the path
* run `conda index` on the platform sub-dirs

```bash
conda build my_recipe
mkdir /opt/my_channel/osx-64/
cd ~/anaconda/conda-bld/osx-64/
cp constants-0.0.1-py35_0.tar.bz2 /opt/my_channel/osx-64/
conda index /opt/my_channel/osx-64/
```

You can use `conda convert` to add packages for other platforms to your local channel:

```bash
mkdir /opt/my_channel/win-64/
cd ~/anaconda/conda-bld/osx-64/
conda convert constants-0.0.1-py35_0.tar.bz2 -p win-64
cp win-64/constants-0.0.1-py35_0.tar.bz2 /opt/my_channel/win-64/
conda index /opt/my_channel/win-64/
```

### Searching Local Channels

After preparing your channel, test it with `conda seach`:

```bash
conda search -c file://opt/my_channel constants --override-channels
```

### Installing from Local Channel

Once prepared and tested, you are ready to install from your channel:

* create a new environment
* activate that environment
* install a package from your local channel with `conda install`
    * use `-c file://full_path_to_channel`
    * also use the `--override-channels` flag

```bash
cd ~/
conda create -n test-local-channel python=3.5 ipython
source activate test-local-channel
conda install -c file://opt/my_channel constants --override-channels
```

## HTTP Serving Local Channels

You can even serve your local channels over HTTP:

*Note: this is leading us to the capability that Anaconda Cloud and Anaconda Repository provide.*

### Prepared your conda config

Update your `~/.condarc` by adding the IP address as shown:

```bash
channels:
- http://0.0.0.0:8000
- defaults
```

### Start HTTP Server

Use python to start an HTTP server:

Start the HTTP server from the directory that contains your indexed `osx-64` and `win-64` subdirs, so that they appear at the top level of the file tree served out:

```bash
cd ~/Desktop/my_channel
python -m http.server
```

### Test HTTP Service

Open a web browser to verify that you can see the directory contents, but crowsing to the following URL:

```
http://0.0.0.0:8000
```

TO install from this HTTP served channel, use `conda install` and specifiy the `<URL>:<PORT>` as the channel:

```bash
conda create -n test python=3.5
source activate test
conda install -c http://0.0.0.0:8000 constants
```

## Exercise: Install from your HTTP Server

Using `http://127.0.0.1:8000` in your `~/.condarc` and then install with `conda install -c http://local.host constants`. Again, use a web browser and try to load `http://127.0.0.1` to see if you get a file listing of the contents of `my_channel`

```
#~/.condarc
channels:
- http://127.0.0.1:8000
- defaults
```

## Exercise: Have others Install from your HTTP Server

Find you assigned IP address on the local network. For example, on Linux of Mac, in a terminal, run the `ifconfig` command, and look for the value of `inet` in the output block labeled `en0`. Give that IP address to your classmate to your left, and ask them to run the commands above, but replace `0.0.0.0` or `127.0.0.1` with this new address. Does it work?

```
#~/.condarc
channels:
- http://10.0.32.184:8000
- defaults
```

```bash
conda create -n test-http python=3.5
source activate test-http
conda install -c http://10.0.32.184:8000 constants --override-channels
```

# Recap and Preview

In this lesson we saw....

* Building a Conda package
* Installing a local conda package
* Installing packages from channels
* Uploading a custom conda package to anaconda.org
* Creating a custom local package channel
* Serving a local channel with a HTTP service

---

