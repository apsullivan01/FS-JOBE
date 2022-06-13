from kivy.graphics import Rectangle
from kivy.metrics import dp
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout


class ImageView(RelativeLayout):
    def __init__(self, imageName, **kwargs):
        super(ImageView, self).__init__(**kwargs)
        self.size = (dp(500), dp(500))
        # self.allow_stretch = True
        self.add_widget(Image(source=imageName,size=self.size,pos=self.pos))

    def changeOpacity(self, instance, opacity):
        self.opacity = opacity/255

    def translate(self, instance, pos):
        self.x -= 10

    def resize(self, instance, size):
        self.texture_size -= 10

    def rotate(self, instance, angle):
        self.angle = angle/100

