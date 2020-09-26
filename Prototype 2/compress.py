from PIL import Image

# Get image
img = Image.open('original.jpg')

# Get image height and width
width = img.width
height = img.height

# Divide by
divide = 8

# Create smaller image
img.thumbnail((width/divide,height/divide))
img.save('input.jpg')