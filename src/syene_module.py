# Eratosthenes measures the radius of the Earth
# All lengths measured in meters
from __future__ import print_function
import math

def get_angle():
    """
    Purpose: measure lengths shadow & stick, get angle
    """
    stick = 1.8
    shadow = 0.23
    rad2deg = 180.0/math.pi 
    angle = math.atan(shadow/stick)*rad2deg
    print("shdow angle = ", angle)
    return angle

def get_travel():
    """
    Purpose: walk from Alexandria to Syene
    """
    step = 2
    counts = 395000
    travel = step * counts 
    print("travel distance = ", travel)
    return travel

def get_radius(angle, travel):
	"""
    Purpose:
        assume earth is a sphere
        use ratio of angles = ratio of lengths
    """
    circumference = travel * (360 / angle)
    radius = circumference / (2.0 * math.pi)
    print("estimated earth radius = ", radius)
    return radius

def get_error(radius):
	"""
	Purpose: Compute error in Earth radius estimation
	"""
	known_value = 6378137 
	error = 100 * math.fabs(known_value - radius) / known_value
	print("known value = ", known_value)
	print("error % = ", error)
	return error

def main():
	angle = get_angle()
	travel = get_travel()
	radius = get_radius(angle, travel)
	error = get_error(radius)


