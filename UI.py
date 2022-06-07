from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget

from ImageBoxAndView import ImageBoxAndView
from ImageView import ImageView


class UI(BoxLayout):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.imageArea = BoxLayout(orientation='vertical')
        self.imageArea.add_widget(Widget(size_hint=(1,0.4)))
        self.sideBar = GridLayout(cols=1, row_force_default=True, row_default_height=150)

        self.imageOneObj = ImageBoxAndView('Images/L15.png')

        self.imageTwo = ImageView('Images/L15 XPL.png')
        self.imageTwoBox = BoxLayout(orientation='vertical')
        self.imageTwoSlider = Slider(min=0, max=100)
        self.imageTwoSlider.bind(value=self.imageTwo.changeOpacity)
        self.imageTwoBox.add_widget(Label(text='L15 XPL.png'))
        self.imageTwoBox.add_widget(self.imageTwoSlider)

        self.imageAreaFix = AnchorLayout(anchor_x='center', anchor_y='center')
        self.imageAreaFix.add_widget(self.imageOneObj.getView())
        self.imageAreaFix.add_widget(self.imageTwo)

        self.imageArea.add_widget(self.imageAreaFix)
        self.imageArea.add_widget(Widget(size_hint=(1, 0.4)))
        self.sideBar.add_widget(self.imageOneObj.getBox())
        self.sideBar.add_widget(self.imageTwoBox)
        self.add_widget(self.sideBar)
        self.add_widget(self.imageArea)