from PIL import Image
from imgcompare import image_diff_percent

image_a = Image.open("original.jpg")
image_b = Image.open("final.jpg")
percentage = image_diff_percent(image_a, image_b)

print(percentage)