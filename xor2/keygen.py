import random
import sys

ERROR_MSG = "Usage: python keygen.py <inputfile> <outputfile>"

def main():
    if len(sys.argv) != 3:
        print(ERROR_MSG)
        sys.exit(0)

    input_file = open(sys.argv[1], "r")
    content = input_file.read()
    filesize = len(content)
    
    key = [chr(random.randint(0, 255)) for i in range(0, filesize)]
    key = ''.join(key)

    output_file = open(sys.argv[2], "w")
    output_file.write(key)

if __name__ == "__main__":
    main()
