class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return format("%s + %si" %(self.a, self.b))
