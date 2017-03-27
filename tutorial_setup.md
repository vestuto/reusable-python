# Tutorial Setup

Before the tutorial you should...

* download an [Anaconda3 installer file](https://www.continuum.io/downloads) for your system.
* [Install Anaconda3](https://docs.continuum.io/anaconda/install) under your user account home directory: this will not affect your system install of python.
* Download the tutorial materials from [https://github.com/vestuto/reusable-python](https://github.com/vestuto/reusable-python), either as a ZIP file or using git clone.
* Locate the `check_version.py` script found within the downloaded course content. Unzip if needed.
* Open a NEW terminal or command-prompt, navigate to the directory containing the `check_version.py` script, and run it as follows: `python ./check_version.py` 
* If script returns `False`, or an error, close your terminal/command-prompt, open a new one, and try again. If the `check_version.py` runs and Anaconda found is `True`, continue. 
* Use the terminal/command-prompt to install `conda-build` by running the following command: `conda install conda-build` 
* To test the install of `conda-build`, open a terminal/command-prompt and run the command: `conda build --help`. You should see a long help text description.
* optional: download and install a text editor, e.g. [sublime text](https://www.sublimetext.com/3)
* optional: if on Windows, download and install `git-bash` from [https://git-scm.com/download/win](https://git-scm.com/download/win)

Notes:

* We will also create conda environments as a student exercise, so no need to do so before hand.
* One week before the tutorial, get the latest version of the course content by downloading ZIP, cloning the project, of "git pull" content

