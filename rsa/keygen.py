import keytable
import random
import sys

key_len = 4
threshold = 10**6
error_msg = "Usage: python keygen.py"

def gen_keys():
    keytable.generate(key_len, threshold)
    nvalues = list(keytable.table['table'].keys())
    nvalues = random.sample(nvalues, key_len)
    keys = []
    for nvalue in nvalues:
        (n, p, q, phi, e, d) = keytable.table['table'][nvalue]
        keys.append((n, e, d))
    return keys

def main():
    if len(sys.argv) != 1:
        print(error_msg)
        sys.exit(0)

    keys = gen_keys()

    with open("publickey.txt", "w") as file:
        for (n, e, d) in keys:
            file.write("n=%d e=%d\n" %(n, e))
    
    with open("privatekey.txt", "w") as file:
        for (n, e, d) in keys:
            file.write("n=%d d=%d\n" %(n, d))

if __name__ == "__main__":
    main()
