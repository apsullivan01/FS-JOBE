# App Imports
from kivy.app import App
# UIX Imports
from kivy.graphics import Rectangle, Color
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
# Property Imports
from kivy.properties import NumericProperty
#File imports
from kivy.uix.widget import Widget

import ImageIN
from ImageIN import imageIn
#from Sliders import UI,ImageView
import os

# Basic GUI Implementation
# Widgets
from UI import UI


class WidgetContainer(BoxLayout):
    def __init__(self, **kwargs):
        super(WidgetContainer, self).__init__(**kwargs)
        self.input_num = None
        self.orientation = 'vertical'
        self.row_default_height = 20
        self.spacing = 10

        # Each button corresponds to the action they would like to take
        select_images = Button(text='Select Images', on_release=self.select_images)
        to_sliders = Button(text='To Sliders', on_release=self.to_sliders)
        load_button = Button(text='Load Images', on_release=self.load_state)
        save_button = Button(text='Save State', on_release=self.save_state)

        self.add_widget(select_images)
        self.add_widget(load_button)
        self.add_widget(save_button)
        self.add_widget(to_sliders)

    # Go back to home state
    def go_home(self, event):
        self.clear_widgets()
        # Each button corresponds to the action they would like to take
        select_images = Button(text='Select Images', on_release=self.select_images)
        to_sliders = Button(text='To Sliders', on_release=self.to_sliders)
        load_button = Button(text='Load Images', on_release=self.load_state)
        save_button = Button(text='Save State', on_release=self.save_state)

        self.add_widget(select_images)
        self.add_widget(load_button)
        self.add_widget(save_button)
        self.add_widget(to_sliders)

    # Clear the interface and setup image selection
    def select_images(self, event):
        self.clear_widgets()
        back_button = Button(text='Home', size_hint=(1, .5), on_release=self.go_home)
        self.add_widget(back_button)

        input_label = Label(text='Enter number of images to be imported in text field below (max 10)')
        self.add_widget(input_label)
        self.input_num = TextInput(text='', size_hint=(1, .2))
        submit_button = Button(text='Submit', on_release=self.submit, size_hint=(1, .2))
        self.add_widget(self.input_num)
        self.add_widget(submit_button)

    # Clear the interface and bring up loadable states
    def load_state(self, event):
        self.clear_widgets()
        back_button = Button(text='Home')
        self.add_widget(back_button)
        back_button.bind(on_release=self.go_home)

    # Needs to be an option after to sliders
    def save_state(self, event):
        self.clear_widgets()
        back_button = Button(text='Home')
        self.add_widget(back_button)

        back_button.bind(on_release=self.go_home)
        pass

    # Go to sliders for image stacking and previewing
    def to_sliders(self, event):
        self.clear_widgets()
        #box = BoxLayout(orientation='vertical')
        #back_button = Button(text='Home',size_hint=(1,0.1))
        #back_button.bind(on_release=self.go_home)

        #box.add_widget(back_button)
        self.sliders = UI()
        #box.add_widget(sliders)
        self.add_widget(self.sliders)


    def submit(self, obj):
        self.numImg = self.input_num.text
        self.imageList = imageIn.imgImport(int(self.numImg))
        self.sliders.setImageList(self.imageList)


# App Class
class UserInterface(App):
    # Build starting interface
    def build(self):
        widgetContainer = WidgetContainer()
        return widgetContainer


if __name__ == "__main__":
    window = UserInterface()
    window.run()
