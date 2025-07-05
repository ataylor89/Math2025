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

    (w, h) = img.size

    print('Image size: %dx%d' %(w, h))

    X = (np.array((-w/2, h/2)), np.array((-w/2, -h/2)), np.array((w/2, h/2)), np.array((w/2, -h/2)))
    X = np.column_stack(X)

    Y = A @ X

    W = int(max(Y[0]) - min(Y[0]))
    H = int(max(Y[1]) - min(Y[1]))

    print('New image size: %dx%d' %(W, H))

    X = []
    for x in range(w):
        for y in range(h):
            coordinates = (x + 0.5 - w/2, h/2 - (y + 0.5))
            X.append(np.array(coordinates))
    X = np.column_stack(X)

    Y = A @ X

    newimg = Image.new(img.mode, (W, H), (0, 0, 0, 0))
    numpixels = W * H

    for i in range(numpixels):
        x, y = int(X[0][i] + w/2), int(h/2 - X[1][i])
        pixel = img.getpixel((x, y))

        x, y = int(Y[0][i] + W/2), int(H/2 - int(Y[1][i]))
        newimg.putpixel((x, y), pixel)

    return newimg
