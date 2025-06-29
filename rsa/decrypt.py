import parser
import pickle
import sys

ERROR_USER_INPUT = "Usage: python decrypt.py <msg> [key]"

def decrypt(cipher, key):
    msg = ""
    keylen = len(key)
    for i in range(0, len(cipher)):
        (n, d) = key[i % keylen]
        m = cipher[i]**d % n
        msg += chr(m)
    return msg

def main():
    argc = len(sys.argv)

    if argc < 2 or argc > 3:
        print(ERROR_USER_INPUT)
        sys.exit(0)

    cipherfile = open(sys.argv[1], "rb")
    cipher = pickle.load(cipherfile)

    path = "privatekey.txt" if argc == 2 else sys.argv[2]
    key = parser.parse_key(path)

    msg = decrypt(cipher, key)
    print(msg, end='')

if __name__ == "__main__":
    main()
