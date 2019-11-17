import fileinput
import os

import matplotlib.pyplot as plt
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
        root = GridLayout()
        root.cols=3
        root.rows=2
        c = Imglayout()
        x = TextInput()
        y = TextInput()
        submit = Button(text="Submit.")
        root.add_widget(c)
        self.im.keep_ratio = False
        self.im.allow_stretch = True
        c.add_widget(self.im)
        root.add_widget(x,2)
        root.add_widget(submit)
        return root

    def callback(self, value):
        self.im = Image(source='images/graph.png')


def graph(x,y):
    plt.plot(x, y)
    plt.savefig("graph.png")
    os.system("mv graph.png images")


if __name__ == '__main__':
    graph([1,2,3],[2,4,6])
    MainTApp().run()
