from PIL import Image
from PIL import ImageStat
import math

chars = [' ','-','+','0','#']
pathToImage = ''

img = Image.open(pathToImage).convert('LA') 

def convertToAscii(img,chars):
    width, height = img.size
    string = ""
    for x in range(width):
        for y in range(height):
            g, _ = img.getpixel((x,y))
            char = chars[0]
            for i in range(len(chars)):
                if g <= i * (256 / len(chars)):
                    char = chars[i]
            string += char 
        string += '\n'
    return string

def fileWrite(string):
    with open("test.txt",'w+') as tf:
        tf.write(string)

fileWrite(convertToAscii(img,chars))
