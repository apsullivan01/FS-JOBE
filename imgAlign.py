from PIL import Image

#takes list of images and corresponding lists of transformation matrices, as well as bool for saving images

def imgAlign(slides, positions, rotations, sizes, saveImg):
    #iterate through images
    i = 0
    for element in slides:
        #translation
        element = element.transform(element.size, Image.AFFINE, (1, 0, positions[i][0], 0, 1, positions[i][1]))
        #rotation
        element = element.rotate(rotations[i])
        #resizing
        element = element.resize(sizes[i])

        if (saveImg):
            element.save("alignedImg" + str(i) + ".png", format="PNG")
        i += 1
    return slides

#TEST CODE
img1 = Image.open("Images\L15 XPL.png")
img2 = Image.open("Images\L15-Plain.jpg")
imgAlign([img1, img2], [(0, 0), (50, 0)], [180, 0], [(300, 300), (img2.size)], 1)