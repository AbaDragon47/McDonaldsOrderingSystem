#LMAO we gotta use Kivy now
#this is Abas file to tinker with

import kivy
# app refers to the instance of the app
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='[b]Hello[\b] [color=ff0099]World[/color]\\n')
MyApp().run()