from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget

from ImageBoxAndView import ImageBoxAndView
from ImageView import ImageView
import imageIn

class UI(BoxLayout):
    def __init__(self, **kwargs):

        super(UI, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.imageArea = BoxLayout(orientation='vertical')
        self.sideBar = GridLayout(cols=1, row_force_default=True, row_default_height=150)

        self.imageList = []
        self.imageObjList = []
        self.opacityList = []
        self.imageAreaFix = AnchorLayout(anchor_x='center', anchor_y='center')

    def reinit(self):
        self.imageList = []
        self.imageObjList = []
        self.opacityList = []
        self.imageArea.clear_widgets()
        self.sideBar.clear_widgets()
        self.imageAreaFix.clear_widgets()
        self.clear_widgets()
    def getImageList(self):
        return self.imageList

    def createImageObj(self,imageList):
        self.imageList = imageList
        for image in imageList:
            imageObj = ImageBoxAndView(image)
            self.imageObjList.append(imageObj)

    def showImageObj(self, imageInputList):
        if len(imageInputList) > 0:
            self.createImageObj(imageInputList)
            self.imageArea.add_widget(Widget(size_hint=(1, 0.4)))
            for image in self.imageObjList:
                self.imageAreaFix.add_widget(image.getView())
                self.sideBar.add_widget(image.getBox())

            self.imageArea.add_widget(self.imageAreaFix)
            self.imageArea.add_widget(Widget(size_hint=(1, 0.4)))

            self.add_widget(self.sideBar)
            self.add_widget(self.imageArea)

    def get_transparencies(self):
        transparency_list = []
        for image in self.imageObjList:
            transparency_list.append(int(image.get_opacity_value()))
        return transparency_list
