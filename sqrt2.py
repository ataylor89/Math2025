# We are going to approximate sqrt(2) by using the following continued fraction:
#
# sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ...)))
#
# We can truncate the continued fraction to get a lower bound and an upper bound for sqrt(2).
#
# For example, 1 is a lower bound for sqrt(2), and 1 + 1/2 is an upper bound for sqrt(2).
#
# We will use a recursive function to truncate the continued fraction and form the approximations.

def approximate_sqrt2(n):
    return _approximate_sqrt2(n, 0)

def _approximate_sqrt2(n, partial):
    if n <= 0:
        return 1 + partial
    return _approximate_sqrt2(n-1, 1/(2 + partial))

lb = approximate_sqrt2(100)
ub = approximate_sqrt2(101)
print("The square root of 2 is between %.15f and %.15f" %(lb, ub))
