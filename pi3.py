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
