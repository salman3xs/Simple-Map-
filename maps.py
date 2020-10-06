import folium
import pandas

data = pandas.read_csv('Volcanoes_USA.txt')

lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
el = list(data['ELEV'])


def color_sel(elv):
    if elv < 1000:
        return 'green'
    elif elv < 2000:
        return 'orange'
    else:
        return 'red'


m = folium.Map(location=[48, -120], zoom_start=5, tiles='Mapbox Bright')

fgv = folium.FeatureGroup(name='maps')

for lt, ln, nm, el in zip(lat, lon, name, el):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=str(nm), icon=folium.Icon(color=color_sel(el))))

fgp = folium.FeatureGroup(name='pop')

fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 20000000 else'red'}))

m.add_child(fgv)
m.add_child(fgp)
m.add_child(folium.LayerControl())

m.save('map.html')
