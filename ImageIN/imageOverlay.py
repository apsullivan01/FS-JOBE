from PIL import Image

def renderOverlay(slides):
    background = Image.open('image1.png')
    x = background.size[0]//2
    y = background.size[1]//2
    background = Image.alpha_composite(
        Image.new("RGBA", background.size),
        background.convert('RGBA')
    )
    for element in slides:
        background.paste(
            element,
            (x, y),
            element
        )
    background.show()