# To take the size of an img
from PIL import Image

img = Image.open("pic.png")
width, height = img.size
print(f"The image is {width}x{height}")

# To get rgb info

for x in range(img.height):
    for y in range(img.width):
        print(y, x)

#img2 = img.convert('RGB')
#for x in range(img2.width):
    
#    r, g, b = img2.getpixel((0, 0))
#    print(x)
#    print(r.to_bytes(1, byteorder='big'))




# To take an input from the console
yoo = input("Your number is: ")

# Two different ways of string interpolation
yo2 = "message"
print(f"This is a {yo2}")
print("This is a", yo2, "too")

# Length method for string
yo3 = "Hello"
lengthOfyo3 = len(yo3)
print(lengthOfyo3)


# Function trys
def trys(string):
    print("You tried", string)

trys('something')

# Coding string
msg = 'hello'
lenght = len(msg)

coded = bytes(msg, 'utf-8')     # It points to an array, so...
coded2 = msg.encode('utf-8')        # This one's better

print(coded)
print(coded2)

# Coding numbers
number = 4

number2 = (number).to_bytes(2, byteorder = 'big')
print(number2)

# Iterate string

#for element in msg:
#    print((0).to_bytes(3, byteorder = 'big') + element.encode('utf-8'))

# To implement

def message(msg):

    header = 'ISC'.encode('utf-8')  # first 3 bytes
    length = (len(msg)).to_bytes(2, byteorder='big')  # 5th & 6th byte
    msgtype = 't'.encode('utf-8')
    msgbyte = bytes()  # N next bytes

    for element in msg:
        msgbyte += ((0).to_bytes(3, byteorder='big') + element.encode('utf-8'))

    fullmsg = header + msgtype + length + msgbyte
    return fullmsg

print(message('hello'))

# Searching something inside a string

fullstring = "Antoine Griezmann Nope"
substring = "Griezdman"
substring2 = "Nope"
substring3 = "Yep"

if substring2 or substring2 in fullstring:
    print("Found")
elif substring3 in fullstring:
    print("Second found")
else:
    print("Not found")

# Trying to decode a message received...

def decMsg(msg):
    btostr = msg.decode('utf-8')
    finn = btostr.replace('ISCt', '')
    return finn


received = message('test')
print(received)
print(decMsg(received))



