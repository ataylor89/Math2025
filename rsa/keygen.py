import primes
import math
import random
import sys

KEY_LEN = 256
ERROR_MSG = "Usage: python keygen.py"

kmin = 10
kmax = 20

test_files = ["test.txt"]
tests = []

def gen_keys():
    keys = []
    while len(keys) < KEY_LEN:
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

        if test(n, e, d):
            keys.append((n, e, d))
    return keys

def test(n, e, d):
    for msg in tests:
        bytes = list(map(lambda x: ord(x), msg))

        encrypted = []
        for i in range(0, len(bytes)):
            encrypted.append(bytes[i]**e % n)

        decrypted = []
        for i in range(0, len(bytes)):
            decrypted.append(encrypted[i]**d % n)

        if bytes != decrypted:
            return False
    return True

def main():
    if len(sys.argv) != 1:
        print(ERROR_MSG)
        sys.exit(0)

    for filename in test_files:
        file = open(filename, "r")
        message = file.read()
        tests.append(message)

    keys = gen_keys()

    with open("publickey.txt", "w") as file:
        for (n, e, d) in keys:
            file.write("n=%d e=%d\n" %(n, e))
    with open("privatekey.txt", "w") as file:
        for (n, e, d) in keys:
            file.write("n=%d d=%d\n" %(n, d))

if __name__ == "__main__":
    main()
