from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget

from ImageBoxAndView import ImageBoxAndView
from ImageView import ImageView
from ImageIN import imageIn

class UI(BoxLayout):
    def __init__(self, **kwargs):

        super(UI, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.imageArea = BoxLayout(orientation='vertical')
        self.sideBar = GridLayout(cols=1, row_force_default=True, row_default_height=150)

        self.imageList = [] #['Images/L15.png', 'Images/L15 XPL.png']
        self.imageObjList = []
        self.imageAreaFix = AnchorLayout(anchor_x='center', anchor_y='center')



    def getImageList(self):
        return self.imageList

    def createImageObj(self,imageList):
        for image in imageList:
            imageObj = ImageBoxAndView(image)
            self.imageObjList.append(imageObj)
    def showImageObj(self, imageInputList):
        self.createImageObj(imageInputList)
        self.imageArea.add_widget(Widget(size_hint=(1, 0.4)))
        for image in self.imageObjList:
            self.imageAreaFix.add_widget(image.getView())
            self.sideBar.add_widget(image.getBox())

        self.imageArea.add_widget(self.imageAreaFix)
        self.imageArea.add_widget(Widget(size_hint=(1, 0.4)))

        self.add_widget(self.sideBar)
        self.add_widget(self.imageArea)

