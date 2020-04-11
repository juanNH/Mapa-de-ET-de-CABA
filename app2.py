
import folium
import pandas
df = pandas.read_csv("escuelas.txt")
map2 = folium.Map(location=[-34.606930, -58.436925],zoom_start=13,titles="pc")
for tool,lat,lon,nombre in zip(df["TOOL"],df["LAT"],df["LON"],df["NOMBRE"]):
    folium.Marker([lat, lon], popup=nombre, marker_color="red",tooltip=tool).add_to(map2)
map2.save('app_test2.html')

