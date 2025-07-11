from PIL import Image
import numpy as np
import math

def rotate(filename, radians):
    A = [[math.cos(radians), -1 * math.sin(radians)],
         [math.sin(radians), math.cos(radians)]]
    return transform(filename, A)

def reflectx(filename):
    A = [[1, 0],
         [0, -1]]
    return transform(filename, A)

def reflecty(filename):
    A = [[-1, 0], 
         [0, 1]]
    return transform(filename, A)

def transform(filename, A):
    img = Image.open(filename)

    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA")

    w, h = img.size
    print("Image size: %dx%d" %(w, h))

    W, H = get_new_size(w, h, A)
    print("New image size: %dx%d" %(W, H))

    X = []
    for x in range(w):
        for y in range(h):
            coordinates = matrix_to_cartesian(y, x, h, w)
            X.append(np.array(coordinates))
    X = np.column_stack(X)
    Y = A @ X

    newimg = Image.new(img.mode, (W, H), (0, 0, 0, 0))
    numpixels = len(X[0])

    for i in range(numpixels):
        (row, col) = cartesian_to_matrix(X[0][i], X[1][i], w, h)
        pixel = img.getpixel((col, row))

        (row, col) = cartesian_to_matrix(Y[0][i], Y[1][i], W, H)
        newimg.putpixel((col, row), pixel)

    return newimg

def matrix_to_cartesian(i, j, n, m):
    x = j - (m-1)/2
    y = (n-1)/2 - i
    return (x, y)

def cartesian_to_matrix(x, y, w, h):
    i = int(h/2 - y)
    j = int(w/2 + x)
    return (i, j)

def get_new_size(w, h, A):
    corners = ((-(w-1)/2, (h-1)/2), (-(w-1)/2, -(h-1)/2), ((w-1)/2, -(h-1)/2), ((w-1)/2, (h-1)/2))
    X = np.column_stack([np.array(corner) for corner in corners])
    Y = A @ X
    return (int(max(Y[0]) - min(Y[0]) + 1), int(max(Y[1]) - min(Y[1]) + 1))
