#email NIGEL about seeing lab
#email Anne about images w/ reference points
#imports
from operator import truediv
from pickle import FALSE, TRUE
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import numpy as np
#bool for adding more images
moreImg = TRUE

root = tk.Tk()
root.withdraw()
imgList = []
while (moreImg):
    file_path = filedialog.askopenfilename()
    imgList.append(file_path)
    more = input("Would you like to add another image? (Y,N)")
    if (more.lower() == "n"):
        moreImg = FALSE
        break

for image in imgList:
    imageOut = Image.open(image)
    imageOut.show()