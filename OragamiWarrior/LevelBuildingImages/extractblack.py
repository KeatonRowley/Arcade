from PIL import Image
import sys


def extract_black(filename):
    img = Image.open(filename).copy()
    img.putalpha(255)
    black = (0,0,0, 255)
    white = (255,255,255, 255)

    newimdata = []

    for color in img.getdata():
        if color != black:
            newimdata.append((255,255,255,0))
        else:
            newimdata.append(black)
    newim = Image.new(img.mode, img.size)
    newim.putdata(newimdata)
    return newim
    

filename = sys.argv[-1]
new_image = extract_black(filename)

new_image.save(filename)


