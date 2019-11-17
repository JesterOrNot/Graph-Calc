import fileinput
import os

import matplotlib.pyplot as plt
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
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
        root = BoxLayout(orientation='vertical')
        c = Imglayout()
        root.add_widget(c)

        self.im.keep_ratio = False
        self.im.allow_stretch = True
        cat = Button(text="Categories", size_hint=(1, .07))
        cat.bind(on_press=self.callback)
        c.add_widget(self.im)
        root.add_widget(cat)
        return root

    def callback(self, value):
        self.im = Image(source='images/graph.png')


def graph():
    x = [1, 2, 3]
    y = [2, 4, 6]
    plt.plot(x, y)
    plt.savefig("graph.png")
    os.system("mv graph.png images")


if __name__ == '__main__':
    graph()
    MainTApp().run()
