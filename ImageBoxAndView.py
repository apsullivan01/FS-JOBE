from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider

from ImageView import ImageView


class ImageBoxAndView:
    def __init__(self,fileName):
        # image to display
        self.image = ImageView(fileName)
        # sliders and text associated to image
        self.imageBox = BoxLayout(orientation='vertical', spacing=dp(5))
        self.imageSlider = Slider(min=0, max=100)
        self.imageSlider.bind(value=self.image.changeOpacity)
        # add sliders and label to image box
        self.imageBox.add_widget(Label(text=fileName))
        self.imageBox.add_widget(self.imageSlider)
    def getBox(self):
        return self.imageBox
    def getView(self):
        return self.image