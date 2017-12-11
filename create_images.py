###
### This program actually flips all of the images around and leaves the intended negative images the same.
### It will create a new file for the results.
###
from PIL import Image
import os
import numpy.random as r
os.mkdir("test/training2")
for dir in os.listdir("test/training"):
    if dir != '.DS_Store':
        os.mkdir("test/training2/" + dir)
        for file in os.listdir("test/training/" + dir):
            picture = Image.open("test/training/" + dir + "/" + file)
            newimage = Image.new('L', picture.size)
            pix1 = picture.load()
            pix2 = newimage.load()
            k = r.randint(20) # If your desired percentage is not a multiple of 5%, modify this number.
            for i in range(0, picture.width):
                for j in range(0, picture.height):
                    if k % 20 <= 1: # Modify this value to control the number of negative images.
                        pix2[i, j] = pix1[i, j]
                    else:
                        pix2[i, j] = 255 - pix1[i, j]
            newimage.save("test/training2/" + dir + "/" + file)
            picture.close()
            newimage.close()

os.mkdir("test/testing2")
for dir in os.listdir("test/testing"):
    if dir != '.DS_Store':
        os.mkdir("test/testing2/" + dir)
        for file in os.listdir("test/testing/" + dir):
            picture = Image.open("test/testing/" + dir + "/" + file)
            newimage = Image.new('L', picture.size)
            pix1 = picture.load()
            pix2 = newimage.load()
            for i in range(0, picture.width):
                for j in range(0, picture.height):
                    pix2[i, j] = pix1[i, j]
            newimage.save("test/testing2/" + dir + "/" + file)
