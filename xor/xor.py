import sys

ERROR_USER_INPUT = "Usage: python xor.py <msg> [key]"

def crypt(msg, key):
    msglen = len(msg)
    keylen = len(key)

    msgbytes = list(map(lambda x: ord(x), msg))
    keybytes = list(map(lambda x: ord(x), key))

    out = [chr(msgbytes[i] ^ keybytes[i % keylen]) for i in range(0, msglen)]
    return ''.join(out)

def main():
    argc = len(sys.argv)

    if argc < 2 or argc > 3:
        print(ERROR_USER_INPUT)
        sys.exit(0)

    msgfile = open(sys.argv[1], "r")
    msg = msgfile.read()

    path = "key.txt" if argc == 2 else sys.argv[2]

    keyfile = open(path, "r")
    key = keyfile.read()

    print(crypt(msg, key), end='')
    
if __name__ == "__main__":
    main()
