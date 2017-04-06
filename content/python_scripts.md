# Reusable Scripts

Python scripts are one of the first units of reusable code that someone new to python creates. Scripts are ubiquitous in data processing and data munging workflows. While they should only be a first step, many python users never go much further than this. We can do better, and we'll see how in this lesson.

# Table of Contents

* [Syene Script](#First-Script)
* [Shell to Script](#Shell-to-Script)
* [Examples](#Examples)
	* [Example Script 1](#Example-Script-1)
	* [Example Script 2](#Example-Script-2)
	* [Example Script 3](#Example-Script-3)
* [Inputs](#Script-Inputs)
	* [Input Args and sys.argv](#Input-Args-and-sys.argv)
	* [Input Args and argparse](#Input-Args-and-argparse)
* [Streams: stdin, stdout, stderr](#Streams:-stdin,-stdout,-stderr)
	* [stdout](#stdout)
	* [stdin](#stdin)
	* [Subprocess](#Subprocess)


# Syene Script

In about the year 230 BCE, [Eratosthenes estimated the radius of the Earth](http://outreach.as.utexas.edu/marykay/assignments/eratos1.html) to an accuracy within 5% of [the modern value](https://nssdc.gsfc.nasa.gov/planetary/factsheet/). He read (perhaps from a differnet kind of "script") that on the summer solstice, the sun was reflected from the water at the bottom of a deep well in Syene. The Sun was directly overhead. On the same day in Alexandria, he noticed a tall obelisk cast a shadow at an angle of about 7 or 8 degrees from vertical. So he walked from Alexandria to Syene, and counted his steps along the way.

Enter the following lines into the ipython terminal.
Then at the end use the `save` command to write all this to a file called `syene_script.py`

```python
from __future__ import print_function
import math

# measure lengths shadow & stick, get angle
stick = 1.8
shadow = 0.23
rad2deg = 180.0/math.pi
angle = math.atan(shadow/stick)*rad2deg
print("shdow angle = ", angle)

# walk from Alexandria to Syene
step = 2  # meters
counts = 395000
travel = step * counts 
print("travel distance = ", travel)

# assume earth is a sphere
# use ratio of angles = ratio of lengths
circumference = travel * (360 / angle)
radius = circumference / (2.0 * math.pi)
print("estimated earth radius = ", radius)

# compute error
known_value = 6378137 
error = 100 * math.fabs(known_value - radius) / known_value
print("known value = ", known_value)
print("error % = ", error)

```

Open a text editor, copy/paste the above lines into it, and save it as `syene_script.py`

--

# Shell to Script

You can use the ipython shell to save your command line history to a file:

```python
In [1]: import math
In [2]: pi = math.pi
In [3]: deg2rad = pi/180.0
In [4]: zero = math.cos(90.0 * deg2rad)
In [5]: save radian.py 1-4

The following commands were written to file `radian.py`:

import math
pi = math.pi
deg2rad = pi/180.0
zero = math.cos(90.0 * deg2rad)
```

--

You can also load file contents from a file on disk into an ipython shell:

```
In [1]: %load radian.py

    ...: import math
    ...: pi = math.pi
    ...: deg2rad = pi/180.0
    ...: zero = math.cos(90.0 * deg2rad)
    ...: 

In [2]: print(pi)
3.141592653589793
```
### Exercise: Perform the steps above

You should have a file `radian.py` after you are done. Use a text editor to confirm the existence and contents of that file.

--

# What is a script?

A python script is any plain-text file saved to disk with a name the ends with the ".py" extention.

```
./src/my_script.py
```

They can be created with any text editor or other tool capable of saving to plain text.

```python
# This is a script. It's not a very good one.
from __future__ import print_function
msg = "Hello World"
print(msg)
```

### Exercise

Use `%load ./src/my_script.py` to view the contents of the script in the ipython shell.

--

In this example, there 4 lines, so it's not the simplest, but close to it.


1. `# This is a script. ` - reuse help: in this case a single comment line, starting with a `#`, is ignored by the python interpreter but very valuable to the human interpreter trying to reuse the script later.
2. `from __future__ import print_function` - reuse code: this is one of two primary mechanisms for bringing in reusable code from the "outside" to use inside our script.
3. `msg = "Hello World"` - reuse data: this creates a string object in memory with the value "Hello World" and then "binds" the name `msg` to it, so that it can be used and reused later in the script.
4. `print(msg)` - reuse methods: this is reusing a function code block built into python itself, together with our data.

--

You can run this script from the system shell:

```bash
$ python ./src/my_script.py
```

You can also run this script from the ipython shell:

```bash
In [1]: %run ./src/my_script.py
```
--

# Examples

## Example Script 1

Any file with python in it can be run as a script. Create a file with the following content:

```
print("Hello World")
```

Use a text editor, or run the following command to create script_01.py:

```python
#  write a script from ipython shell
In [42]: print("Hello World")
save script_01.py 42
```

```python
# write a script from a jupyter notebook cell
%%file script_01.py
print("Hello World")
```

Now run the script and observe the behavior...

You can run it from your system shell (e.g. bash or cmd.exe)

```python
$ python script_01.py
```

You can also run it from within the ipython shell using the `!` character to pass commands to the system shell:

```python
In [45]: !python script_01.py
```

Or use the special `run` keyword available within ipython:

```python
In [46]: run ./script_01.py
```

## Example Script 2

Chunking code into reusable functions if one of the first steps towards turning a script into a reusable library or module.

```python
## Type in the following contents into your new `script_02.py`

print("Inside of script: before def func()")

def func(thing):
    print("Inside of script: inside def func()")
    print("The input to func: ", thing)

print("Inside of script: after def func()")

func("Hello World")

print("Inside of script: after call to func()")

```

Use a text editor to create script_02.py:


```python
# script_02.py
print("Inside of script: before def func()")
def func(thing):
    print("Inside of script: inside def func()")
    print("The input to func: ", thing)
print("Inside of script: after def func()")
func("Hello World")
print("Inside of script: after call to func()")

```

Then run the script from either the system shell or the ipython shell:


```python
# run script
In [46]: !python3 script_02.py

# Notice the order of the print() statements!!!
```

You can also `import` a script!

```python
# import script
import script_02

# Notice that all code in the file gets executed upon import!!!
```

Problem! We don't want all the code to execute on import. Let's see how to adapt this script into a reusable module.

## Example Script 3

To make your file usable as both a script and a module, you need to add a conditional test of `__name__`

```python
## Type in the following contents into your new `script_03.py`

def func(thing):
    print("Inside of func()")
    print("The input to func: ", thing)

def main():
    print("Inside of main()")
    func("Hello World")

if __name__ == '__main__':
    print("Inside of __name__ test")
    main()
```

Use a text editor, or run the following command to create script_03.py:


```python
%%file script_03.py
def func(thing):
    print("Inside of func()")
    print("The input to func: ", thing)

def main():
    print("Inside of main()")
    func("Hello World")

if __name__ == '__main__':
    print("Inside of __name__ test")
    main()
```


```python
# run script
!python3 script_03.py
```


```python
# import script
import script_03

# Notice that NOTHING is printed upon import! Yay!! We did it!
```


# Inputs

A script is not very reusable if we cannot change input new content.

## Input Args and sys.argv


```python
import sys
```


```python
# argv for the jupyter notebook looks a bit weird

print( 'Number of Arguments:', len(sys.argv) )
print( 'Argument Values:', str(sys.argv) )
```

Create a new file with the following path location and name:


```python
import os
os.path.join( os.getcwd(), 'script_arg_test01.py')
```

```python
import sys

print( 'Number of Arguments:', len(sys.argv) )
print( 'Argument Values:' )
count = 0
for arg in sys.argv:
    print( "    sys.argv[%s]: %s" % (count, str(arg)) )
    count += 1
```

Use a text editor to screat the file and enter the text above, or simple execute the following:


```python
# if in a jupyter notebook, use the %%file to write
# %%file script_arg_test01.py
import sys
print( 'Number of Arguments:', len(sys.argv) )
print( 'Argument Values:' )
count = 0
for arg in sys.argv:
    print( "    sys.argv[%s]: %s" % (count, str(arg)) )
    count += 1
```

Then run the script from your system CLI shell as:

```bash
python3 script_arg_test01.py
```

## Input Args and argparse

The module `argparse` provides much more powerful input arg capabilities

Create a file called `script_argparse.py` with the following contents:

* Include the top level docstring
* Using at least one function, in this case `my_print()`
* Encapsulating the argparse set-up in a function
* Doing more of the work inside a `main()` function
* Inclusion of a conditional test for `__name__` for dual-use script/module

```python
import argparse
    
"""
This is the docstring for a module named 'tutorial'.
Note that this file has to be in your current dir or
in a path listed in sys.path
"""

def my_print(msg="This is a script"):
    """
    This is the docstring for the my_print() method
    This will appear when you call help(my_print) or 
    if you type my_print? in ipython
    """
    print(msg)
    return None

def get_inputs():
    """Build input arg parser"""
   
    # Create defaults and help strings
    help_arg_d = 'days, int,    default = %(default)s'
    help_arg_p = 'path, string, default = %(default)s'
    default_arg_d = 7
    default_arg_p = "tmp"

    # Create a parse object
    parser = argparse.ArgumentParser( description='Tutorial Module' )

    # add args to parser object
    parser.add_argument('-d', '--days', dest='num_days',  help=help_arg_d, default=default_arg_d, type=int)
    parser.add_argument('-p', '--path', dest='file_path', help=help_arg_p, default=default_arg_p, type=str)

    args  = parser.parse_args()

    return args


def main():
    """
    This is the docstring for the main() method in the tutorial.py module
    """

    # Build parser and parse input args
    inputs = get_inputs()
    
    # Unpack the args (optional)
    num_days  = inputs.num_days
    file_path = inputs.file_path

    # Use input args
    my_msg = "Number of days = " + str(num_days) + "\n"
    my_msg += "File path = "     + file_path
    my_print(my_msg)

    return None

if __name__ == "__main__":
    main()

```

Now test the script:


```python
! python3 script_argparse.py --help
```

# Streams: stdin, stdout, stderr

Crewating scripts that can interact with your system streams stdin, stdout, stderr

Streams:

* stdin and stdout are file-like objects (called "streams") provided by the OS.
* for interactive shell
    * stdin < keyboard
    * stdout > tty
* shell can "connect" stdin/stdout to other things:
    * redirect from/to files: `echo < infile`, `echo "hello"> outfile`
    * pipe output/input from/to other programs: echo "hello world" | grep hello

Unix and Python:
> The ability to redirect input and output streams to programs is a powerful aspect of the Unix design philosophy. 

> The streams `sys.stdin`, `sys.stdout`, and `sys.stderr` in `sys` bring that power to Python programs.

Python:

* input() reads from stdin
* print() writes to stdout
* sys.stdin.read() < stdin
* sys.stdout.write() > stdout

## stdout


```python
# print() is a thin wrapper for sys.stdout.write() and does nice things like converts inputs to strings for you 
print(99)
```


```python
# sys.stdout.write() is raw, and doesn't do any conversion for you
import sys

# sys.stdout.write( 99 )     # ERROR
# sys.stdout.write( '99' )   # no line return
sys.stdout.write(str(99) + '\n') # mimic print() output
```

## stdin

The very manual way...



```python
name = input("What's your name? ")
```


```python
print( name )
```

A better way is to use `sys.stdin.read()` in a script to make that script "stream compliant":


```python
# Check which directory you are about to write to...
import os
os.getcwd()
```


```python
%%file script_stdin.py
# Contents of script_stdin.py
import sys
data = sys.stdin.readlines()
print "This file contains", len(data), " lines."
```

Then run the script from your system CLI shell as:

In the Linux or OSX shell:
```bash
cat script_stdin.py | python3 script_stdin.py
```

In the Windows shell:
```bash
type script_stdin.py | python3 script_stdin.py
```

## Shells: Subprocess

Finally, for writing python scripts that need more complex interactions with the system shell, use the `subprocess` module


```python
"""
Demonstration of the subprocess module for interfacing with stdin/stdout of the shell
"""

import os
import subprocess


if os.name == 'nt': # is it a windows machine
    shell_command = "dir"
else:               # it is not windows
    shell_command = "ls -thor" # List my files, O Mighty Thor!
proc = subprocess.Popen(shell_command.split(), stdout=subprocess.PIPE)
output = proc.stdout.read()

print(output)

# The End
```

# Recap

* Scripts vs. Shells
* Scripts vs. Modules
* Module Basics
* import and sys.path
* Inputs: sys.argv, argparse
* Streams: stdin, stdout, stderr
* Shells: Subprocess


