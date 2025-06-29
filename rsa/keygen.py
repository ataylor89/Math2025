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
    for e in range(2, phi):
        if primes.gcd(e, phi) == 1:
            break
    #print("e = %d" %e)

    d = 0
    for d in range(2, phi):
        if (e * d) % phi == 1:
            break
    #print("d = %d" %d)

    return (n, e, d)

def main():
    (n, e, d) = gen_keys()
    with open("publickey.txt", "w") as file:
        file.write("n=%d e=%d" %(n, e))
    with open("privatekey.txt", "w") as file:
        file.write("n=%d d=%d" %(n, d))

if __name__ == "__main__":
    main()
