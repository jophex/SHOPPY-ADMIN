from kivy import utils
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.image import AsyncImage
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

if utils.platform != 'android':
    Window.size = (360, 640)


class Foods(MDCard):
    pass


class Labels(MDLabel):
    pass


class MainApp(MDApp):
    # ------------------- SIZE----------------------- #

    size_x = NumericProperty(0)
    size_y = NumericProperty(0)

    # ------------- MAIN VARIABLES ---------------------#

    admin_name = StringProperty('joseph')
    orders = StringProperty('10')
    followers = StringProperty('389')




    def details(self):
        pass

    def test(self):
        for i in range(9):
            card = Foods(on_release=self.details)
            scroll = self.root.ids.Orders
            self.product_name = f'product {i}'
            self.product_price = f'price {i}/tsh'
            self.time = f' time 12:{i}, Thursday'
            self.company_name = i * 'aa'

            card.add_widget(AsyncImage(source='images/test.png'))
            card.add_widget(Labels(text=self.product_name, halign='center'))
            card.add_widget(Labels(text=self.product_price, halign='center'))
            card.add_widget(Labels(text=self.time, halign='center'))
            card.add_widget(Labels(text=self.company_name, halign='center'))

            card.id = f'product{i}'
            scroll.add_widget(card)

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.accent = "Brown"
        self.title = 'Shoppy Admin'
        self.size_x, self.size_y = Window.size


MainApp().run()
