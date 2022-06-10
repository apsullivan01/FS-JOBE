from kivy.graphics import Rectangle
from kivy.metrics import dp
from kivy.uix.relativelayout import RelativeLayout


class ImageView(RelativeLayout):
    def __init__(self, imageName, **kwargs):
        super(ImageView, self).__init__(**kwargs)
        self.size = (dp(500), dp(500))
        self.allow_stretch = True
        with self.canvas:
            self.opacity = 1
            Rectangle(source=imageName, pos=(dp(30),dp(0)), size=(dp(500),dp(500)))

    def changeOpacity(self, instance, opacity):
        self.opacity = opacity/100

    def translate(self, instance, pos):
        self.x -= 10

    def resize(self, instance, size):
        self.texture_size -= 10

    def rotate(self, instance, angle):
        self.angle = angle/100

