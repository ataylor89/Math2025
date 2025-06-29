import parser
import util
import pickle
import sys

ERROR_USER_INPUT = "Usage: python encrypt.py <msg>"

def encrypt(msg, key):
    bytes = list(map(lambda x: ord(x), msg))
    keylen = len(key)
    cipher = []
    for i in range(0, len(bytes)):
        (n, e) = key[i % keylen]
        cipher.append(util.power_mod_m(bytes[i], e, n))
        #cipher.append(bytes[i]**e % n)
        #res = 1
        #for j in range(0, e):
            #res = (res * bytes[i]) % n
        #cipher.append(res)
    return cipher

def main():
    if len(sys.argv) != 2: 
        print(ERROR_USER_INPUT)
        sys.exit(0)

    msgfile = open(sys.argv[1], "r")
    msg = msgfile.read()

    key = parser.parse_key("publickey.txt")
    cipher = encrypt(msg, key)

    cipherfile = open("cipher.txt", "wb")
    pickle.dump(cipher, cipherfile)

if __name__ == "__main__":
    main()
