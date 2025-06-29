import random
import sys

KEY_LEN = 1024
ERROR_MSG = "Usage: python keygen.py [outputfile]"

def gen_key():
    key = [chr(random.randint(0, 255)) for i in range(0, KEY_LEN)]
    return ''.join(key)

def main():
    argc = len(sys.argv)

    if argc > 2:
        print(ERROR_MSG)
        sys.exit(0)

    key = gen_key()
    
    path = "key.txt" if argc == 1 else sys.argv[1]     
    file = open(path, "w")
    file.write(key)

if __name__ == "__main__":
    main()
