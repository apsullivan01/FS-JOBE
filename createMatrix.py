import imageIn
import userInterface
import numpy as np
from PIL import Image
import imageio

matrixList = []
pokeThroughList = []

#this all kind of works, the instancing is fucked tbh
#unsure how all of this will be called
#but basic idea is as follows:
    #create new image matrix, this loops through all layers and creates 3d matrix of the individual pixel values
    #given a point (x,y):
        #pokeThrough will create a list of each layers rgba value (as a touple) at that point

class pokeThrough:
    pokeThroughList = []
    def pokeThrough(x, y):
        for layer in matrixList:
            rgba = (layer[x,y,0], layer[x,y,1], layer[x,y,2], layer[x,y,3])
            pokeThroughList.append(rgba)

class imgMatrix:
    def createMatrix(imgList):
        #loop through all images
        for image in imgList:
            img = Image.open(image)
            #cast to 3d array
            arr = np.array(img)
            matrixList.append(arr)
            #do something with said array
            #needs to be updated
            np.savetxt("test.csv", arr, delimiter=",")
    

            