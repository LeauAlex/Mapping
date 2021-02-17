import folium
from geopy.geocoders import ArcGIS

n = ArcGIS()
z = n.geocode('Siriu, Buzau, Coltu Pietrii, Romania')# using geocode to extract latitude and longitude


map_create = folium.Map(location= [z.latitude, z.longitude], zoom_start=6, tiles="Stamen Terrain") # map creation
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




map_creade.add_child(fgc)
map_create.save('Map_Iza.html')
