def numbytes(n):
    k = 1
    while 256**k - 1 < n:
        k += 1
    return k

def to_string(n):
    str = ""
    k = numbytes(n)
    for i in range(0, k):
        bitmask = 0xFF << (8 * (k - i - 1))
        str += chr((n & bitmask) >> (8 * (k - i - 1)))
    return str

def to_number(str):
    n = 0
    k = len(str)
    for i in range(0, k):
        n += ord(str[i]) << (8 * (k - i - 1))
    return n

#n = 123456
#print("n = %d" %n)

#k = numbytes(n)
#print("k = %d" %k)

#s = to_string(n)
#print(s)
#n = to_number(s)
#print(n)
