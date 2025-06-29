import parser
import util
import sys

ERROR_MSG = "Usage: python decrypt.py <msg> <n> <d>"

def decrypt(cipher, n, d):
    blocksize = util.numbytes(n)
    numblocks = int(len(cipher) / blocksize)
    str = ""
    for i in range(0, numblocks):
        block = cipher[i*blocksize:(i+1)*blocksize]
        num = util.to_number(block)
        str += chr(num**d % n)
    return str

def main():
    if len(sys.argv) != 3:
        print(ERROR_MSG)
        sys.exit(0)

    cipherfile = open(sys.argv[1], "r")
    cipher = cipherfile.read()
    (n, d) = parser.parse_key(sys.argv[2])
    msg = decrypt(cipher, n, d)
    print(msg, end='')

if __name__ == "__main__":
    main()
