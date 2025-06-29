import primetable
import util
import math
import random
import sys

KEY_LEN = 1
ERROR_MSG = "Usage: python keygen.py"

kmin = 10**2
kmax = 10**3

test_file = "test.txt"

def gen_keys():
    keys = []
    primetable.load("primetable.pickle")
    while len(keys) < KEY_LEN:
        p = primetable.get(random.randint(kmin,kmax))
        q = primetable.get(random.randint(kmin,kmax))
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
        encrypted.append(util.power_mod_m(bytes[i], e, n))

    decrypted = []
    for i in range(0, len(bytes)):
        decrypted.append(util.power_mod_m(encrypted[i], d, n))
    
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
