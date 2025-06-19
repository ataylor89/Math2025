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
