from ImageIN import imageIn
import userInterface
import numpy as np
from PIL import Image
import imageio

def createMatrix(imgList):
    for image in imgList:
         img = Image.open(image.path)
         arr = np.array(img)
         print(arr)