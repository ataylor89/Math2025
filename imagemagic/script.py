from PIL import Image
import imagemagic
import math

input_file = 'images/usflag/usflag.png'
output_file = 'images/usflag/transformations/rotate90.png'

#input_file = 'images/pawn/pawn.png'
#output_file = 'images/pawn/transformations/rotate90.png'

#input_file = 'images/stacksofwheat/stacksofwheat.jpg'
#output_file = 'images/stacksofwheat/transformations/rotate90.jpg'

#input_file = 'images/beachatsainteadresse/beachatsainteadresse.jpg'
#output_file = 'images/beachatsainteadresse/transformations/rotate90.jpg'

image = imagemagic.rotate(input_file, math.pi/2)
image.save(output_file)
image.show()
