from kivy.graphics import Rectangle, Color
from kivy.graphics.transformation import Matrix
from kivy.metrics import dp
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.app import App


class MoveMe(Scatter):
    def __init__(self, **kwargs):
        super(MoveMe, self).__init__(**kwargs)
        self.size = (dp(500),dp(500))
        #self.bind(pos=self.updateCanvas, size=self.updateCanvas)
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

# App Class
class UserInterface(App):
    # Build starting interface
    def build(self):
        widgetContainer = MoveMe()
        widgetContainer.add_widget(Image(source = 'Images/L03.png', size = (dp(300),dp(300))))
        return widgetContainer


if __name__ == "__main__":
    window = UserInterface()
    window.run()