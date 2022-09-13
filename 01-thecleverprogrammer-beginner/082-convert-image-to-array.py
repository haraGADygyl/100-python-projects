from PIL import Image
from numpy import  asarray

image = Image.open('resources/1.jpg')
data = asarray(image)
print(data)
