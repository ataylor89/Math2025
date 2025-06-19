# In this program, we approximate Pi using the Archimedes algorithm.
#
# Let a[n] be the circumference of a regular n-gon that circumscribes the unit circle.
# Let b[n] be the circumference of a regular n-gon that inscribes the unit circle.
#
# b[n]/2 is a lower bound for Pi, and a[n]/2 is an upper bound for Pi
#
# We can get a better and better approximation for Pi using the following recurrence formula:
#
# a[2n] = 2*a[n]*b[n]/(a[n] + b[n])
# b[2n] = sqrt(a[2n] * b[n])
#
# It is very hard to derive the recurrence formula, but once you have it, you can use it to approximate Pi.
#
# The Archimedes Algorithm uses the recurrence formula, repeatedly, to get a good approximation of Pi.
#
# The recurrence formula gives us a lower bound and an upper bound for 2Pi.
#
# We can divide these bounds by 2 to get a lower bound and an upper bound for Pi.

import math

def approximate_pi(n):
    a = 3*2*math.sqrt(3)/3
    b = 3
    return _approximate_pi(n, a, b)

def _approximate_pi(n, a, b):
    if n <= 0:
        return (b, a)
    a2 = 2*a*b/(a + b)
    b2 = math.sqrt(a2 * b)
    return _approximate_pi(n-1, a2, b2)

bounds = approximate_pi(10)
print("Pi is between %.10f and %.10f" %(bounds[0], bounds[1]))
