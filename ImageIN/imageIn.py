#imports
from ast import Import
from operator import truediv
from pickle import FALSE, TRUE
import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from cv2 import FileNode_NAMED
import numpy as np

class importImage:
    path = ""
    name = ""
    ext = ""
    transparancy = 1.0
    rotation = 0.0
    width = 0
    height = 0

class allImages:
    imgList = []
    def __init__(self):
        self.img1 = importImage()
        self.imgList.append(self.img1)
        self.img2 = importImage()
        self.imgList.append(self.img2)
        self.img3 = importImage()
        self.imgList.append(self.img3)
        self.img4 = importImage()
        self.imgList.append(self.img4)
        self.img5 = importImage()
        self.imgList.append(self.img5)
        self.img6 = importImage()
        self.imgList.append(self.img6)
        self.img7 = importImage()
        self.imgList.append(self.img7)
        self.img8 = importImage()
        self.imgList.append(self.img8)
        self.img9 = importImage()
        self.imgList.append(self.img9)
        self.img10 = importImage()
        self.imgList.append(self.img10)

    



#importing method
def imgImport(numImage):
    #removing unused images from list
    for i in range (numImage - 1, 9):
        allImages.imgList.pop()

    #idk what this does but its necesary
    root = tk.Tk()
    root.withdraw()

    #loop until no more images to select
    for image in allImages.imgList:
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
        if (image.ext.lower() != "png"):
            print("File type not supported. Please try again.")
            break
        #extract size and then extract height and width
        imageSize = imageOut.size
        image.width, image.height = imageSize
        #show image
        #imageOut.show()

def updateTrans(imageNum, trans):
    allImages.imgList[imageNum].transparancy = trans

print("Welcome to the image import wizard. You will be walked through how to import any number of images to be used with the image combination program.")
num = int(input("How many images would you like to import (max 10)"))
Images = allImages()
imgImport(num)