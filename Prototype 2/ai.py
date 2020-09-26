# Imports
import tensorflow as tf
from PIL import Image

# Print version
print('Using Tensorflow version '+tf.__version__)

# Get size and pixeldata
inputImage = Image.open('input.jpg')
width = inputImage.width
height = inputImage.height
inputData = list(inputImage.getdata())
