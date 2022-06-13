from tkinter import Button
from kivy.app import App
from kivy.graphics import Rectangle, Color, Line
from kivy.graphics.transformation import Matrix
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget



class MoveMe(Scatter):
    def __init__(self, **kwargs):
        super(MoveMe, self).__init__(**kwargs)
        self.size = (dp(500),dp(500))
        self.do_scale=False
    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                if self.scale < 10:
                    self.apply_transform(Matrix().scale(1.05, 1.05, 1.05),
                                         anchor=touch.pos)
            if touch.button == 'scrollup':
                if self.scale > 0.5:
                    self.apply_transform(Matrix().scale(1.0 / 1.05, 1.0 / 1.05, 1.0 / 1.05),
                                         anchor=touch.pos)
        else:
            super(MoveMe, self).on_touch_down(touch)

class UserInterface(App):
    def build(self):
        box = BoxLayout()
        button = Button()
        scatter = MoveMe()
        #scatter.auto_bring_to_front = True
        image = Image(source="Images/L15.png",size=(dp(500),dp(500)))
        scatter.add_widget(image)
        return scatter

# creating the object root for ButtonApp() class
#UserInterface().run()