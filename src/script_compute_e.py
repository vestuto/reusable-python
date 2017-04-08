print( "Start of script_compute_e.py" )

import math

E1 = 2.7182899999999

num_terms=10
sum = 0
for n in range(num_terms):
    sum += 1/math.factorial(n)
E2 = sum

print( "Error in E2 - E1 ", math.fabs(E2-E1))

print( "End of script_compute_e.py" )
