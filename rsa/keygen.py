import primes
import math
import random
import sys

KEY_LEN = 4
ERROR_MSG = "Usage: python keygen.py"

kmin = 1000
kmax = 2000

test_file = "test.txt"

def gen_keys():
    keys = []
    primes.init(kmax)
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
            print("Adding key (n=%d, e=%d, d=%d)" %(n, e, d))
            keys.append((n, e, d))
    return keys

def test(n, e, d):
    bytes = list(map(lambda x: ord(x), test_message))

    encrypted = []
    for i in range(0, len(bytes)):
        res = 1
        for j in range(0, e):
            res = (res * bytes[i]) % n
        encrypted.append(res)

    decrypted = []
    for i in range(0, len(bytes)):
        res = 1
        for j in range(0, d):
            res = (res * encrypted[i]) % n
        decrypted.append(res)
    
    return bytes == decrypted

def main():
    if len(sys.argv) != 1:
        print(ERROR_MSG)
        sys.exit(0)

    file = open(test_file, "r")

    global test_message
    test_message = file.read()

    keys = gen_keys()

    with open("publickey.txt", "w") as file:
        for (n, e, d) in keys:
            file.write("n=%d e=%d\n" %(n, e))
    
    with open("privatekey.txt", "w") as file:
        for (n, e, d) in keys:
            file.write("n=%d d=%d\n" %(n, d))

if __name__ == "__main__":
    main()
