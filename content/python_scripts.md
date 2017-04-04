# Reusable Scripts

Python scripts are one of the first units of reusable code that someone new to python creates. Scripts are ubiquitous in data processing and data munging workflows. While they should only be a first step, many python users never go much further than this. We can do better, and we'll see how in this lesson.

# Table of Contents

* [Scripts vs. Modules](#Scripts-vs.-Modules)
	* [Example Script 1](#Example-Script-1)
	* [Example Script 2](#Example-Script-2)
	* [Example Script 3](#Example-Script-3)
* [Module Basics](#Module-Basics)
	* [import](#import)
	* [sys.path](#sys.path)
* [Inputs](#Script-Inputs)
	* [Input Args and sys.argv](#Input-Args-and-sys.argv)
	* [Input Args and argparse](#Input-Args-and-argparse)
* [Streams: stdin, stdout, stderr](#Streams:-stdin,-stdout,-stderr)
	* [stdout](#stdout)
	* [stdin](#stdin)
	* [Subprocess](#Subprocess)


# What is a script?

A python script is simple a plain text file saved to disk with a name the ends with the ".py" extention.

```
my_script.py
```

They can be created with any text editor or other tool capable of saving to plain text.

They con contain 0 lines or 1000 lines.

```python
# This is a script. It's not a very good one.
from __future__ import print_function
msg = "Hello World"
print(msg)
```

You can run this script from the shell:

```bash
$ python ./my_script.py
```

In this example, there 5 parts, so it's not the simplest, but close to it.


1. `# This is a script. ` - reuse help: in this case a single comment line, starting with a `#`, is ignored by the python interpreter but very valuable to the human interpreter trying to reuse the script later.
2. `from __future__ import print_function` - reuse code: this is one of two primary mechanisms for bringing in reusable code from the "outside" to use inside our script.
3. `msg = "Hello World"` - reuse data: this creates a string object in memory with the value "Hello World" and then "binds" the name `msg` to it, so that it can be used and reused later in the script.
4. `print(msg)` - reuse methods: this is reusing a function code block built into python itself, together with our data.

# Scripts vs. Modules

## Example Script 1

Any file with python in it can be run as a script


```python
# Open text editor and create new file in CWD
script_name = "script_01.py"
script_fullname = os.path.join(cwd, script_name)
print("Open a text editor and create a new file here: \n" + script_fullname)
```

Create a file with the following content:
```python
print("Hello World")
```

Use a text editor, or run the following command to create script_01.py:


```python
%%file script_01.py
print("Hello World")
```


```python
# run script
!python3 script_01.py
```


```python
# import script
import script_01
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

Use a text editor, or run the following command to create script_02.py:


```python
%%file script_02.py
print("Inside of script: before def func()")
def func(thing):
    print("Inside of script: inside def func()")
    print("The input to func: ", thing)
print("Inside of script: after def func()")
func("Hello World")
print("Inside of script: after call to func()")

```


```python
# run script
!python3 script_02.py

# Notice the order of the print() statements!!!
```


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

# Module Basics

## import

All code in a module is executed on import
* def statements only create functions, not call them
* if you a module to act like both a library and a script, write a main, and wrap it in a test for `__name__`


```python
if __name__ == "__main__":
    print("What's in a name?")
```

## sys.path

Python searches the paths contained in `sys.path` to find anything you try to import


```python
import sys
sys.path
```

Installing a python module can be as simple as copying the file into a path like

>  '/Users/jvestuto/anaconda/lib/python3.5/site-packages' 

or using an install tool that does this for you.

*Note: Most installs are NOT that simple! Dear Team Conda, we love you!*

# Inputs

A script is not very reusable if we cannot change input new content.

## Input Args and sys.argv


```python
import sys
```


```python
# argv for the notebook looks a bit weird

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
%%file script_arg_test01.py
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
    This is the docstring for the my_print() method in the tutorial.py module

    This will appear when you call help(my_print) or use the my_print? in ipython
    """
    print(msg)
    return None

def build_parser():
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
    return parser


def main():
    """
    This is the docstring for the main() method in the tutorial.py module
    """

    # Build parser and parse input args
    parser = build_parser()
    args   = parser.parse_args()
    
    # Unpack the args (optional)
    num_days  = args.num_days
    file_path = args.file_path

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


