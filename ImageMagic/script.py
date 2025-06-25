import imagemagic
import matplotlib.pyplot as plt
import math

INPUT_FILE = 'images/pawn/pawn.png'
OUTPUT_FILE = 'images/pawn/transformations/rotate90.png'

img = imagemagic.rotate(INPUT_FILE, math.pi/2)
width = len(img[0])
height = len(img)

plt.figure(figsize=(width/72, height/72), dpi=72)
plt.axis("off")
plt.imshow(img)
plt.savefig(OUTPUT_FILE, transparent=True)
