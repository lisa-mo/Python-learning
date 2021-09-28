import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""


def color_maker(elevation):
    if elevation < 500:
        return 'green'
    elif 500 <= elevation < 1500:
        return 'orange'
    else:
        return 'red'


beach_map = folium.Map(location=[39.46287349798747, -118.3212552739576], zoom_start=5)
# tiles="Stamen Terrain" works incorrect and is needed to be fixed or replaced

volcanoes_feature_group = folium.FeatureGroup(name="The Volcanoes Map")
population_feature_group = folium.FeatureGroup(name="The Population Map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    volcanoes_feature_group.add_child(folium.CircleMarker(location=(lt, ln), radius=8, popup=folium.Popup(iframe),
                                                          fill_color=color_maker(el), color='white', fill_opacity=0.5))

population_feature_group.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                                                  style_function=lambda x: {'fillColor': 'grey' if
                                                  x['properties']['POP2005'] < 5000000 else 'light-blue'}))

beach_map.add_child(volcanoes_feature_group)
beach_map.add_child(population_feature_group)
beach_map.add_child(folium.LayerControl())
beach_map.save("This_is_a_beach_map.html")
