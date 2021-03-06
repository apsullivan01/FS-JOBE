from PIL import Image

#takes list of images and corresponding list of transparencies

def renderOverlay(slides, transparency,name):
    #open first image, convert to RGBA, set transparency
    background = slides[0]
    background = background.convert("RGBA")
    background.putalpha(transparency[0])
    
    #convert to RGBA, set transparency, and paste consecutive images over background
    i = 0
    for element in slides:
        if (i > 0):
            x = (background.width - element.width)//2
            y = (background.height - element.height)//2
            mask = element.convert("RGBA")
            mask.putalpha(transparency[i])
            background.paste(
                element,
                (x, y),
                mask)
        i += 1
    background.save(name + ".png", format="PNG")
    background.show()

#TEST CODE
#img1 = Image.open("Images\L15 XPL.png")
#img2 = Image.open("Images\L15-Plain.jpg")
#renderOverlay([img1, img2], [255, 128])