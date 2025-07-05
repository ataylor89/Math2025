import imagemagic
import matplotlib.pyplot as plt
import math

input_file = 'images/pawn/pawn.png'
output_file = 'images/pawn/transformations/rotate90.png'

# The DPI for my computer is 72 dots per inch.
#
# I was able to figure out the DPI for my MacBook by opening an image in Preview,
# going to Tools->Show_Inspector, and getting the Image DPI from the General Info GUI.
#
# In order to make this program work, you might have to find out the DPI for your computer,
# and set the DPI variable accordingly.
#
# For some reason, inches are the native unit for matplotlib.
#
# We use DPI to convert between pixels and inches.
# DPI means dots per inch and also pixels per inch. The two meanings are equivalent.
#
# I hope that explains all this DPI business. It's a way of converting between pixels and inches.
DPI = plt.rcParams["figure.dpi"]

img = imagemagic.rotate(input_file, math.pi/2)
width = len(img[0])
height = len(img)

plt.figure(figsize=(width/DPI, height/DPI), dpi=DPI)
plt.axis("off")
plt.imshow(img)
plt.savefig(output_file, transparent=True)
