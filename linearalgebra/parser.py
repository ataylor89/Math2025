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
