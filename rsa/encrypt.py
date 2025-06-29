import parser
import util
import sys

ERROR_MSG = "Usage: python encrypt.py <msg> <n> <e>"

def encrypt(msg, n, e):
    bytes = list(map(lambda x: ord(x), msg))
    crypt = list(map(lambda x: x**e % n, bytes))
    k = util.numbytes(n)
    return ''.join([util.to_string(x, k) for x in crypt])

def main():
    if len(sys.argv) != 3:
        print(ERROR_MSG)
        sys.exit(0)

    msgfile = open(sys.argv[1], "r")
    msg = msgfile.read()
    (n, e) = parser.parse_key(sys.argv[2])
    cipher = encrypt(msg, n, e)
    print(cipher, end='')

if __name__ == "__main__":
    main()
