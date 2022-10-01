from math import *

HEIGHT = 0.1
ANGLE = pi/6

base = HEIGHT/tan(ANGLE)
hypo = sqrt(base**2 + HEIGHT**2)

print (base, hypo)