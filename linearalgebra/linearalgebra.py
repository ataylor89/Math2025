from parser import Parser, ParseTree
import numpy as np

FILENAME = 'problems/problem4.txt'

parser = Parser()
result = parser.parse(FILENAME)
matrix = np.array(result.coefficients)

if np.linalg.det(matrix) == 0:
    print("The system has no solution or infinitely many solutions.")
else:
    inverse_matrix = np.linalg.inv(matrix)
    constants = np.array(result.constants)
    solution = inverse_matrix @ constants
    print("Solution: %s" %solution)
