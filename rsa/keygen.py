import primes
import math
import random
import sys

ERROR_MSG = "Usage: python keygen.py <msg>"

kmin = 10
kmax = 20

def gen_keys(msg):
    keys = []
    while len(keys) < 256:
        p = primes.nthprime(random.randint(kmin,kmax))
        q = primes.nthprime(random.randint(kmin,kmax))
        n = p * q
        phi = math.lcm(p-1,q-1)

        e = 0
        for e in range(2, phi):
            if math.gcd(e, phi) == 1:
                break

        d = 0
        for d in range(2, phi):
            if (d * e) % phi == 1:
                break

        if test(msg, n, e, d):
            keys.append((n, e, d))
    return keys

def test(msg, n, e, d):
    bytes = list(map(lambda x: ord(x), msg))

    encrypted = []
    for i in range(0, len(bytes)):
        encrypted.append(bytes[i]**e % n)

    decrypted = []
    for i in range(0, len(bytes)):
        decrypted.append(encrypted[i]**d % n)

    return bytes == decrypted

def main():
    if len(sys.argv) != 2:
        print(ERROR_MSG)
        sys.exit(0)

    msgfile = open(sys.argv[1], "r")

    msg = msgfile.read()
    keys = gen_keys(msg)

    with open("publickey.txt", "w") as file:
        for (n, e, d) in keys:
            file.write("n=%d e=%d\n" %(n, e))
    with open("privatekey.txt", "w") as file:
        for (n, e, d) in keys:
            file.write("n=%d d=%d\n" %(n, d))

if __name__ == "__main__":
    main()
