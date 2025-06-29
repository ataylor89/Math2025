import pickle
import sys
import os

ERROR_MSG = "Usage: python primetable.py <n>"
EXISTING_TABLE_SUFFICIENT = "The existing prime table is sufficient"

# Gets the nth prime from the prime table
def get(n):
    return table[n-1]

# Loads a prime table from a file
def load(path):
    global table

    file = open(path, "rb")
    table = pickle.load(file)

# Saves the prime table to a file
def save(path):
    if table:
        file = open(path, "wb")
        pickle.dump(table, file)

# Generates a prime table of size n
def generate(n):
    global table

    size = 100 * n
    s = _sieve(n, size)
    while s.count('P') < n:
        size *= 100
        s = _sieve(n, size)
    table = [i for i, j in enumerate(s) if j == 'P'][0:n]

# Helper function used to create our prime table
def _sieve(n, size):
    sieve = ['P'] * size
    sieve[0] = 'N'
    sieve[1] = 'N'
    for i in range(2, size):
        if sieve[i] == 'P':
            j = 2
            while i * j < size:
                sieve[i * j] = 'C'
                j += 1
    return sieve

def main():
    if len(sys.argv) != 2:    
        print(ERROR_MSG)
        sys.exit(0)

    try:
        n = int(sys.argv[1])
    except:
        print(ERROR_MSG)
        sys.exit(0)

    if n <= 0:
        print(ERROR_MSG)
        sys.exit(0)
 
    if os.path.exists("primetable.pickle"):
        load("primetable.pickle")
        if len(table) >= n:
            print(EXISTING_TABLE_SUFFICIENT)
            sys.exit(0)

    generate(n)
    save("primetable.pickle")

if __name__ == "__main__":
    main()
