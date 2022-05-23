#imports
from operator import truediv
from pickle import FALSE, TRUE
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import numpy as np

#bool for adding more images
moreImg = TRUE

#idk what this does but its necesary
root = tk.Tk()
root.withdraw()

#declare list
imgList = []

#loop until no more images to select
while (moreImg):
    file_path = filedialog.askopenfilename()
    imgList.append(file_path)
    more = input("Would you like to add another image? (Y,N)")
    if (more.lower() == "n"):
        moreImg = FALSE
        break

#loop through images in list and open, will then be modified to work with 
for image in imgList:
    imageOut = Image.open(image)
    imageOut.show()