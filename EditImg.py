from kivy.graphics import Rectangle
from kivy.metrics import dp
from kivy.uix.relativelayout import RelativeLayout


class EditImg(RelativeLayout):
    def __init__(self, imageName, **kwargs):
        super(EditImg, self).__init__(**kwargs)
        self.size = (dp(350),dp(350))
        with self.canvas:
            self.pos = (dp(0), dp(0))
            img = Rectangle(source=imageName, pos=(self.pos), size=(self.size))
            img.rotate(self.angle)
    def translate(self, instance, pos):
        self.pos = pos/100
    
    def resize(self, size):
        self.size = size/100
    
    def rotate(self, angle):
        self.angle = angle/100