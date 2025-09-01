import folium
import requests
from geopy.distance import geodesic
def get_current_location():
    try:
        response = requests.get('http://ipinfo.io/json')
        data = response.json()
        loc = data['loc'].split(',')
        return [float(loc[0]), float(loc[1])]
    except:
        return [26.8206, 30.8025]  # Default location in Egypt if location fetch fails

current_location = get_current_location()
tourist_attractions = {
    "Pyramids": {"location": (29.9792, 31.1342), "image": "pyramids.jpg"},
    "Karnak Temple": {"location": (25.7188, 32.6573), "image": "karnak_temple.jpg"},
    "Fayoum Oasis": {"location": (29.3084, 30.8438), "image": "fayoum_oasis.jpg"},
    "Mount Sinai": {"location": (28.5392, 33.9754), "image": "mount_sinai.jpg"},
    "Wax Museum": {"location": (30.0331, 31.2244), "image": "wax_museum.jpg"},
    "Louvre Museum": {"location": (30.0596, 31.2001), "image": "louvre_museum.jpg"},
    "Luxor City": {"location": (25.6872, 32.6396), "image": "luxor_city.jpg"},
    "Egyptian Museum": {"location": (30.0478, 31.2336), "image": "egyptian_museum.jpg"},
    "Citadel of Salah El-Din": {"location": (30.0299, 31.2613), "image": "citadel.jpg"},
    "Philae Temple": {"location": (24.0240, 32.8844), "image": "philae_temple.jpg"},
    "Abu Simbel Temples": {"location": (22.3372, 31.6258), "image": "abu_simbel.jpg"},
    "Alexandria Library": {"location": (31.2089, 29.9092), "image": "alexandria_library.jpg"},
    "Montaza Palace": {"location": (31.2865, 30.0205), "image": "montaza_palace.jpg"},
    "Siwa Oasis": {"location": (29.2041, 25.5193), "image": "siwa_oasis.jpg"},
    "Dahab": {"location": (28.5095, 34.5136), "image": "dahab.jpg"},
    "Sharm El Sheikh": {"location": (27.9158, 34.3299), "image": "sharm_sheikh.jpg"},
    "Hurghada": {"location": (27.2579, 33.8116), "image": "hurghada.jpg"},
    "Temple of Hatshepsut": {"location": (25.7376, 32.6066), "image": "hatshepsut_temple.jpg"},
    "Valley of the Kings": {"location": (25.7402, 32.6014), "image": "valley_kings.jpg"},
    "Nubian Museum": {"location": (24.0871, 32.8989), "image": "nubian_museum.jpg"},
    "White Desert": {"location": (27.2236, 28.1538), "image": "white_desert.jpg"},
    "Saint Catherine's Monastery": {"location": (28.5558, 33.9760), "image": "saint_catherine.jpg"}

}

map_egypt = folium.Map(location=current_location, zoom_start=6)
folium.Marker(
    location=current_location,
    popup="My Current Location",
    icon=folium.Icon(color="green")
).add_to(map_egypt)

def calculate_distance(current_location, tourist_location):
    return geodesic(current_location, tourist_location).km

for name, place in tourist_attractions.items():
    distance = calculate_distance(current_location, place["location"])
    popup_html = f"<img src='{place['image']}' alt='{name}' style='width:200px;height:150px;'><br>{name}<br>Distance: {distance:.2f} km"
    folium.Marker(location=place["location"], popup=popup_html).add_to(map_egypt)

map_egypt.save("map.html")
