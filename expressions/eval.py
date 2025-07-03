import sys

error_msg = "Usage: python eval.py expression.txt"

operators = {'+', '-', '*', '/', '^'}

map = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
    '^': 2
}

def eval(expression):
    tokens = tokenize(expression)
    return _eval(tokens)

def tokenize(expression):
    str = ""
    for c in expression:
        if c == '(' or c == ')' or c in operators:
            str += " " + c + " "
        else:
            str += c
    return str.split()

def _eval(tokens):
    n = len(tokens)

    if n == 1:
        f = float(tokens[0])
        return int(f) if f.is_integer() else f

    index = 0
    level = 0
    highest_priority = -1

    for i in range(0, n):
        token = tokens[i]
        if token == '(':
            level += 1
        elif token== ')':
            level -= 1
        elif token in operators:
            priority = map[token] + 3*level
            if priority > highest_priority:
                highest_priority = priority
                index = i

    op1 = float(tokens[index-1])
    op2 = float(tokens[index+1])

    match tokens[index]:
        case '+':
            op1 = op1 + op2
        case '-':
            op1 = op1 - op2
        case '*':
            op1 = op1 * op2
        case '/':
            op1 = op1 / op2
        case '^':
            op1 = op1 ** op2

    tokens[index-1] = op1
    del tokens[index:index+2]

    if tokens[index-2] == '(' and tokens[index] == ')':
        del tokens[index]
        del tokens[index-2]

    return _eval(tokens)

def main():
    if len(sys.argv) != 2:
        print(error_msg)
        sys.exit(0)

    file = open(sys.argv[1], "r")
    expression = file.read()
    
    result = eval(expression)
    print(result)

if __name__ == "__main__":
    main()
