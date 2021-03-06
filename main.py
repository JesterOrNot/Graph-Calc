import fileinput
import os
import shutil

import matplotlib.pyplot as plt
import numpy as np
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class Imglayout(FloatLayout):

    def __init__(self, **args):
        super(Imglayout, self).__init__(**args)

        with self.canvas.before:
            Color(0, 0, 0, 0)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.updates, pos=self.updates)

    def updates(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos


class MainTApp(App):

    im = Image(source='images/graph.png')

    def build(self):
        try:
            os.remove("images/graph.png")
        except Exception:
            pass
        self.root = GridLayout()
        self.root.cols = 4
        c = Imglayout()
        global x
        self.x = TextInput()
        submit = Button(text="Submit.")
        submit.bind(on_press=self.callback)
        # submit.bind(on_press=self.myfunc)
        self.root.add_widget(c)
        self.im.keep_ratio = True
        self.im.allow_stretch = True
        c.add_widget(self.im)
        self.root.add_widget(self.x)
        self.root.add_widget(submit)
        return self.root
    def callback(self, instance):
        try:
            os.remove("images/graph.png")
            shutil.move("graph.png", "images")
        except Exception:
            pass
        x = np.linspace(-10, 10)
        y = eval(self.x.text)
        plt.plot(x, y)
        plt.savefig("graph.png")
        self.im.source = 'images/graph.png'
        self.root.remove_widget(self.im)
        self.im.reload()


if __name__ == '__main__':
    MainTApp().run()
