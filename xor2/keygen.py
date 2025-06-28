import random
import sys

ERROR_MSG = "Usage: python keygen.py <msgfile> <keyfile>"

def main():
    if len(sys.argv) != 3:
        print(ERROR_MSG)
        sys.exit(0)

    msgfile = open(sys.argv[1], "r")
    msg = msgfile.read()
    msglen = len(msg)
    
    key = [chr(random.randint(0, 255)) for i in range(0, msglen)]
    key = ''.join(key)

    keyfile = open(sys.argv[2], "w")
    keyfile.write(key)

if __name__ == "__main__":
    main()
