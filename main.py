from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file('tr.kv')

class MainScreen(ScreenManager):
    def close(self):
       print('2, pressed') 
    def command(self):
        print('command pressed')
    def clear_command(self):
        self.ids.command.text = ''
    def video(self, type):
        print(type)
    def image(self, type):
        print(type)

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()
