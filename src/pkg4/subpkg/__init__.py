"""
This is a docstring for the subpkg directory
"""
print("Hello from the pkg2.subpkg.__init__.py")

count = {}
count[0] = 1
count[1] = 10
count[2] = 100

def talk():
    message = "Hello again and welcome to the subpkg"
    print(message)
    return message

talk()
from . import mod3
