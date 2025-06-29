import primes
import random

nmin = 1
nmax = 50

def gen_keys():
    p = primes.nthprime(random.randint(nmin,nmax))
    q = primes.nthprime(random.randint(nmin,nmax))
    n = p * q
    phi = (p-1)*(q-1)

    #print("p = %d" %p)
    #print("q = %d" %q)
    #print("n = %d" %n)
    #print("phi = %d" %phi)

    e = 0
    for i in range(2, phi):
        if primes.gcd(i, phi) == 1:
            e = i
            break
    #print("e = %d" %e)

    d = 0
    for i in range(2, phi):
        if (e * i) % phi == 1:
            d = i
            break
    #print("d = %d" %d)

    return (n, e, d)

def main():
    keys = gen_keys()
    print("n=%d e=%d d=%d" %(keys[0], keys[1], keys[2]))

if __name__ == "__main__":
    main()
