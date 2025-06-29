import parser
import pickle
import sys

ERROR_USER_INPUT = "Usage: python encrypt.py <msg> [key]"

def encrypt(msg, key):
    bytes = list(map(lambda x: ord(x), msg))
    keylen = len(key)
    cipher = []
    for i in range(0, len(bytes)):
        (n, e) = key[i % keylen]
        cipher.append(bytes[i]**e % n)
    return cipher

def main():
    argc = len(sys.argv)

    if argc < 2 or argc > 3:
        print(ERROR_USER_INPUT)
        sys.exit(0)

    msgfile = open(sys.argv[1], "r")
    msg = msgfile.read()

    path = "publickey.txt" if argc == 2 else sys.argv[2]

    key = parser.parse_key(path)
    cipher = encrypt(msg, key)

    cipherfile = open("cipher.txt", "wb")
    pickle.dump(cipher, cipherfile)

if __name__ == "__main__":
    main()
