import math

# Let f(x) = sin(x)
# Since f(x) is an infinitely differentiable function, we can form a Taylor series for sin(x).
# We will center our Taylor series at a=0.
# In order to form the Taylor series, we need to calculate the 1st, 2nd, and 3rd derivatives of sin(x)
# We will do that now
#
# f(x) = sin(x)
# f'(x) = cos(x)
# f''(x) = -sin(x)
# f'''(x) = -cos(x)
# f''''(x) = sin(x)
#
# Since our Taylor series will be centered at a=0, we need to know the value of the derivatives at x=0
#
# f(0) = 0
# f'(0) = 1
# f''(0) = 0
# f'''(0) = -1
# f''''(0) = 0
#
# The Taylor series for an infinitely differentiable function f(x), centered at a, is given by
# P(x) = f(a) + f'(a)*(x-a) + f''(a)*(x-a)^2/2! + f'''(a)*(x-a)^3/3! + ...
#
# The Taylor series for sin(x) centered at a=0 is given by
#
# P(x) = 0 + 1*x + 0 + -1*x^3/3! + ...
# P(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
#
# We can use this series to approximate sin(x).

def sin(x):
    lb = 0
    ub = 0
    # n should be a multiple of 4
    # We are using a degree n polynomial for the lb and a degree (n+1) polynomial for the ub
    n = 16
    for i in range(0, n+2):
        if i % 2 == 0:
            continue
        term = x**i / math.factorial(i)
        if i % 4 == 1:
            if i < n+1:
                lb += term
            ub += term
        if i % 4 == 3:
            lb -= term
            ub -= term
    return (lb, ub)

bounds = sin(1)
print("sin(1rad) is between %.15f and %.15f" %(bounds[0], bounds[1]))
