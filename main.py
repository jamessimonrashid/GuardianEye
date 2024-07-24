from kivy.uix.actionbar import BoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
import threading
from kivy.uix.screenmanager import Screen, ScreenManager
#from kivymd.uix.scrollview import scrollview
from kivy.garden.mapview import MapView, MapMarkerPopup
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton
import geocoder

class Main(Screen):
    pass
class AddAccountScreen(Screen):
    pass
class ImageScreen(Screen):
    pass
class VideoScreen(Screen):
    pass
class LocationScreen(Screen, MapView):
    def __init__(self, **kwargs):
        super(LocationScreen, self).__init__(**kwargs)

        # Create a BoxLayout for the screen content
        layout = BoxLayout(orientation='vertical')

        mapview = MapView(zoom=11, lat=51.5074, lon=-0.1278)  # London coordinates

        marker = MapMarkerPopup(lat=51.5074, lon=-0.1278, source='marker.png')
        mapview.add_marker(marker)
        layout.add_widget(MDIconButton(icon='home', on_release=self.Switch))
        layout.add_widget(mapview)

        self.add_widget(layout)
    def Switch(self, instance):
        self.manager.current = 'main'
class FileScreen(Screen):
    pass
class masterApp(MDApp):
    def build(self):
        Builder.load_file('nw.kv')
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "Orange"
        sm = ScreenManager()
        sm.add_widget(Main(name='main'))
        sm.add_widget(ImageScreen(name='image'))
        sm.add_widget(VideoScreen(name='video'))
        sm.add_widget(LocationScreen(name='location'))
        sm.add_widget(FileScreen(name='file'))
        sm.add_widget(AddAccountScreen(name='account'))

        return sm
    def change(self, cur):
        if cur == 'location':
            print('location')

            self.root.current = 'location'
            
        elif cur == 'video':
            self.root.current = 'video'
        elif cur == 'image':
            self.root.current = 'image'
        elif cur == 'file':
            self.root.current = 'file' 
        elif cur == 'main':
            self.root.current = 'main' 
        elif cur == 'add_account':
            self.root.current = 'account'
    def screen_record_file(self):
        print('files')
if __name__ == '__main__':
    masterApp().run()
