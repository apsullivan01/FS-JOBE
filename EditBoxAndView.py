from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider

from ImageView import ImageView

class EditBoxAndView:
    def __init__(self, fileName):
        # Image to display
        self.image = ImageView(fileName)
        # Sliders and text associated to image
        self.imageBox = BoxLayout(orientation='vertical', spacing=dp(5))
        self.positionSlider = Slider(min=0, max=100)
        self.positionSlider.bind(value=self.image.translate)
        self.sizeSlider = Slider(min=0, max=100)
        self.sizeSlider.bind(value=self.image.translate)
        self.angleSlider = Slider(min=0, max=100)
        self.angleSlider.bind(value=self.image.translate)
        # Add Sliders and label to image box
        self.imageBox.add_widget(Label(text=fileName))
        self.imageBox.add_widget(Label(text='Position'))
        self.imageBox.add_widget(self.positionSlider)
        self.imageBox.add_widget(Label(text='Size'))
        self.imageBox.add_widget(self.sizeSlider)
        self.imageBox.add_widget(Label(text='Rotation'))
        self.imageBox.add_widget(self.angleSlider)

    def getBox(self):
        return self.imageBox

    def getView(self):
        return self.image
