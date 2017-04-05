"""
This is a docstring for the file mod4.py
Not imported from the init file!
"""
print("Hello from the pkg2.subpkg.mod4.py")

pie = 3.14159
radius = 0.10 # radius of pie in meters

def crust(r=radius):
	"""
	Purpose:
	    This is a function to compute pie crust
    Usage:
        area = crust(radius) where lengths are in meters
	"""
	area = 2*pie*r*r
	return area

