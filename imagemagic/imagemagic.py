import matplotlib.image as mpimg
import numpy as np
import math

# This module is dedicated to image transformation. It contains functions for transforming images.
#
# The main libraries used are (1) numpy and (2) matplotlib.
#
# We use numpy for matrix multiplication, and we use matplotlib to read and write images.
#
# The algorithm we use to transform images is described below.
# (In my opinion, an algorithm is just a list of instructions.)
# 
# Algorithm
# 1. We read an image into a matrix using matplotlib.
# 2. We calculate the dimensions of the matrix that will store the new image.
# 3. We create a new matrix with the right dimensions to store the new image.
# 4. We loop through every pixel (row, col) in the original image, and...
# 4a. We map the matrix coordinates (row, col) to Cartesian coordinates (x, y)
# 4b. We apply the linear transformation (x2, y2) = A * (x, y),
#     where A is the transformation matrix, to get the Cartesian coordinates in the new image.
# 4c. We map the Cartesian coordinates (x2, y2) to matrix coordinates (row2, col2).
# 4d. We set the color at (row2, col2) in the new image, to the color at (row, col) in the original image.
# 5. We return the new matrix. The new matrix can be rendered as an image using the matplotlib.pyplot library.
#
# I hope that these five steps are clear. I know that the code is a little confusing.
# Part of the confusion is due to library complexity. I think the libraries can be made a little simpler.
# Part of the confusion is due to the fact that we have to perform three coordinate transformations...
#
# First we convert matrix coordinates to Cartesian coordinates,
# Then we transform the Cartesian coordinates using the linear transformation y = Ax,
# Then we convert the resulting Cartesian coordinates to matrix coordinates.
#
# The main idea behind image transformation is this:
# We can use matrix multiplication to rotate or reflect a vector.
# Likewise, we can use matrix multiplication to rotate or reflect an image.
# 
# One reason we have matrices, in the first place, is for vector transformation and image transformation.
# It is very hard to rotate or reflect an image without resorting to matrix multiplication.
# But if we use matrix multiplication, it is a straightforward process.
#
# I think this is why we learn about matrices in high school.
# Matrices are very useful when dealing with graphics.
#
# I hope that this introduction is helpful.
# Let's move onto the code.
#
# The main functions in this module are rotate, reflectx, and reflecty.
# The other functions serve as utility functions.

# Gets the x, y coordinates of a pixel in an nxm image
def get_xy(row, col, n, m):
    i, j = col + 0.5, row + 0.5
    return [i - m/2, n/2 - j]

# Gets the row and column of a pixel in an nxm image
def get_rowcol(x, y, n, m):
    return [int(n/2 - y), int(x + m/2)]

# Rotates an image around the origin by the specified number of radians
def rotate(filename, radians):
    A = [[math.cos(radians), -1 * math.sin(radians)],
         [math.sin(radians), math.cos(radians)]]
    return transform(filename, A)

# Reflects an image around the x axis in an xy coordinate system
def reflectx(filename):
    A = [[1, 0],
         [0, -1]]
    return transform(filename, A)

# Reflects an image around the y axis in an xy coordinate system
def reflecty(filename):
    A = [[-1, 0], 
         [0, 1]]
    return transform(filename, A)

def transform(filename, A):
    # Read the image from file
    img = mpimg.imread(filename)
    n, m = len(img), len(img[0])
    print('%dx%d matrix (%s)' %(n, m, filename))

    # Get the dimensions of the new (transformed) image
    V = (np.array([-m/2, n/2]), np.array([-m/2, -n/2]), np.array([m/2, n/2]), np.array([m/2, -n/2]))
    V = np.column_stack(V)
    # Perform the linear transformation T = AV on the corners of the original image
    T = A @ V
    xmax, xmin = max(T[0]), min(T[0])
    ymax, ymin = max(T[1]), min(T[1])
    print('xmax=%1.2f xmin=%1.2f' %(xmax, xmin))
    print('ymax=%1.2f ymin=%1.2f' %(ymax, ymin))
    # The dimensions of the new image are N rows and M columns
    N, M = int(ymax-ymin), int(xmax-xmin)
    print("N=%d\nM=%d" %(N, M))

    # Get the xy coordinates for every pixel and store as column vectors in matrix X
    X = []
    for row in range(n):
        for col in range(m):
            coordinates = get_xy(row, col, n, m)
            X.append(np.array(coordinates))
    X = np.column_stack(X)

    # Perform the linear transformation Y = AX
    # Y contains the new coordinates for every pixel
    Y = A @ X

    # Create a matrix for our new image
    # Let's call it canvas
    # The new matrix has N rows and M columns
    canvas = [[[0, 0, 0] for i in range(M)] for j in range(N)]

    # Copy the RGB values from img into the appropriate pixel in canvas 
    num_cols = len(X[0])
    for col in range(num_cols):
        x, y = X[0][col], X[1][col]
        xt, yt = Y[0][col], Y[1][col]
        [row, col] = get_rowcol(x, y, n, m)
        [row_t, col_t] = get_rowcol(xt, yt, N, M)
        canvas[row_t][col_t] = img[row][col]

    return canvas
