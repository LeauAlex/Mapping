import folium
import pandas
from geopy.geocoders import ArcGIS

n = ArcGIS()
z = n.geocode('Siriu, Buzau, Coltu Pietrii, Romania')


data = pandas.read_csv(r'C:\Users\Leau\Desktop\Python\Mapping\Volcanoes.txt')
lon = list(data['LON'])
lan = list(data['LAT'])
name = list(data['NAME'])
elev = list(data['ELEV'])


def elevation_interval(el):
    if 0<= el < 1000:
        return 'green'
    elif 1000 <= el < 2000:
        return 'orange'
    else:
        return 'red'


map_create = folium.Map(location= [-32.5, 20], zoom_start=6, tiles="Stamen Terrain") # map creation

fg = folium.FeatureGroup(name = 'My Map')
mk = folium.FeatureGroup(name = 'Markers')

for la,lo,nm,ev in zip(lan,lon,name,elev):
    mk.add_child(folium.CircleMarker(location=(la,lo), popup = "{},{} m".format(nm,ev) ,fill_color=elevation_interval(ev), fill = True, radius = 7, color = 'grey', fill_opacity = 0.7))  # add Marker

fg.add_child(folium.GeoJson(data = open(r'C:\Users\Leau\Desktop\Python\Mapping\world.json','r', encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

fgc = folium.FeatureGroup(name = 'Acasa la IZA')

def add_Marker(z):
    r = []
    x = n.geocode(z)
    r.append(x.longitude)
    r.append(x.latitude)
    return r


def locations():
        l = []
        input_location = input('Please add location: ')
        while input_location.lower() != 'stop':
            l.append(add_Marker(input_location))
            input_location = input('Please add location: ')
        return l


user_input = input('Do you want to add an location?: ')

def lists(user_input):
    if user_input.lower() == 'y':
        return locations()
    else:
        print('Ok then!')


z = lists(user_input)
for coordinates in z:
    fgc.add_child(folium.Marker(location=[coordinates[1], coordinates[0]], popup=' Acasa la Iza in Spania',icon=(folium.Icon(color='green'))))  # add Marker




map_create.add_child(fgc)

map_create.add_child(fg)
map_create.add_child(mk)

map_create.add_child(folium.LayerControl())

map_create.save('Map1.html')