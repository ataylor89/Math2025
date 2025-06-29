import sys

ERROR_USER_INPUT = "Usage: python xor.py <msg>"

def crypt(msg, key):
    msglen = len(msg)
    keylen = len(key)

    msgbytes = list(map(lambda x: ord(x), msg))
    keybytes = list(map(lambda x: ord(x), key))

    out = [chr(msgbytes[i] ^ keybytes[i % keylen]) for i in range(0, msglen)]
    return ''.join(out)

def main():
    if len(sys.argv) != 2:
        print(ERROR_USER_INPUT)
        sys.exit(0)

    msgfile = open(sys.argv[1], "r")
    msg = msgfile.read()

    keyfile = open("key.txt", "r")
    key = keyfile.read()

    print(crypt(msg, key), end='')
    
if __name__ == "__main__":
    main()
