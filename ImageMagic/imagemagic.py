import matplotlib.image as mpimg
import numpy as np
import math

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
