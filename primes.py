# We start with a sieve of size 100*n
#
# If that's not big enough to hold n primes, we will increase the sieve size, repeatedly,
# until it's big enough to hold the first n primes
#
# After we are sure that our sieve holds the first n primes, we extract every prime from the sieve,
# and we use list slicing (primes[0:n) to get the first n primes

import sys

ERROR_MSG = "Usage: python primes.py <n>"

def generate(n):
    size = 100 * n
    s = sieve(n, size)
    while s.count('P') < n:
        size *= 100
        s = sieve(n, size)
    primes = [i for i, j in enumerate(s) if j == 'P']
    return primes[0:n]

# A sieve separates the stuff we want to keep from the stuff we don't want to keep
# For example, the popular kitchen colander is a type of sieve
#
# This approach to generating primes is often called the "sieve of Eratosthenes"
# It tells us whether an integer is prime or composite, for all integers between 2 and size-1
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

# This is the main method, in which we read n as a command-line argument
#
# We validate the input, and make sure that there is only one command-line argument,
# and we make sure that the argument is a positive integer.
#
# After validating the input and obtaining n, we print the first n primes.
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

    primes = generate(n)
    print(primes)

if __name__ == "__main__":
    main()
