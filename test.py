# To take the size of an img
from PIL import Image

img = Image.open("pic.png")
width, height = img.size
print(f"The image is {width}x{height}")

# To take an input from the console
yoo = input("Your number is: ")

# Two different ways of string interpolation
yo2 = "message"
print(f"This is a {yo2}")
print("This is a", yo2, "too")
