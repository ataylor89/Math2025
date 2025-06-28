from parser import Parser

class Polynomial:
    def __init__(self, text):
        parser = Parser()
        result = parser.parse(text)
        self.text = text
        self.degree = result.degree
        self.coefficients = result.coefficients
