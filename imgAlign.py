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
        print(element.size)
        new_size = int(x * value[2]), int(y * value[2])
        print(new_size)
        element = element.resize(new_size)

        element = element.crop((value[0][0] * -1, value[0][1] * -1, size[0] - value[0][0], size[1] - value[0][1]))
        #translation
        #element = element.transform(element.size, Image.AFFINE, (1, 0, value[0][0], 0, 1, value[0][1]))

        element.save(key + "_aligned.png", format="PNG")
        list.append(key + "_aligned.png")
    return list
#TEST CODE
#img1 = Image.open("Images\L15 XPL.png")
img2 = Image.open("Images\L15-Plain.jpg")
dict = {}
dict['Images\L15 XPL.png'] = ((300, 0), 90, 1)
imgAlign(dict, "Images\L15 XPL.png")