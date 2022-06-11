from PIL import Image

#takes list of images and corresponding lists of transformation matrices, as well as bool for saving images

def imgAlign(dict, size):
    #iterate through images
    list = []
    for key, value in dict.items():
        element = Image.open(key)
        #translation
        element = element.transform(element.size, Image.AFFINE, (1, 0, value[0][0], 0, 1, value[0][1]))
        #rotation
        element = element.rotate(value[1])
        #resizing
        x, y = element.size
        print(element.size)
        new_size = int(x * value[2]), int(y * value[2])
        print(new_size)
        element = element.resize(new_size)
        element = element.crop(0, 0, size[0] * -1, size[1] * -1)

        element.save(key + "_aligned.png", format="PNG")
        list.append(key + "_aligned.png")
    return list
#TEST CODE
#img1 = Image.open("Images\L15 XPL.png")
img2 = Image.open("Images\L15-Plain.jpg")
dict = {}
dict['Images\L15 XPL.png'] = ((300, 0), 90, 0.01)
imgAlign(dict)