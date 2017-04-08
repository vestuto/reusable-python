print( "Start of script_constants.py" )

import math

# Assumed values for E and PI
E1 = 2.7182899999999
PI1 = 3.14159

# Compute PI
PI2 = 4.0*math.atan(1.0)

# Compute E
num_terms=10
sum = 0
for n in range(num_terms):
    sum += 1/math.factorial(n)
E2 = sum

# Report results
print( "Error in E2 - E1 = ", math.fabs(E2-E1))
print( "Error in P2 - P1 = ", math.fabs(PI2-PI1))

print( "End of script_constants.py" )
