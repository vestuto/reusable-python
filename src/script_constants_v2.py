print( "Start of module-like section." )

import math

def compute_pi():
    pi = 4.0*math.atan(1.0)
    return pi

def compute_e(num_terms=10):
    e_sum = 0
    for n in range(num_terms):
        e_sum += 1/math.factorial(n)
    e = e_sum
    return e

def compute_error(val1, val2, name):
    error = math.fabs(val2 - val1)
    template = "The error in {name}2 - {name}1 = {err}"
    message = template.format(name=name, err=error)
    print( message )
    return error

print( "End of module-like section." )

if __name__ == "__main__":	
    print( "Start of script." )

    E1 = 2.7182899999999
    PI1 = 3.14159

    E2 = compute_e()
    PI2 = compute_pi()

    E_error = compute_error(E1, E2, "E")
    PI_error = compute_error(PI1, PI2, "PI")

    print( "End of script." )
