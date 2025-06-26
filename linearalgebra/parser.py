# My family taught me that a parser breaks down a sentence into parts.
# A parser can also break down a file into parts.
#
# The code in this module parses an input file.
# The input file contains a system of linear equations.
#
# After parsing the file, it returns a parse tree.
# The parse tree contains the coefficients matrix, the variables, and the constants.
#
# We can use the results from the parse tree, in conjunction with numpy, to solve the system of linear equations.
# We do that in a separate file called linearalgebra.py.
#
# It is worth pointing out, that after we read a line from a file, we have to tokenize the line.
# String tokenization means breaking down a sentence into words.
# 
# We tokenize each line using whitespace as our delimiter.
# String tokenization is a specific form of parsing (breaking down a complex whole into parts).
#
# Parsing is useful for many things.
# When we write a compiler, an interpreter, or an assembler, we have to parse the source code.
# We have to parse each line, and make sense of it.
# We have to process each token, and make sense of each token.
#
# For example, if we parse the following line of assembly code
#   mov eax, 0x12345678
#
# We can say that the instruction type is "mov"
# We can say that the first operand is eax
# We can say that the first operand is a register
# We can say that the second operand is 0x12345678
# We can say that the second operand is a number
#
# I tried writing an assembler a long time ago, and it was hard
# But it was also a task that involved parsing
#
# My family taught me that a parser breaks down a sentence into parts, or a file into parts
# This project helps us understand the importance of parsing
#
# We put the parsing code in its own module so that the project is well-organized
# It also allows us to test the parser as a standalone module

class ParseTree:
    def __init__(self, coefficients, variables, constants):
        self.coefficients = coefficients
        self.variables = variables
        self.constants = constants

class Parser:
    def parse(self, filename):
        try:
            return self._parse(filename)
        except FileNotFoundError:
            print("The file %s was not found" %filename)

    def _parse(self, filename):
        coefficients = []
        variables = []
        constants = []
        for line in open(filename, "r"):
            on_left = True
            sign = 1
            row_coeffs = []
            tokens = line.split()
            for token in tokens:
                if token == '+':
                    sign = 1
                elif token == '-':
                    sign = -1
                elif token == '=':
                    on_left = False
                elif on_left:
                    coefficient = sign if len(token) == 1 else sign * int(token[:-1])
                    row_coeffs.append(coefficient)
                    variable = token[-1]
                    if variable not in variables:
                        variables.append(variable)
                else:
                    constants.append(int(token))
            coefficients.append(row_coeffs)
        return ParseTree(coefficients, variables, constants)
