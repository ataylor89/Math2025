import random
import sys

KEY_LEN = 1024
ERROR_MSG = "Usage: python keygen.py"

def gen_key():
    key = [chr(random.randint(0, 255)) for i in range(0, KEY_LEN)]
    return ''.join(key)

def main():
    if len(sys.argv) != 1:
        print(ERROR_MSG)
        sys.exit(0)

    key = gen_key()
    file = open("key.txt", "w")
    file.write(key)

if __name__ == "__main__":
    main()
