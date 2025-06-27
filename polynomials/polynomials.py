from parser import Parser, ParseTree
import math

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return format("%s + %si" %(self.a, self.b))

class Polynomial:
    def __init__(self, text):
        parser = Parser()
        result = parser.parse(text)
        self.text = text
        self.degree = result.degree
        self.coefficients = result.coefficients

    def solve(self):
        if self.degree == 2:
            return self._solve_quadratic()
        else:
            print("Currently, this class only supports quadratic polynomials.")

    def _solve_quadratic(self):
        if self.degree != 2:
            return
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

text = "3x^2 + 4x + 5"
p = Polynomial(text)
solutions = p.solve()
print("Polynomial: %s" %text)
print("Roots: x = {%s, %s}" %(solutions[0], solutions[1]))
