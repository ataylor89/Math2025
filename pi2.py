import math

def approximate_pi(n):
    lb = 0
    ub = 0
    for i in range(0, n):
        x1 = i/n
        y1 = math.sqrt(1 - x1**2)
        ub += y1/n
        x2 = (i+1)/n
        y2 = math.sqrt(1 - x2**2)
        lb += y2/n
    lb *= 4
    ub *= 4 
    return (lb, ub)

bounds = approximate_pi(10**6)
print("Pi is between %.10f and %.10f" %(bounds[0], bounds[1]))
