from kivy.app import App
from kivy.garden.mapview import MapView, MapMarkerPopup

class MapApp(App):
    def build(self):
        mapview = MapView(zoom=11, lat=51.5074, lon=-0.1278)  # London coordinates

        marker = MapMarkerPopup(lat=51.5074, lon=-0.1278, source='marker.png')
        mapview.add_marker(marker)

        return mapview

if __name__ == '__main__':
    MapApp().run()
