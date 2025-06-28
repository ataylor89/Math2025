from polynomials import Polynomial
from complexnumbers import ComplexNumber

import math
import sys

ERROR_MSG = 'Example usage: python quadratic.py "3x^2 + 4x + 5"'

class Quadratic(Polynomial):
    def __init__(self, text):
        try: 
            super().__init__(text)
        except:
            print(ERROR_MSG)
            sys.exit(0)
        if self.degree != 2:
            print(ERROR_MSG)
            sys.exit(0)

    def solve(self):
        a = self.coefficients[2]
        b = self.coefficients[1]
        c = self.coefficients[0]
        if b**2 - 4*a*c >= 0:
            root1 = ComplexNumber((-b + math.sqrt(b**2 - 4*a*c))/(2*a), 0)
            root2 = ComplexNumber((-b - math.sqrt(b**2 - 4*a*c))/(2*a), 0)
        else:
            root1 = ComplexNumber(-b/(2*a), math.sqrt(-(b**2 - 4*a*c))/(2*a))
            root2 = ComplexNumber(-b/(2*a), -1*math.sqrt(-(b**2 - 4*a*c))/(2*a))
        return (root1, root2)

def main():
    if len(sys.argv) != 2:
        print(ERROR_MSG)
        sys.exit(0)

    q = Quadratic(sys.argv[1])
    solutions = q.solve()
    print("x = {%s, %s}" %(solutions[0], solutions[1]))

if __name__ == "__main__":
    main()
