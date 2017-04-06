# Eratosthenes measures the radius of the Earth
# All lengths measured in meters
from __future__ import print_function
import math

# measure lengths shadow & stick, get angle
stick = 1.8
shadow = 0.23
rad2deg = 180.0/math.pi
angle = math.atan(shadow/stick)*rad2deg
print("shdow angle = ", angle)

# walk from Alexandria to Syene
step = 2
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
