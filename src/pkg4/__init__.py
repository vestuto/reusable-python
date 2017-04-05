"""
HERE IS A DOCSTRING THAT SCREAMS FROM PKG2
"""

print("Hello from the pkg2.__init__.py")
from . import mod1
from . import mod2
# from . import subpkg
from .subpkg import mod3
del subpkg

__all__=['mod1','mod2','mod3'] # "from pkg2 import *"
