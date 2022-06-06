from PIL import Image

def renderOverlay(slides, transparency):
    #open first image, convert to RGBA, set transparency
    background = slides[0]
    background = background.convert("RGBA")
    background.putalpha(transparency[i])
    
    x = background.size[0]//2
    y = background.size[1]//2
    
    #background = Image.alpha_composite(
    #    Image.new("RGBA", background.size),
    #    background.convert('RGBA'))
    
    #convert to RGBA, set transparency, and paste consecutive images over background
    i = 1
    for element in slides:
        element.putalpha(transparency[i])
        background.paste(
            element,
            (x, y),
            element)
        i += 1
    background.show()