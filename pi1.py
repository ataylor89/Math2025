# We use the Taylor series for arctan(1) centered at a=0 to approximate Pi
#
# In other words, we use the equation Pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... to approximate Pi.
#
# We arrive at this equation by plugging x=1 into the Taylor series for arctan(x) centered at a=0
#
# This is an easy way to approximate Pi... it's hard to derive the equation, but easy to use the equation.
#
# We approximate Pi by generating a lower bound and an upper bound. Pi is somewhere between the two bounds.

def approximate_pi(n):
    result = 0
    for i in range(0, n):
        if i % 2 == 0:
            result += 1/(2*i + 1)
        else:
            result -= 1/(2*i + 1)
    result *= 4
    return result

n = 10**6
lb = approximate_pi(n)
ub = approximate_pi(n+1)
print("Pi is between %.10f and %.10f" %(lb, ub))
