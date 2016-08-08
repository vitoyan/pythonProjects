#the gray formula
# gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
# most of below is from shiyanlou.com/courses/370/labs/1191

from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type = int, default = 80)
parser.add_argument('--height', type = int, default = 80)

args = parser.parse_args()

IMAGE = args.file
OUT = args.output
WIDTH = args.width
HEIGHT = args.height

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def convertGrayToChar(r, b, g, grayScale = 256):
    if(grayScale == 0):
        return ' '

    vol = len(ascii_char)
    gray = int(0.2126*r + 0.7125*b + 0.0722*g)

    rate = (grayScale + 1)/vol

    return ascii_char[int(gray/rate)]

if __name__ == '__main__':
    image = Image.open(IMAGE)
    image = image.resize((WIDTH, HEIGHT), Image.NEAREST)

    chars = ''

    for x in range(HEIGHT):
        for y in range(WIDTH):
            chars += convertGrayToChar(*image.getpixel((y, x)))
        chars += '\n'

    if OUT:
        with open(OUT, 'wt') as out:
            out.write(chars)
    else:
        with open('imageToString.txt','wt') as out:
            out.write(chars)

