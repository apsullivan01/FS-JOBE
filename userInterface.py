# Kivy Imports
import gc

import kivy
kivy.require('2.1.0')
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
        self.outputImageList = []
        self.input_num = None

        # Each button corresponds to the action they would like to take
        select_images = Button(text='Select Images', on_release=self.select_images)
        to_sliders = Button(text='View and Change Transparency', on_release=self.to_sliders)
        edit_button = Button(text='Align Images', on_release=self.edit_images)

        # Adding buttons to the home screen
        self.homeScreen.add_widget(select_images)
        self.homeScreen.add_widget(edit_button)
        self.homeScreen.add_widget(to_sliders)

        self.add_widget(self.homeScreen)

    # Clear the interface and setup image selection
    def select_images(self, event):
        if len(self.imageList) > 0:
            not_empty = Popup(title='This will clear your current images.', content=BoxLayout(orientation='horizontal'),
                              size_hint=(0.2, 0.2))
            cont_button = Button(text='Continue', on_press=self.select_images_help, on_release=not_empty.dismiss)
            go_back_button = Button(text='Back', on_release=not_empty.dismiss)
            not_empty.content.add_widget(cont_button)
            not_empty.content.add_widget(go_back_button)
            not_empty.open()
        else:
            self.select_images_help(event)

    def select_images_help(self, event):
        self.imageList = []
        self.outputImageList = []
        self.manager.transition.direction = 'left'
        self.manager.current = 'selectScreen'
        self.manager.get_screen('selectScreen').create()
        if self.manager.has_screen('editScreen'):
            self.manager.remove_widget(self.manager.get_screen('editScreen'))
        if self.manager.has_screen('slidersScreen'):
            self.manager.remove_widget(self.manager.get_screen('slidersScreen'))
        self.manager.add_widget(EditImages(name="editScreen"))
        self.manager.add_widget(SlidersScreen(name="slidersScreen"))

    # Clear the interface and bring up loadable states
    def edit_images(self, event):
        self.manager.get_screen('editScreen').image_edit.clear_widgets()
        gc.collect()
        self.manager.get_screen('editScreen').createArea(self.imageList)
        self.manager.transition.direction = 'left'
        self.manager.current = 'editScreen'

    # Go to sliders for image stacking and previewing
    def to_sliders(self, event):
        self.manager.get_screen('slidersScreen').sliders.reinit()
        self.manager.get_screen('slidersScreen').updateList(self.outputImageList)
        self.manager.transition.direction = 'left'
        self.manager.current = 'slidersScreen'

    def submit(self, numImages):
        # Grabs the number of images in the input_num TextInput
        self.numImg = numImages

        # Brings up the image importing interface
        self.imageListClass = imageIn.imgImport(int(self.numImg))

        # Gets the list of images imported
        self.imageList = self.imageListClass.getImageList()
        self.outputImageList = [self.imageList[0]]
        self.manager.get_screen('editScreen').createArea(self.imageList)

        # Creates the entirety of the slider and image sections


class SelectImages(Screen):
    def __init__(self, **kwargs):
        # Call to box layout constructor
        super(SelectImages, self).__init__(**kwargs)
        self.create()

    def create(self):
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
        if self.input_num.text.isdigit():
            chg = self.manager.get_screen('homeScreen')
            chg.submit(self.input_num.text)
            self.go_home(event)
        else:
            wrong_input = Popup(title='Please enter a valid number', content=Button(text="Confirm",
                                size_hint=(1, 0.5)), size_hint=(0.3, 0.3))
            wrong_input.content.bind(on_release=wrong_input.dismiss)
            wrong_input.open()
            self.input_num.text=''

class EditImages(Screen):
    def __init__(self, **kwargs):
        # Call to box layout constructor
        super(EditImages, self).__init__(**kwargs)

        self.export_info = {}
        self.image_edit = ImageEditSceen()
        # Creates the entirety of the slider and image sections
        self.list = []
        # Creating back button and new box layout for images and sliders
        back_button = Button(text='Home', size_hint=(1, 0.1), on_release=self.go_home)
        box = BoxLayout(orientation='vertical')
        self.warning = Label(text='No images to edit', size_hint=(1,0.1))
        #export_botton = Button(text='Export saved images', size_hint=(1, 0.1), on_release=self.export)
        self.export_button = Button(size_hint=(1, 0.1))
        # Adding created widgets to the user interface
        box.add_widget(back_button)
        box.add_widget(self.warning)
        box.add_widget(self.image_edit)
        #box.add_widget(export_botton)
        box.add_widget(self.export_button)
        self.add_widget(box)

    def createArea(self, imageList):
        self.image_list = imageList
        self.image_edit.createArea(imageList)
        if len(imageList) > 1 :
            self.warning.text = "Press Save Image before Next Image"


    def go_home(self, event):
        self.manager.transition.direction = 'right'
        self.manager.current = 'homeScreen'

    def handle_save(self,pos, rotation, scale, image_name):
        self.export_info[image_name] = (pos, rotation, scale)

    def handle_export(self):
        if self.image_edit.save_state == False:
            not_saved = Popup(title='You have not saved this image', content=BoxLayout(orientation='horizontal'),
                              size_hint=(0.2, 0.2), auto_dismiss=False)
            skip_button = Button(text='Skip', on_press=self.export, on_release=not_saved.dismiss)
            save_button = Button(text='Save', on_press=self.image_edit.send_save, on_release=not_saved.dismiss)
            not_saved.content.add_widget(skip_button)
            not_saved.content.add_widget(save_button)
            not_saved.open()
        else:
            self.export()

    def export(self):
        export_popup = Popup(title='Export in progress...',
                          size_hint=(0.2, 0.2))
        confirm_button = Button(text='Confirm', on_press=self.go_home, on_release=export_popup.dismiss)
        export_popup.content = confirm_button
        export_popup.open()
        self.manager.get_screen('homeScreen').outputImageList = [self.manager.get_screen('homeScreen').outputImageList[0]]
        self.manager.get_screen('homeScreen').outputImageList += imgAlign.imgAlign(self.export_info,self.image_list[0])
        export_popup.content = confirm_button
        export_popup.title = "Export Complete!"


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
        self.save_popup = Popup(title='Enter File Name:',
                             size_hint=(0.2, 0.2),auto_dismiss=False)
        self.text_box = TextInput(text='', size_hint=(1, 1), write_tab=False, multiline=False,
                                   on_text_validate=self.do_save)
        self.save_popup.content=self.text_box
        self.save_popup.open()
    def do_save(self,instance):
        self.save_popup.dismiss()
        self.save_popup.open()
        transpList = self.sliders.get_transparencies()
        slidesList = []
        for image in self.newImageList:
            slidesList.append(Image.open(image))
        imageOverlay.renderOverlay(slidesList, transpList, self.text_box.text.replace(".png", ""))
        self.save_popup.title = 'Export Complete'
        self.save_popup.content = Button(text='Confirm', on_release=self.save_popup.dismiss)
        self.save_popup.open()




# App Class
class UserInterface(App):
    # Build starting interface
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(HomeScreen(name="homeScreen"))
        screen_manager.add_widget(SelectImages(name="selectScreen"))
        return screen_manager


if __name__ == "__main__":
    window = UserInterface()
    window.run()
