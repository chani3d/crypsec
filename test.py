
#To take the size of an img
from PIL import Image

img = Image.open("pic.png")
width, height = img.size
print(f"The image is {width}x{height}")

msgTest = "Antonio"
print(msgTest.toByte)

