
# Python Modules

Another means to reuse code is by gathering a collection of ***definitions*** of classes, functions, and data into python source files called *modules*.

The idea is to use or define units with well-defined purpose and scope, and reuse them instead of copying source lines of similar code.

The module file usually contains definitions of classes, functions, and global variables, data containers, and some statements to initialize the module.

--

Herein we will see how to transform **scripts** into **modules** and prepare a **package**.

* A **script** is a unit of python code that is executed from a single file. It need not use functions.

* A **module** is a unit of python code that can be be *imported* into other python code files. It need not be directly executable as a script.

* A **package** is a collection of python **modules** that can be *imported* as a whole using a package manager. A package need not provide executable scripts, but should provide some testing capabilities.

--

# Exercise: Tidy up Script

* Use a text editor to open the script `./src/syene_script.py`
* Add function definitions, one for each code block marked by a comment line.
* Add a `main()` function that calls the others, and reproduces the behavioe of `syrene_script.py`
* Save as `syene_module.py`


--

# Table of Contents

* [Modules](#Modules)
* [Examining a module file](#Examining-a-module-file)
* [Script or module?](#Script-or-Module?)
* [Creating a module](#Creating-a-module)
* [Consensual privacy](#Consensual-privacy)
* [Dunder names](#Dunder-names)
* [Recommending visibility](#Recommending-visibility)
* [Re-importing a module ](#Re-importing-a-module)

--

# Modular Coding

[*Modular programming*](https://en.wikipedia.org/wiki/Modular_programming) improves readability and maintainability of your programs. In practice, programs have fewer bugs and are easier to extend and debug/troubleshoot. 

The key idea is to emphasize separating the functionality of programs into independent, interchangeable modules, such that each contains everything necessary to execute only one aspect of the desired functionality.


--

# Modular Python

Most of the functionality in Python is provided by modules

The ***Python Standard Library*** is in fact a large collection of modules:

* *cross-platform* implementations of common facilities
* e.g. access to the operating system, file I/O, string management, network communication.

--

# Modular Levels

Python supports modular programming at many levels. 

* Containers and Functions, low-level
* Classes, low-level 
* Python *modules*, higher-level
* modules group related data, functions, and classes together in a `my_module.py`.
* The module file contents may be added to local scope with `import my_module`
* when imported, the module `file name` is used as a namespace providing access to all contents of the file.

--

# Contents of a module

* As an example, we will work with the module `random`
* the standard `random` module contains mathematical functions for pseudo-random numbers 
* Use a local copy `myrandom.py` of the file `random.py`, just in case. 
* The file is about 750 lines long.
* examine the source file in an editor/IDE that provides syntax highlighting.

--

# Exercise: Locate and Copy

Find where the `random` module file is installed and make a copy of it to the `src` directory in the tutorial file directory.

```python
import random
file_path = random.__file__
print(file_path)
```

--

# Modules as Objects

* A module is an object whose attributes & methods are stored in module file. 

* For instance, looking at the `myrandom` module's `__file__` attribute provides the path to the module file that contains all its code.


```python
print('The myrandom module is in the file %s' % \
       myrandom.__file__)
```


--

# Modules as Namespaces

To import the module `myrandom`:


```python
import src.myrandom as myrandom
```

Once the module `myrandom` is imported from the local file `myrandom.py`, we can list the "symbols" it provides using the built-in `dir()` function:


```python
for name in dir(myrandom):
    print(name)

print(len(dir(myrandom)))
```

--

## Docstrings in Modules

* The module file `myrandom.py` begins with a *docstring* at the very beginning of the file (lines 1 through 37). This is the text that appears in an interactive IPython session on typing `?myrandom`.

```python
"""Random variable generators.

    integers
    --------
           uniform within range

 # Lines deleted...
 
 General notes on the underlying Mersenne Twister core generator:

* The period is 2**19937-1.
* It is one of the most extensively tested generators in existence.
* The random() method is implemented in C, executes in a single Python step,
  and is, therefore, threadsafe.

"""
```

* Typing `help(myrandom)` prints out out the module docstring followed by the class docstring and the function docstring for every class and function in the module.

--

## Imports in modules

* After the module docstring, the module file `myrandom.py` imports a few modules (lines 39 through 45). 
* That is, modules can import other modules. It is customary to put imports of other modules near the top of a file for clarity.

```python
from warnings import warn as _warn
from types import MethodType as _MethodType, BuiltinMethodType as _BuiltinMethodType

# ... Lines deleted

from hashlib import sha512 as _sha512
```

--

## Data in Modules

* After the `import`s, a few constants are defined (lines 47 through 59) and a (private, hidden) module called `_random` is imported at line 66. 
* Once a module is imported its varibles are accessible by the Python interpreter.

```python
__all__ = ["Random","seed","random","uniform","randint","choice","sample",
           # ... Lines deleted
           "SystemRandom"]

NV_MAGICCONST = 4 * _exp(-0.5)/_sqrt(2.0)
TWOPI = 2.0*_pi
LOG4 = _log(4.0)

# ... Lines deleted
import _random
```

--

## Classes in Modules

* The classes `myrandom.Random` and `myrandom.SystemRandom` are defined in lines 68 through 635 and lines 639 through 668 respectively. 
* The class `myrandom.Random` provides the important methods in this module.

```python
class Random(_random.Random):
    """Random number generator base class used by bound module functions.

# Lines deleted
    """

    VERSION = 3     # used by getstate/setstate

# MANY lines deleted

## --------------- Operating System Random Source  ------------------

class SystemRandom(Random):
    """Alternate random number generator using sources provided
    by the operating system (such as /dev/urandom on Unix or
    CryptGenRandom on Windows).

     Not available on all systems (see os.urandom() for details).
    """
```

--

## Functions in Modules

* Between lines 672 and 710, there are two test functions `_test_generator` and `_test`.
* A single instance `_inst` is constructed of the class `random.Random` at line 718.
```python
_inst = Random()
```

* Between lines 719 and 739, various functions are assigned as aliases so that, for instance, the function `myrandom.uniform` is actually the method `myrandom._inst.uniform` from the object `myrandom._inst`

```python
seed = _inst.seed
random = _inst.random
uniform = _inst.uniform

# ... Lines deleted

getrandbits = _inst.getrandbits
```


--


# Script or Module?

Newcomers to Python can be confused by the terms "script file" and "module file". 

It is natural to ask, given a file containing Python code like `myrandom.py`, is it a script or a module? The answer is that it is *both*.

There are two ways to get the functions and classes stored in `myrandom.py` into a Python session. 

The one method we have seen already is to start a Python session (e.g., in a Jupyter/IPython notebook or a plain Python shell) and to *import* the module into the workspace. 

We have done this already and we can examine all the internal objects created in the file.


```python
import src.myrandom as myrandom # If already imported, no change is made.
print('myrandom.Log4 is %f.' % myrandom.LOG4)
print(type(myrandom._inst))  # Remember, myrandom._inst is an instance of class myrandom.Random
# All the functions in this module are in fact methods of this class instance
print(myrandom.uniform == myrandom._inst.uniform)
print(__name__)
```


--

# Import a Module

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

--

# Execute a Module

The second way to get all the objects described in the file `myrandom.py` into a Python session is to execute the file as a script. That is, from the command prompt of a shell, type

```bash
% python src/myrandom.py
```

just as we would do for running a Python script (assuming the file `myrandom.py` is in the working directory).

As the interpreter parses the file, all the imports, constant definitions, class definitions, and function definitions are executed as if entered at the Python command prompt. 

These lines are executed also when the module `myrandom` is imported into a Python session. 

--

# Dundar Name

The difference is in the very last two lines of the file `myrandom.py`:

```python
if __name__ == '__main__':
    _test()
```

When a Python file is imported (as a module) or executed (as a script), the Python interpreter sets a special identifier `__name__` that associates any objects created with a certain namespace. 

* If the file `myrandom.py` is *executed* (as a script) using "`python src/myrandom.py`",  the variable `__name__` is set to `'__main__'`.

* If the file `myrandom.py` is *imported* (as a module) using "`import src/myrandom`", the variable `__name__` is set to `'myrandom'`.

--

# Conditional Main

Thus, the last two lines of the file `myrandom.py` execute *only* when the file is run as a script, in which case, it executes the test code constucted in the function `_test()`. 

When imported as a module, the test "`__name__=='__main__'`" fails at the top of the `if` block and the `_test()` function is not executed.


```python
# This shell command executes myrandom.py and hence runs the _test() function.
!python src/myrandom.py 
```

More generally, importing a module from a file *`module.py`* assigns `__name__=`*`'module'`*. The idiom 

```python
if __name__ == "__main__:
    # Block of code to execute
    # when module runs as script
```

is widely used in module files to provide tests of the module's functions and classes. 

With this `if` block in place, the Python interpreter ignores the block of, say, test code when the module file is imported as a module, but runs the tests when the module file is executed as a script.

--

# Exercise: Creating a module

Having examined an actual module from the Python library, let's create our own module as an example. 

* Use a text editor to create a file `BankAccount.py` and add to it the following code block:

```python

'''BankAccount: This is the module docstring.'''

class BankAccount:   
    def __init__(self, account_ID, first_name, last_name, initial_balance):
        self._account_ID = account_ID
        self._first_name = first_name
        self._last_name = last_name
        self._balance = initial_balance

    def deposit(self, amount):
        '''BankAccount.deposit(amount) increases balance by amount'''
        try:
            if amount<=0:
                raise(ValueError('Expect positive amount!'))
            self._balance += amount
        except Exception as e:
            print(repr(e))

    def withdraw(self, amount):
        '''BankAccount.withdraw(amount) increases balance by amount'''
        try:
            if amount<=0:
                raise(ValueError('Expect positive amount!'))
            self._balance -= amount
        except Exception as e:
            print(repr(e))

    def account_status(self):
        out_string = "%s %s\tID: %s\tBalance: $%.2f" % \
                     (self._first_name, self._last_name, self._account_ID, self._balance)
        print(out_string)
```

* Execute the file as if it were a script
* Import the file as a module and use one of the functions

--

# Exercise: Modify a module

Before importing this module, let's append a test function and an `if` block as follows:

```python
if __name__=='__main__':
    print('BankAccount.py: executed as a script, running tests')
    _test_account()
    print('BankAccount.py: executed as a script, all tests passed')
else:
    print('BankAccount.py: imported as a module')
```

* Now add the test definition and place two `print` statements immediately before the `if` block, so those statements will always execute (i.e., regardless of whether the file is executed or imported).


```python
def _test_account():
    # Construct an account
    sophie_account = BankAccount('987654321', 'Sophie', 'Germaine', 1000.00)
    sophie_account.withdraw(150.00)
    # An assert statement is like an if-block that passes or throws an error
    assert sophie_account._balance == 850.00, 'Error in withdrawal function'
    sophie_account.deposit(375.00)
    assert sophie_account._balance == 1225.00, 'Error in deposit function'

print('All classes and function defined in module BankAccount')
print('__name__ == %s' % __name__)

if __name__=='__main__':
    print('BankAccount.py: executed as a script, running tests')
    _test_account()
    print('BankAccount.py: executed as a script, all tests passed')
else:
    print('BankAccount.py: imported as a module')
```

Finally, test the module by importing it and by runnign it as a script:

```python
import src.BankAccount
```


```bash
$ python src/BankAccount.py
```

--

# Consensual privacy

There is a common saying in the Python community of "We're all adults here."  

The meaning of this is that Python enforces very few actual *restrictions* on how other users use your code; 

...instead, Python has *conventions* about the intended use of code based on names given to objects.  

Many of these conventions are described in [PEP8](https://www.python.org/dev/peps/pep-0008/#naming-conventions), which is generally an excellent document to study and internalize.

Some naming conventions concern the *type* of object being named.  

For example, we typically use names following this pattern:

```python
CONSTANT_VAL = 7.5
class CamelCase(object): ...
function lower_with_under(args): ...
class JustAintRightError(ValueError): ...
```

--

# Dunder names

A special purpose is indicated by names that have leading (and possibly trailing) underscores.  

Names that have both two leading and two trailing spaces are "magic" in the sense that a number of them are used internally to enable syntax sugar or special behaviors by the interpreter. 

These are often called by the nickname "dunder names (methods)." 

Some of these magic names operate at module scope, but most are methods of classes.  

For example:

```python
__all__ = ['names', 'to', 'provide', 'externally']

if __name__ == '__main__':
    "Code to run when used as script"
    
class MyThing(object):
    def __init__(self, more, args):
        "Things to do when creating an instance"
    def __getitem__(self, key):
        "How to respond to square brackets: MyThing()[something]"
        return "A value"
```

--

# Recommending visibility

Generally you will not create your own new dunder names, unless you are designing a framework or a low-level package.  

However, you *should* take good advantage of names that *lead* with a single or double underscore.  

Names that begin with a single underscore are implicity stated not to promise a consist API (or continued existence) over different versions of the code.  

I.e. you should try not to rely on the functionality provided with these names, but rather only on names starting with letters.  

The use of a leading double underscore states this non-promise even more strongly, and in the case of classes makes the name slightly harder to access at all.

--

# Visibility Example

Let us look at a few examples, first a very simple module.  Notice that this module does not use the special list `__all__` to override default import behavior.

```bash
% cat simple.py
public = 5
_private = 6
__secret = 7
```

When we import this module:

```python
>>> from simple import *  # Only import "public" names
>>> dir() 
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'public']

>>> from simple import _private, __secret
>>> _private, __secret  # We're all adults here
(6, 7)
```

Classes do slightly more in terms of "enforcing" privacy


```python
class Visibility(object):
    public = 5
    _private = 6
    __secret = 7
    
visibility = Visibility()
```


```python
# The official API of the class
visibility.public   
```


```python
# Part of the "private" implementation of the class
visibility._private
```


```python
# A name-mangled attribute that is slightly harder to access
visibility._Visibility__secret
```

# Re-importing a module 

One thing to be aware of while developing modules: for efficiency reasons, each module is only imported once per interpreter session. 

Thus, typing `import module` generally imports the objects defined in `module.py` only the first time only. 

If the file `module.py` is modified, to import the modified module, we must either restart the Python interpreter (thereby losing all data in the current session) or use the `reload` function from the `imp` module, i.e.,

```python
import imp
imp.reload(module)
```

# Building Packages 

* There's more details to constructing packages (with modules nested within modules). 
* The rules are all available in the
[Python Official Documentation on modules](https://docs.python.org/3/tutorial/modules.html).
* There is a description of how to create (sub-)package namespaces at [https://docs.python.org/3.4/tutorial/modules.html#packages](https://docs.python.org/3.4/tutorial/modules.html#packages).  

