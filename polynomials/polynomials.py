from parser import Parser

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
