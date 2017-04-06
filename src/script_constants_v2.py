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

if __name__ == "__main__":
	"""If imported, this block will not execute"""
	
    print( "Start of script." )

    E2 = compute_e()
    print( "Error in E calculation is ", abs(E2-E))
  
    PI2 = compute_pi()
    print( "Error in E calculation is ", abs(PI2-PI))

    print( "End of script." )
