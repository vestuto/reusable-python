print( "Start of script_compute_pi.py" )

import math

PI0 = math.pi
PI1 = 3.14159
PI2 = 4.0*math.atan(1.0)

print( "Error PI2 - PI1 ", math.fabs(PI2-PI1))
print( "Error PI2 - PI0 ", math.fabs(PI2-PI0))

print( "End of script_compute_pi.py" )