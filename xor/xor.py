import sys

ERROR_MSG = "Usage: python xor.py <key> <path_to_file>"

def crypt(key, str):
    bytes = list(map(lambda x: ord(x) ^ key, str))
    return ''.join([chr(x) for x in bytes])

def is_binary(str):
    try:
        int(str, 2)
        return True
    except ValueError:
        return False

def is_decimal(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def is_hexadecimal(str):
    try:
        int(str, 16)
        return True
    except ValueError:
        return False

def is_valid(key):
    return isinstance(key, int) and key >= 0 and key <= 255

def main():
    if len(sys.argv) != 3:
        print(ERROR_MSG)
        sys.exit(0)
    
    key = sys.argv[1]
    
    if is_binary(key):
        key = int(key, 2)
    elif is_decimal(key):
        key = int(key)
    elif is_hexadecimal(key):
        key = int(key, 16)

    if not is_valid(key):
        print(ERROR_MSG)
        sys.exit(0)

    filename = sys.argv[2]

    with open(filename, "r") as file:
        content = file.read()
        print(crypt(key, content), end='')    

if __name__ == "__main__":
    main()
