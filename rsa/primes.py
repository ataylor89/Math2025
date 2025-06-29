import sys

ERROR_MSG = "Usage: python primes.py <n>"

def nthprime(n):
    primes = generate(n)
    return primes[n-1]

def generate(n):
    size = 100 * n
    s = sieve(n, size)
    while s.count('P') < n:
        size *= 100
        s = sieve(n, size)
    primes = [i for i, j in enumerate(s) if j == 'P']
    return primes[0:n]

def sieve(n, size):
    sieve = ['P'] * size
    sieve[0] = 'N'
    sieve[1] = 'N'
    for i in range(2, size):
        if sieve[i] == 'P':
            j = 2
            while i * j < size:
                sieve[i * j] = 'C'
                j += 1
    return sieve

def main():
    if len(sys.argv) != 2:    
        print(ERROR_MSG)
        sys.exit(0)

    try:
        n = int(sys.argv[1])
    except:
        print(ERROR_MSG)
        sys.exit(0)

    if n <= 0:
        print(ERROR_MSG)
        sys.exit(0)
 
    print(nthprime(n))
    #print(generate(n))

if __name__ == "__main__":
    main()
