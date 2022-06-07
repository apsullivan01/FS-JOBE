from kivy.graphics import Rectangle
from kivy.metrics import dp
from kivy.uix.relativelayout import RelativeLayout


class ImageView(RelativeLayout):
    def __init__(self, imageName, **kwargs):
        super(ImageView, self).__init__(**kwargs)
        self.size = (dp(350),dp(350))
        with self.canvas:
            self.opacity = 1
            Rectangle(source=imageName, pos=(dp(30),dp(0)), size=(dp(350),dp(350)))

    def changeOpacity(self, instance, opacity):
        self.opacity = opacity/100
