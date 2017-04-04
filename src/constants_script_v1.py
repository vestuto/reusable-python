print( "Start of script." )
# This is an example script you might
# write to test some ideas
# It is not well organized
# It is intended only to be run from the shell

import math

# Assumed values for E and PI
E = 2.7182899999999
PI = 3.14159

# Compute PI
PI2 = 4.0*math.atan(1.0)

# Compute E
num_terms=10
sum = 0
for n in range(num_terms):
    sum += 1/math.factorial(n)
E2 = sum

# Report results
print( "Error in E calculation is ", abs(E2-E))
print( "Error in E calculation is ", abs(PI2-PI))

print( "End of script." )
