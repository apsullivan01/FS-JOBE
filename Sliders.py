import kivy
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line,Rectangle

# Property that represents a numeric value
# within a minimum bound and / or maximum
# bound – within a numeric range.
from kivy.properties import NumericProperty

# class in which we are defining the
# sliders and its effects
from kivy.uix.widget import Widget


class UI(BoxLayout):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.imageArea = BoxLayout(orientation='vertical')
        self.imageArea.add_widget(Widget(size_hint=(1,0.4)))
        self.sideBar = GridLayout(cols=1, row_force_default=True, row_default_height=150)

        self.imageOne = ImageView('Images/L15.png')
        self.imageOneBox = BoxLayout(orientation='vertical', spacing=dp(5))
        with self.sideBar.canvas:
            Color(1, 1, 0, 0)
            self.bg = Rectangle(pos=self.pos, size=self.size)
        self.imageOneSlider = Slider(min=0, max=100)
        self.imageOneSlider.bind(value=self.imageOne.changeOpacity)
        self.imageOneBox.add_widget(Label(text='L15.png'))
        self.imageOneBox.add_widget(self.imageOneSlider)

        self.imageTwo = ImageView('Images/L15 XPL.png')
        self.imageTwoBox = BoxLayout(orientation='vertical')
        self.imageTwoSlider = Slider(min=0, max=100)
        self.imageTwoSlider.bind(value=self.imageTwo.changeOpacity)
        self.imageTwoBox.add_widget(Label(text='L15 XPL.png'))
        self.imageTwoBox.add_widget(self.imageTwoSlider)

        self.imageAreaFix = AnchorLayout(anchor_x='center', anchor_y='center')
        self.imageAreaFix.add_widget(self.imageOne)
        self.imageAreaFix.add_widget(self.imageTwo)

        self.imageArea.add_widget(self.imageAreaFix)
        self.imageArea.add_widget(Widget(size_hint=(1, 0.4)))
        self.sideBar.add_widget(self.imageOneBox)
        self.sideBar.add_widget(self.imageTwoBox)
        self.add_widget(self.sideBar)
        self.add_widget(self.imageArea)


class ImageView(RelativeLayout):
    def __init__(self, imageName, **kwargs):
        super(ImageView, self).__init__(**kwargs)
        self.size = (dp(350),dp(350))
        with self.canvas:
            self.opacity = 1
            Rectangle(source=imageName, pos=(dp(30),dp(0)), size=(dp(350),dp(350)))

    def changeOpacity(self, instance, opacity):
        self.opacity = opacity/100

# The app class
