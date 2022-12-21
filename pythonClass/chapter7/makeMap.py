import folium
import folium as f

# lat, long = 37.52860, 126.93431

lat = [37.52860, 37.52400, 37.51865]

long = [126.93431, 126.91889, 126.92041]

map_y = f.Map([37.52860, 126.93431], zoom_start=15)

name = ["여의도 한강공원", "여의도 공원", "샛강생태공원"]

color = ["red", "blue", "gray"]

icon = ["star", "home", "automobile"]

for i in range(3):
    f.Marker(
        [lat[i], long[i]], tooltip=name[i],
        icon=folium.Icon(color=color[i], icon=icon[i], prefix="fa")
    ).add_to(map_y)

map_y.save('index.html')


