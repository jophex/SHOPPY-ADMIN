from kivy import utils
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon

if utils.platform != 'android':
    Window.size = (360, 640)


class me(MDIcon):
    pass


class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.theme_style = "Light"
        self.title = 'Shoppy Admin'


MainApp().run()
