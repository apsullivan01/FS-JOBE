# Kivy Imports
from kivy.app import App
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
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget

# Other Imports
import imageIn
import os
# from Sliders import UI,ImageView
from UI import UI
from EditImg import EditImg

# Basic GUI Implementation
class WidgetContainer(BoxLayout):
    def __init__(self, **kwargs):
        # Call to box layout constructor
        super(WidgetContainer, self).__init__(**kwargs)

        # Declaring options for spacing and look
        self.orientation = 'vertical'
        self.row_default_height = 20
        self.spacing = 10

        # Instancing UI and EditImg
        self.sliders = UI()
        self.image_edit = EditImg()


        # Each button corresponds to the action they would like to take
        select_images = Button(text='Select Images', on_release=self.select_images)
        to_sliders = Button(text='To Sliders', on_release=self.to_sliders)
        edit_button = Button(text='Edit Images', on_release=self.edit_images)

        # Adding buttons to the home screen
        self.add_widget(select_images)
        self.add_widget(edit_button)
        self.add_widget(to_sliders)

    # Go back to "home" state
    def go_home(self, event):
        # Clears existing widgets to simulate change to Home screen
        self.clear_widgets()

        # Each button corresponds to the action they would like to take
        select_images = Button(text='Select Images', on_release=self.select_images)
        to_sliders = Button(text='To Sliders', on_release=self.to_sliders)
        edit_button = Button(text='Edit Images', on_release=self.edit_images)

        # Adding buttons to the "new" home screen
        self.add_widget(select_images)
        self.add_widget(edit_button)
        self.add_widget(to_sliders)

    # Clear the interface and setup image selection
    def select_images(self, event):
        # Clears existing widgets to simulate change to Select Images screen
        self.clear_widgets()

        # Creating necessary widgets - home button, label(for directions), and input
        back_button = Button(text='Home', size_hint=(1, .5), on_release=self.go_home)
        self.input_num = TextInput(text='', size_hint=(1, .2), write_tab=False, multiline=False,
                                   on_text_validate=self.submit)
        input_label = Label(text='Enter number of images to be imported in text field below (max 10) \n'
                                 'Only use files in the .png format')

        self.add_widget(back_button)
        self.add_widget(input_label)
        self.add_widget(self.input_num)

    # Clear the interface and bring up loadable states
    def edit_images(self, event):
        # Clears existing widgets to simulate change to Edit Images screen
        self.clear_widgets()

        # Creates the entirety of the slider and image sections
        self.image_edit.showImageObj(self.imageList)

        # Creating back button and new box layout for images and sliders
        back_button = Button(text='Home', size_hint=(1, 0.1), on_release=self.go_home)
        box = BoxLayout(orientation='vertical')

        # Adding created widgets to the user interface
        box.add_widget(back_button)
        box.add_widget(self.image_edit)
        self.add_widget(box)



    # Go to sliders for image stacking and previewing
    def to_sliders(self, event):
        # Clears existing widgets to simulate change to Sliders screen
        self.clear_widgets()

        # Creating back button and new box layout for images and sliders
        back_button = Button(text='Home', size_hint=(1, 0.1), on_release=self.go_home)
        box = BoxLayout(orientation='vertical')

        # Adding created widgets to the user Interface
        box.add_widget(back_button)
        box.add_widget(self.sliders)
        self.add_widget(box)


    def submit(self, obj):
        # Grabs the number of images in the input_num TextInput
        self.numImg = self.input_num.text

        # Brings up the image importing interface
        self.imageListClass = imageIn.imgImport(int(self.numImg))

        # Gets the list of images imported
        self.imageList = self.imageListClass.getImageList()

        # Creates the entirety of the slider and image sections
        self.sliders.showImageObj(self.imageList)


# App Class
class UserInterface(App):
    # Build starting interface
    def build(self):
        widgetContainer = WidgetContainer()
        return widgetContainer


if __name__ == "__main__":
    window = UserInterface()
    window.run()
