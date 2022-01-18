from kivy import utils
import datetime
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.image import AsyncImage
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy import Config
import os

Config.set('graphics', 'multisamples', '0')

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
if utils.platform != 'android':
    Window.size = (360, 640)


class Foods(MDCard):
    pass


class Products(MDCard):
    pass


class Labels(MDLabel):
    pass


class MainApp(MDApp):
    # ------------------- SIZE----------------------- #
    size_x = NumericProperty(0)
    size_y = NumericProperty(0)

    # ------------- MAIN VARIABLES ---------------------#

    orders = StringProperty('')
    oders2 = NumericProperty(1)
    times = str(datetime.datetime.now())
    timess = times.split('.')
    products_screen = StringProperty(' ')



    def test(self):
        for i in range(self.oders2):
            card = Foods()
            scroll = self.root.ids.Orders
            self.orders = f'{i}'
            self.product_name = f'product {i}'
            self.product_price = f'price {i}/tsh'
            self.time = f'{self.timess[0]}'
            self.company_name = i * 'aa'

            card.md_bg_color = 8 / 225, 18 / 225, 115 / 225, 1
            card.add_widget(AsyncImage(source='images/test.png'))
            card.add_widget(Labels(text=self.product_name, halign='center'))
            card.add_widget(Labels(text=self.product_price, halign='center'))
            card.add_widget(Labels(text=self.time, halign='center'))
            card.add_widget(Labels(text=self.company_name, halign='center'))
            card.add_widget(Labels(text=self.orders, halign='center'))

            card.id = f'product{i}'
            scroll.add_widget(card)

    def product(self):
        for i in range(1):
            products = Products(on_release=self.details)
            scroll = self.root.ids.products

            self.product_names = f'name {i}'
            self.price_products = f'price {i}'

            products.add_widget(AsyncImage(source='images/test.png'))
            products.add_widget(Labels(text=self.product_names, halign='center'))
            products.add_widget(Labels(text=self.price_products, halign='center'))

            products.id = f'product{i}'
            scroll.add_widget(products)

    def details(self, instance):

        sm = self.root
        sm.current = "products_details"

        self.products_screen = instance.id







    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.accent = "Brown"
        self.title = 'Shoppy Admin'
        self.size_x, self.size_y = Window.size


MainApp().run()
