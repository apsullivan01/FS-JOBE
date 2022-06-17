import math

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
    def __init__(self, **kwargs):
        super(ImageEditSceen, self).__init__(**kwargs)



    def createArea(self,imageList):
        if len(imageList) > 1:
            self.on_image = 1
            self.image_list = imageList
            self.imageArea = ImageEdit(imageList[self.on_image], imageList[0])
            self.imageSlider = ImageEditSlider(imageList[1], 1, len(imageList)-1)
            self.imageSlider.slider.bind(value=self.imageArea.imageBox.scatter.change_opacity)
            if len(self.image_list) > 2:
                self.imageSlider.next_button.text = 'Next Image'
                self.imageSlider.next_button.bind(on_release=self.next_image)
            else:
                self.parent.parent.export_button.text = 'Export saved images'
                self.parent.parent.export_button.on_release = self.parent.parent.export
            self.imageSlider.save_button.bind(on_release=self.send_save)
            self.add_widget(self.imageSlider)
            self.add_widget(self.imageArea)


    def next_image(self, instance):
        self.on_image += 1
        self.clear_widgets()
        self.imageArea = ImageEdit(self.image_list[self.on_image], self.image_list[0])
        self.imageSlider = ImageEditSlider(self.image_list[self.on_image],self.on_image, len(self.image_list)-1)
        self.imageSlider.slider.bind(value=self.imageArea.imageBox.scatter.change_opacity)
        if (len(self.image_list)-1) > self.on_image:
            self.imageSlider.next_button.text = 'Next Image'
            self.imageSlider.next_button.bind(on_release=self.next_image)
        else:
            self.parent.parent.export_button.text = 'Export saved images'
            self.parent.parent.export_button.on_release = self.parent.parent.export

        self.imageSlider.save_button.bind(on_release=self.send_save)
        self.add_widget(self.imageSlider)
        self.add_widget(self.imageArea)

    def send_save(self,instance):
        box = self.imageArea.imageBox
        x = box.scatter.x - box.init_x
        y = box.scatter.y - box.init_y
        #(x)
        #print(box.scatter.pos)
        #print(box.backImage.norm_image_size)
        #y = scatter.heigh + y
        pos = (x*2/(box.backImage.norm_image_size[0]), y*2/box.backImage.norm_image_size[1])
        rotation = box.scatter.rotation
        scale = box.scatter.scale
        self.parent.parent.handle_save(pos, rotation, scale, self.image_list[self.on_image])





class ImageEditSlider(GridLayout):
    def __init__(self, imageName, on_image, num_images, **kwargs):
        super(ImageEditSlider, self).__init__(**kwargs)
        self.size_hint = (1, 0.2)
        self.pos_hint = {"top": 1, "left": 1}
        self.rows = 1
        # grid for slider and label
        self.grid = GridLayout(cols=1)
        # make slider
        self.slider = Slider(min=0, max=1.0,value=0.66)
        # add slider and label
        string_name = imageName[imageName.rfind('/')+1:]
        self.grid.add_widget(Label(text=("Image " + str(on_image) + " of " + str(num_images) + ": " + string_name), size_hint=(1, 0.5)))
        self.grid.add_widget(self.slider)
        # add grid to overall grid
        self.add_widget(self.grid)
        # make save button
        self.save_button = Button(text='Save Image', size_hint=(0.4, 1))
        # make next button
        self.next_button = Button(size_hint=(0.4, 1))
        # add save and next button to overall grid
        self.add_widget(self.save_button)
        self.add_widget(self.next_button)


class ImageEdit(GridLayout):
    def __init__(self, editImage, backImage, **kwargs):
        super(ImageEdit, self).__init__(**kwargs)
        self.cols = 1
        self.pos_hint = {"top": 0.795, "left" : 1 }
        self.size_hint = (1, .795)

        self.imageBox = ImageBox(editImage, backImage)
        self.add_widget(self.imageBox)


class ImageBox(StencilView):
    def __init__(self, editImage, backImage, **kwargs):
        super(ImageBox, self).__init__(**kwargs)
        self.backImage = Image(source=backImage, height=self.height, width=self.width,pos = self.pos)
        self.scatter = ImageAlign(editImage, x=50, y=50, size=self.backImage.norm_image_size, auto_bring_to_front=True)
        self.add_widget(self.backImage)
        self.add_widget(self.scatter)
        self.bind(pos=self.updateImage, size=self.updateImage)


    def updateImage(self, instance, value):
        self.backImage.width = self.width
        self.backImage.height = self.height
        self.backImage.pos = self.pos

        self.scatter.size = self.backImage.norm_image_size
        self.scatter.pos = (((self.size[0] - self.backImage.norm_image_size[0])/4),
                              self.parent.parent.parent.parent.export_button.height/2)
        self.init_x = (self.size[0] - self.backImage.norm_image_size[0])/4
        self.init_y = self.parent.parent.parent.parent.export_button.height/2


class ImageAlign(Scatter):
    def __init__(self, imageName, **kwargs):
        super(ImageAlign, self).__init__(**kwargs)
        # set size and position
        self.image = Image(source=imageName, size=self.size, pos=self.pos, opacity=0.66)
        # prevent zooming while rotating
        self.do_rotation = False
        self.do_scale = False
        # add image
        self.add_widget(self.image)
        self.bind(pos=self.updateCanvas, size=self.updateCanvas)
        with self.canvas:
            Color(1,1,1,1)
            x,y = self.pos
            self.bg = Line(rectangle=(x,y,self.width,self.height))

    def updateCanvas(self, *args):
        self.bg.rectangle = (self.x,self.y,self.width,self.height)
        self.image.size = self.size
        self.image.pos = self.pos
    # change default on touch to include a mouse wheel scroll for zooming.

    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                if self.scale < 10:
                    self.apply_transform(Matrix().scale(1.01, 1.01, 1.01), anchor=(self.center_x,self.center_y+100))
            if touch.button == 'scrollup':
                if self.scale > 0.1:
                    self.apply_transform(Matrix().scale(1.0 / 1.01, 1.0 / 1.01, 1.0 / 1.01), anchor=(self.center_x,self.center_y))

        else:
            super(ImageAlign, self).on_touch_down(touch)
        '''elif touch.button == 'right':
                    y = (touch.y - self.center[1])
                    x = (touch.x - self.center[0])
                    calc = math.degrees(math.atan2(y, x))
                    self.prev_angle = calc if calc > 0 else 360 + calc
                    self.tmp = self.rotation'''

    def change_opacity(self, instance, opacity):
        self.image.opacity = opacity

    '''def on_touch_move(self, touch):
        if touch.button == 'right':
            y = (touch.y - self.center[1])
            x = (touch.x - self.center[0])
            calc = math.degrees(math.atan2(y, x))
            new_angle = calc if calc > 0 else 360+calc
            rot = self.rotation + (new_angle-self.prev_angle)%360
            mat = Matrix().rotate(rot,0,0,1)
            self.apply_transform(mat,anchor=(self.x + self.width/2,self.y + self.height/2))
        else:
            super(ImageAlign, self).on_touch_move(touch)'''