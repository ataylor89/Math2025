import sys

ERROR_USER_INPUT = "Usage: python xor.py <msgfile> <keyfile>"
ERROR_KEYSIZE = "The key has to be the same size as the message."

def crypt(msg, key):
    filesize = len(msg)

    msgbytes = list(map(lambda x: ord(x), msg))
    keybytes = list(map(lambda x: ord(x), key))

    out = [chr(msgbytes[i] ^ keybytes[i]) for i in range(0, filesize)]
    return ''.join(out)

def main():
    if len(sys.argv) != 3:
        print(ERROR_USER_INPUT)
        sys.exit(0)

    msgfile = open(sys.argv[1], "r")
    msg = msgfile.read()

    keyfile = open(sys.argv[2], "r")
    key = keyfile.read()

    if len(msg) != len(key):
        print(ERROR_KEYSIZE)
        sys.exit(0)

    print(crypt(msg, key), end='')
    
if __name__ == "__main__":
    main()
