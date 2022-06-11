

from kivy.app import App
from kivy.graphics import Rectangle, Color, Line
from kivy.graphics.transformation import Matrix
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scatter import Scatter
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.slider import Slider
from kivy.uix.stencilview import StencilView
from kivy.uix.widget import Widget


class ImageEditSceen(FloatLayout):
    def __init__(self, imageList, **kwargs):
        super(ImageEditSceen, self).__init__(**kwargs)
        self.imageArea = ImageEdit()
        self.imageSlider = ImageEditSlider("L15.png")
        self.add_widget(self.imageSlider)
        self.add_widget(self.imageArea)


class ImageEditSlider(GridLayout):
    def __init__(self, imageName, **kwargs):
        super(ImageEditSlider, self).__init__(**kwargs)
        self.size_hint = (1, 0.2)
        self.pos_hint = {"top": 1, "left": 1}
        self.rows = 1
        # grid for slider and label
        self.grid = GridLayout(cols=1)
        # make slider
        self.slider = Slider(min=0, max=100)
        # add slider and label
        self.grid.add_widget(Label(text="Transparency for " + imageName, size_hint=(1, 0.5)))
        self.grid.add_widget(self.slider)
        # add grid to overall grid
        self.add_widget(self.grid)
        # make save button
        self.saveButton = Button(text='Save Aligned Image', size_hint=(0.4, 1))
        # add save button to overall grid
        self.add_widget(self.saveButton)


class ImageEdit(GridLayout):
    def __init__(self, **kwargs):
        super(ImageEdit, self).__init__(**kwargs)
        self.cols = 1
        self.pos_hint = {"top": 0.795, "left" : 1 }
        self.size_hint = (1, .795)

        self.imageBox = ImageBox()
        self.add_widget(self.imageBox)


class ImageBox(StencilView):
    def __init__(self, **kwargs):
        super(ImageBox, self).__init__(**kwargs)
        self.scatter = ImageAlign('L15.png',  0.9*float(self.width),
                                              0.9*float(self.height),
                                              self.pos, pos=self.pos, auto_bring_to_front=True)
        backImage = 'L15 XPL.png'
        self.backImage = Image(source=backImage, height=0.9*float(self.height), width=0.9*float(self.width))
        self.add_widget(self.backImage)
        self.add_widget(self.scatter)
        self.bind(pos=self.updateBackImage, size=self.updateBackImage)

    def updateBackImage(self, instance, value):
        self.scatter.image.width = 0.9*float(self.width)
        self.scatter.image.height = 0.9*float(self.height)
        self.scatter.image.pos = self.pos

        self.scatter.size = self.scatter.image.size

        self.backImage.width = 0.9 * float(self.width)
        self.backImage.height = 0.9 * float(self.height)
        self.backImage.pos = self.pos


class ImageAlign(Scatter):
    def __init__(self, imageName, imageWidth, imageHeight, imagePos, **kwargs):
        super(ImageAlign, self).__init__(**kwargs)
        # set size and position
        self.image = Image(source=imageName, size=(imageWidth, imageHeight), pos=imagePos, opacity=0.66)
        self.size = self.image.size
        # prevent zooming while rotating
        self.do_scale = False
        # add image
        self.add_widget(self.image)

    # change default on touch to include a mouse wheel scroll for zooming.
    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                if self.scale < 10:
                    self.apply_transform(Matrix().scale(1.01, 1.01, 1.01), anchor=touch.pos)
            if touch.button == 'scrollup':
                if self.scale > 0.5:
                    self.apply_transform(Matrix().scale(1.0 / 1.01, 1.0 / 1.01, 1.0 / 1.01), anchor=touch.pos)
        else:
            super(ImageAlign, self).on_touch_down(touch)