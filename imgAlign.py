from PIL import Image
from matplotlib import offsetbox

#takes list of images and corresponding lists of transformation matrices, as well as bool for saving images

def imgAlign(dict, bgName):
    #iterate through images
    list = []
    size = Image.open(bgName).size
    for key, value in dict.items():
        element = Image.open(key)
        #rotation
        element = element.rotate(value[1])
        #resizing
        x, y = element.size
        x_pos = x * value[0][0]
        y_pos = y * value[0][1]
        new_size = int(x * value[2]), int(y * value[2])
        element = element.resize(new_size)
        element = element.crop((x_pos * -1,(y - y_pos - new_size[1]) * -1 , x - x_pos, y_pos + new_size[1]))
        #translation
        #element = element.transform(element.size, Image.AFFINE, (1, 0, value[0][0], 0, 1, value[0][1]))
        stringName = key.replace(".png","")
        element.save(stringName + "_aligned.png", format="PNG")
        list.append(stringName + "_aligned.png")
    return list
#TEST CODE
#img1 = Image.open("Images\L15 XPL.png")
#img2 = Image.open("Images\L15-Plain.jpg")
#dict = {}
#dict['Images/L03 - Modal analysis #1_Panorama_Phases+BSE.png'] = ((0.0, 0.0), 356.07026066052475, 0.8786625992724453)
#imgAlign(dict, "Images/L03.png")