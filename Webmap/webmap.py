import folium
import pandas

map=folium.Map(location=[40,-120], zoom_start=5, tiles="Mapbox Bright")
data=pandas.read_csv("Volcanoes_USA.txt")
lon=list( data["LON"])
lat=list(data["LAT"])
nam=list(data["NAME"])
elev=list(data["ELEV"])

def elevcolor(elavation):
    if el<2000:
        return 'green'
    elif el>=2000 and el<3000:
        return 'orange'
    else:
        return 'red'

fgv=folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup = str(el),
    fill=True, fill_color= elevcolor(el), color=elevcolor(el), fill_opacity = 0.2))

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
style_function=lambda x: {'fillColor':'red' if x['properties']['POP2005'] < 10000000
else 'yellow' if 10000000 <= x['properties']['POP2005']< 20000000 else 'green'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("webmap1.html")
