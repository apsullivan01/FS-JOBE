#imports
from ast import Import
import importImage
from operator import truediv
from pickle import FALSE, TRUE
import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from cv2 import FileNode_NAMED
import numpy as np

#declare list
img1 = importImage()
img2 = importImage()
img3 = importImage()
img4 = importImage()
img5 = importImage()
img6 = importImage()
img7 = importImage()
img8 = importImage()
img9 = importImage()
img10 = importImage()

imgList = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10]

#importing method
def imgImport(numImage):
    #removing unused images from list
    for i in range (numImage - 1, 9):
        imgList.pop()

    #idk what this does but its necesary
    root = tk.Tk()
    root.withdraw()



    #loop until no more images to select
    for image in imgList:
        #extract file path from dialog box
        image.path = filedialog.askopenfilename()
        #create image object
        imageOut = Image.open(image.path)
        #extract name
        image.name = imageOut.filename
        #extract file extension
        image.ext = imageOut.format
        #check for supported file type
        #this might need to be fixed, kinda shit code ngl
        if (image.ext.lower() != "jpeg"):
            print("File type not supported. Please try again.")
            break
        #extract size and then extract height and width
        imageSize = imageOut.size
        image.width, image.height = imageSize
        #show image
        imageOut.show()

print("Welcome to the image import wizard. You will be walked through how to import any number of images to be used with the image combination program.")
num = int(input("How many images would you like to import (max 10)"))
imgImport(num)