#LMAO we gotta use Kivy now
#this is Abas file to tinker with

import kivy
# app refers to the instance of the app
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class KVBL(BoxLayout):
    #this just creates the boxlayout root widget used in the kv file
    pass
class KVBoxLayoutApp(App):
    def build(self):
        #returns instance of about class
        return KVBL
root= KVBoxLayoutApp()
root.run