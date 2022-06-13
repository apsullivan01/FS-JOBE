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
from kivy.uix.screenmanager import ScreenManager, Screen

# Other Imports
import imageIn
import os
import imgAlign
import imageOverlay
from PIL import Image
# from Sliders import UI,ImageView
from UI import UI
from Scatter import ImageEditSceen


# Basic GUI Implementation
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        # Call to box layout constructor
        super(HomeScreen, self).__init__(**kwargs)
        # Declaring options for spacing and look
        self.homeScreen = BoxLayout(orientation='vertical', spacing=10)
        self.homeScreen.row_default_height = 20
        self.imageList = []
        self.input_num = None

        # Each button corresponds to the action they would like to take
        select_images = Button(text='Select Images', on_release=self.select_images)
        to_sliders = Button(text='To Sliders', on_release=self.to_sliders)
        edit_button = Button(text='Edit Images', on_release=self.edit_images)

        # Adding buttons to the home screen
        self.homeScreen.add_widget(select_images)
        self.homeScreen.add_widget(edit_button)
        self.homeScreen.add_widget(to_sliders)

        self.add_widget(self.homeScreen)

    # Clear the interface and setup image selection
    def select_images(self, event):
        self.manager.transition.direction = 'left'
        self.manager.current = 'selectScreen'

    # Clear the interface and bring up loadable states
    def edit_images(self, event):
        #temp
        self.manager.get_screen('editScreen').createArea(['Images/L03 XPL.png','Images/L03.png'])

        self.manager.transition.direction = 'left'
        self.manager.current = 'editScreen'

    # Go to sliders for image stacking and previewing
    def to_sliders(self, event):
        self.manager.transition.direction = 'left'
        self.manager.current = 'slidersScreen'

    def submit(self, numImages):
        # Grabs the number of images in the input_num TextInput
        self.numImg = numImages

        # Brings up the image importing interface
        self.imageListClass = imageIn.imgImport(int(self.numImg))

        # Gets the list of images imported
        self.imageList = self.imageListClass.getImageList()

        self.manager.get_screen('editScreen').createArea(self.imageList)

        # Creates the entirety of the slider and image sections


class SelectImages(Screen):
    def __init__(self, **kwargs):
        # Call to box layout constructor
        super(SelectImages, self).__init__(**kwargs)
        self.selectScreen = BoxLayout(orientation='vertical', spacing=10)
        self.selectScreen.row_default_height = 20
        self.numImg = None
        back_button = Button(text='Home', size_hint=(1, .5), on_release=self.go_home)
        self.input_num = TextInput(text='', size_hint=(1, .2), write_tab=False, multiline=False,
                                   on_text_validate=self.submit)
        input_label = Label(text='Enter number of images to be imported in text field below (max 10) \n'
                                 'Only use files in the .png format')

        self.selectScreen.add_widget(back_button)
        self.selectScreen.add_widget(input_label)
        self.selectScreen.add_widget(self.input_num)

        self.add_widget(self.selectScreen)

    def go_home(self, event):
        self.manager.transition.direction = 'right'
        self.manager.current = 'homeScreen'

    def submit(self, event):
        # Grabs the number of images in the input_num TextInput
        chg = self.manager.get_screen('homeScreen')
        chg.submit(self.input_num.text)
        self.go_home(event)

class EditImages(Screen):
    def __init__(self, **kwargs):
        # Call to box layout constructor
        super(EditImages, self).__init__(**kwargs)
        self.export_info = {}

        self.image_edit = ImageEditSceen()
        # Creates the entirety of the slider and image sections

        # Creating back button and new box layout for images and sliders
        back_button = Button(text='Home', size_hint=(1, 0.1), on_release=self.go_home)
        box = BoxLayout(orientation='vertical')
        warning = Label(text='Press Save Image before Next Image', size_hint=(1,0.1))
        #export_botton = Button(text='Export saved images', size_hint=(1, 0.1), on_release=self.export)
        self.export_button = Button(text='Export saved images', size_hint=(1, 0.1), on_release=self.export)
        # Adding created widgets to the user interface
        box.add_widget(back_button)
        box.add_widget(warning)
        box.add_widget(self.image_edit)
        #box.add_widget(export_botton)
        box.add_widget(self.export_button)
        self.add_widget(box)

    def createArea(self, imageList):
        self.image_list = imageList
        self.image_edit.createArea(imageList)

    def go_home(self, event):
        self.manager.transition.direction = 'right'
        self.manager.current = 'homeScreen'

    def handle_save(self,pos, rotation, scale, image_name):
        self.export_info[image_name] = (pos, rotation, scale)
        print(pos, rotation, scale)

    def export(self,event):
        print()
        list = imgAlign.imgAlign(self.export_info,self.image_list[0])
        list.insert(0,self.image_list[0])
        self.manager.get_screen('slidersScreen').updateList(list)

    def init_pos(self):
        self.self.export_button.size


class SlidersScreen(Screen):
    def __init__(self, **kwargs):
        # Call to box layout constructor
        super(SlidersScreen, self).__init__(**kwargs)
        self.slidersScreen = BoxLayout(orientation='vertical', spacing=10)
        self.sliders = UI()
        back_button = Button(text='Home', size_hint=(1, 0.1), on_release=self.go_home)
        save_button = Button(text='Save Transparencies', size_hint=(1, 0.1), on_release=self.save_transp)
        # Adding created widgets to the user Interface
        self.slidersScreen.add_widget(back_button)
        self.slidersScreen.add_widget(self.sliders)
        self.add_widget(self.slidersScreen)
        self.add_widget(save_button)

    def updateList(self, imageList):
        self.newImageList = imageList
        self.sliders.showImageObj(imageList)


    def go_home(self, event):
        self.manager.transition.direction = 'right'
        self.manager.current = 'homeScreen'

    def save_transp(self, event):
        transpList = self.sliders.get_transparencies()
        slidesList = []
        for image in self.newImageList:
            slidesList.append(Image.open(image))
        imageOverlay.renderOverlay(slidesList, transpList)

# App Class
class UserInterface(App):
    # Build starting interface
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(HomeScreen(name="homeScreen"))
        screen_manager.add_widget(SelectImages(name="selectScreen"))
        screen_manager.add_widget(EditImages(name="editScreen"))
        screen_manager.add_widget(SlidersScreen(name="slidersScreen"))
        return screen_manager


if __name__ == "__main__":
    window = UserInterface()
    window.run()
