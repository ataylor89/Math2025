# The algorithm that I know of to solve a system of linear equations is called "Gaussian elimination".
# We can also use Gaussian elimination to invert a matrix.
#
# There are other ways to solve a system of linear equations, like substitution.
# But I like the Gaussian elimination approach.
#
# It takes so long to implement this algorithm, in source code, that I just use numpy instead.
#
# numpy has methods for inverting a matrix and calculating the determinant of a matrix.
# I use these methods to help me solve the system of equations.
#
# We mentioned two approaches so far, elimination and substitution.
# A third approach is to invert the coefficients matrix, and to multiply the inverse matrix by the constants.
#
# In this program, I take the third approach.
#
# I invert the coefficients matrix (let's call it M) and I calculate M^{-1} * (c1, c2, ..., cn),
# where the sequence (c1, c2, ..., cn) represents the constants.
#
# We discovered in the imageprocessing folder that matrices help us transform images.
# Matrices also help us solve systems of equations.
#
# Consider the following system of equations
# 2x + 4y = 6
# 3x + 5y = 7
#
# We can write this system as an equation involving matrices (a vector is just a 1-by-n or n-by-1 matrix).
# (2 4) (x)  =  (6)
# (3 5) (y)  =  (7)
#
# We now just have to solve for the unknown, the variables x and y.
#
# The field of algebra has to do with solving for an unknown.
# (In other words, algebra is solving for an unknown)

# This is also the case in linear algebra.
# The solution to a system of linear equations is an unknown.
#
# In the example I gave, the unknown is (x, y)
# 
# There are many ways of solving for (x, y). Three approaches we can take are:
# (1) Elimination or Gaussian elimination
# (2) Substitution
# (3) Inverting the lefthand matrix, and left-multiplying both sides by the inverse.
#
# In this program we take the third approach, matrix inversion, using the helper functions from numpy.

from parser import Parser, ParseTree
import numpy as np

FILENAME = 'problems/problem5.txt'

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
