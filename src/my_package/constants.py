print("Welcome to the constants.py module, revision 2")

import math

E = 2.7182899999999
PI = 3.14159

def compute_pi():
    return 4.0*math.atan(1.0)

def compute_e(num_terms=10):
    sum = 0
    for n in range(num_terms):
        sum += 1/math.factorial(n)
    return sum

def print_const(x):
    print("The value of your constant is ", x)
    return None
