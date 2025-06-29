def parse_key(path):
    file = open(path, "r")
    content = file.read()
    tokens = content.split()
    return (int(tokens[0][2:]), int(tokens[1][2:]))
