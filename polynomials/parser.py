class ParseTree:
    def __init__(self, degree, coefficients):
        self.degree = degree
        self.coefficients = coefficients

class Parser:
    def parse(self, line):
        try:
            return self._parse(line)
        except:
            raise ValueError("The polynomial does not match the required format.")

    def _parse(self, line):
        coefficients = {}
        sign = 1
        tokens = line.split()
        for token in tokens:
            if token == "+":
                sign = 1
            elif token == "-":
                sign = -1
            elif token.startswith("x^"):
                coefficient = sign
                power = int(token[2:])
                if power in coefficients:
                    coefficients[power] += coefficient
                else:
                    coefficients[power] = coefficient
            elif token.startswith("-x^"):
                coefficient = sign * -1
                power = int(token[3:])
                if power in coefficients:
                    coefficients[power] += coefficient
                else:
                    coefficients[power] = coefficient
            elif "x^" in token:
                parts = token.split("x^")
                coefficient = sign * float(parts[0])
                power = int(parts[1])
                if power in coefficients:
                    coefficients[power] += coefficient
                else:
                    coefficients[power] = coefficient
            elif token == "x":
                coefficient = sign
                power = 1
                if power in coefficients:
                    coefficients[power] += coefficient
                else:
                    coefficients[power] = coefficient
            elif token == "-x":
                coefficient = sign * -1
                power = 1
                if power in coefficients:
                    coefficients[power] += coefficient
                else:
                    coefficients[power] = coefficient
            elif token.endswith("x"):
                coefficient = sign * float(token[:-1])
                power = 1
                if power in coefficients:
                    coefficients[power] += coefficient
                else:
                    coefficients[power] = coefficient
            else:
                coefficient = sign * float(token)
                power = 0
                if power in coefficients:
                    coefficients[power] += coefficient
                else:
                    coefficients[power] = coefficient
            degree = max(coefficients.keys())
            for i in range(0, degree+1):
                if i not in coefficients:
                    coefficients[i] = 0
        return ParseTree(degree, coefficients)
