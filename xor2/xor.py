import sys

ERROR_USER_INPUT = "Usage: python xor.py <key> <path_to_file>"
ERROR_KEYSIZE = "The key has to be the same size as the message."

def crypt(key, msg):
    filesize = len(msg)

    keybytes = list(map(lambda x: ord(x), key))
    msgbytes = list(map(lambda x: ord(x), msg))

    out = [chr(msgbytes[i] ^ keybytes[i]) for i in range(0, filesize)]
    return ''.join(out)

def main():
    if len(sys.argv) != 3:
        print(ERROR_USER_INPUT)
        sys.exit(0)
    
    keyfile = open(sys.argv[1], "r")
    key = keyfile.read()

    msgfile = open(sys.argv[2], "r")
    msg = msgfile.read()

    if len(key) != len(msg):
        print(ERROR_KEYSIZE)
        sys.exit(0)

    print(crypt(key, msg), end='')
    
if __name__ == "__main__":
    main()
