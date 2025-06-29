def parse_keys(path):
    file = open(path, "r")
    content = file.read()
    tokens = content.split()
    n = int(tokens[0][2:])
    e = int(tokens[1][2:])
    d = int(tokens[2][2:])
    return (n, e, d)
