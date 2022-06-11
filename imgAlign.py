from PIL import Image

#takes list of images and corresponding lists of transformation matrices, as well as bool for saving images

def imgAlign(dict):
    #iterate through images
    for key, value in dict.items():
        element = Image.open(source=key)
        #translation
        element = element.transform(element.size, Image.AFFINE, (1, 0, value[0][0], 0, 1, value[0][1]))
        #rotation
        element = element.rotate(value[1])
        #resizing
        element = element.resize(element.size * value[2])

        element.save(key + "_aligned.png", format="PNG")

#TEST CODE
img1 = Image.open("Images\L15 XPL.png")
img2 = Image.open("Images\L15-Plain.jpg")
imgAlign([img1, img2], [(0, 0), (50, 0)], [180, 0], [(300, 300), (img2.size)], 1)