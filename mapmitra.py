import folium
import openrouteservice
import time
from IPython.display import display, clear_output
import random
import sys


import webbrowser

# Function to open the link
def open_link():
    url = "https://colab.research.google.com/drive/1oxH1XknyArEHz4AHbB2h7TJYgVucFwU_?usp=sharing"
    webbrowser.open(url)

# Call the function
open_link()

api_key = '5b3ce3597851110001cf62487dab724e881e4bfeab36d60cd37e61f6'
client = openrouteservice.Client(key=api_key)

start_coords = (28.8567367, 77.0984433)
end_coords = (28.808122, 77.049466)

#https://colab.research.google.com/drive/1oxH1XknyArEHz4AHbB2h7TJYgVucFwU_?usp=sharing

route = client.directions(coordinates=[(start_coords[1], start_coords[0]), (end_coords[1], end_coords[0])], profile='driving-car', format='geojson')
route_coords = [(coord[1], coord[0]) for coord in route['features'][0]['geometry']['coordinates']]
car_map = folium.Map(location=[start_coords[0], start_coords[1]], zoom_start=14)
folium.GeoJson(route, name='route').add_to(car_map)

folium.Marker(
    location=[start_coords[0], start_coords[1]],
    popup='Start',
    icon=folium.Icon(color='green')
).add_to(car_map)

folium.Marker(
    location=[end_coords[0], end_coords[1]],
    popup='End',
    icon=folium.Icon(color='red')
).add_to(car_map)
coords_path = [[lon, lat] for lon, lat in zip(path_points['Longitude'], path_points['Latitude'])]

for lat, lon, junction, signal, district, green_light, changing_time, speed_limit in points:
    folium.Marker(
        location=[lat, lon],
        popup=(
            f'Junction: {junction}<br>'
            f'Signal: {signal}<br>'
            f'District: {district}<br>'
            f'Green Light: {green_light}<br>'
            f'Changing Time: {changing_time} s<br>'
            f'Speed Limit: {speed_limit} km/h'
        ),
        icon=folium.Icon(color='green')
    ).add_to(car_map)

distance = route['features'][0]['properties']['segments'][0]['distance'] / 1000
duration = route['features'][0]['properties']['segments'][0]['duration'] / 60

folium.map.Marker(
    [start_coords[0], start_coords[1]],
    icon=folium.DivIcon(
        html=f'<div style="font-size: 16pt">Distance: {distance:.2f} km<br>Duration: {duration:.2f} min</div>'
    )
).add_to(car_map)


car_map.save('car_movement_directions_map.html')

display(car_map)


for i in range(len(route_coords)):
    current_coords = route_coords[i]
    clear_output(wait=True)
    car_map = folium.Map(location=current_coords, zoom_start=14)
    folium.GeoJson(route, name='route').add_to(car_map)
    folium.Marker(
        location=[start_coords[0], start_coords[1]],
        popup='Start',
        icon=folium.Icon(color='green')
    ).add_to(car_map)

    folium.Marker(
        location=[end_coords[0], end_coords[1]],
        popup='End',
        icon=folium.Icon(color='red')
    ).add_to(car_map)

    folium.PolyLine(locations=route_coords[:i+1], color='blue').add_to(car_map)

    speed_limit = random.uniform(35, 37)

    print(f'Current speed limit: {speed_limit:.2f} km/h')

    folium.Marker(
        location=current_coords,
        popup=f'Speed Limit: {speed_limit:.2f} km/h',
        icon=folium.Icon(color='red')
    ).add_to(car_map)

    # Display the map
    display(car_map)

    time.sleep(0.1)

# Your OpenRouteService API key
api_key = '5b3ce3597851110001cf62487dab724e881e4bfeab36d60cd37e61f6'
client = openrouteservice.Client(key=api_key)

# Sample path points data
path_points = {
    'Longitude': [77.0984433, 77.088433, 77.078423, 77.068413, 77.058403, 77.049466],
    'Latitude': [28.8567367, 28.8467267, 28.8367167, 28.8267067, 28.8166967, 28.808122]
}

# Sample points data for additional markers
points = [
    (28.8567367, 77.0984433, 'Junction1', 'Signal1', 'District1', 'Yes', 30, 50),
    (28.8467267, 77.088433, 'Junction2', 'Signal2', 'District2', 'Yes', 45, 60),
    (28.8367167, 77.078423, 'Junction3', 'Signal3', 'District3', 'No', 60, 70),
    (28.8267067, 77.068413, 'Junction4', 'Signal4', 'District4', 'Yes', 15, 40),
    (28.8166967, 77.058403, 'Junction5', 'Signal5', 'District5', 'No', 50, 30),
    (28.808122, 77.049466, 'Junction6', 'Signal6', 'District6', 'Yes', 25, 55)
]

# Convert path points to coordinates
coords_path = [(lat, lon) for lon, lat in zip(path_points['Longitude'], path_points['Latitude'])]

# Generate route that follows the road
def get_route(client, start, end):
    route = client.directions(coordinates=[(start[1], start[0]), (end[1], end[0])], profile='driving-car', format='geojson')
    return [(coord[1], coord[0]) for coord in route['features'][0]['geometry']['coordinates']]

# Combine all segments
full_route = []
for i in range(len(coords_path) - 1):
    segment = get_route(client, coords_path[i], coords_path[i+1])
    full_route.extend(segment if i == 0 else segment[1:])  # avoid duplicate points

# Initial map setup
car_map = folium.Map(location=[coords_path[0][0], coords_path[0][1]], zoom_start=14)

# Add start and end markers
folium.Marker(
    location=[coords_path[0][0], coords_path[0][1]],
    popup='Start',
    icon=folium.Icon(color='green')
).add_to(car_map)

folium.Marker(
    location=[coords_path[-1][0], coords_path[-1][1]],
    popup='End',
    icon=folium.Icon(color='red')
).add_to(car_map)

# Add additional markers from points data
for lat, lon, junction, signal, district, green_light, changing_time, speed_limit in points:
    folium.Marker(
        location=[lat, lon],
        popup=(
            f'Junction: {junction}<br>'
            f'Signal: {signal}<br>'
            f'District: {district}<br>'
            f'Green Light: {green_light}<br>'
            f'Changing Time: {changing_time} s<br>'
            f'Speed Limit: {speed_limit} km/h'
        ),
        icon=folium.Icon(color='green')
    ).add_to(car_map)

    # Retrieve argument passed from Node.js
    data = sys.argv[1] if len(sys.argv) > 1 else 'No input received'
    result = f"Hello from Python! Received: {data}"
    print(result)

if __name__ == "__main__":

# Save the initial map
car_map.save('car_movement_directions_map.html')
display(car_map)

# Animate car movement through full_route
for i in range(len(full_route)):
    current_coords = full_route[i]
    clear_output(wait=True)
    car_map = folium.Map(location=current_coords, zoom_start=14)

    # Add start and end markers
    folium.Marker(
        location=[coords_path[0][0], coords_path[0][1]],
        popup='Start',
        icon=folium.Icon(color='green')
    ).add_to(car_map)

    folium.Marker(
        location=[coords_path[-1][0], coords_path[-1][1]],
        popup='End',
        icon=folium.Icon(color='red')
    ).add_to(car_map)

    # Draw the route path
    folium.PolyLine(locations=full_route[:i+1], color='blue').add_to(car_map)

    # Simulate a random speed limit for the current position
    speed_limit = random.uniform(35, 37)
    print(f'Current speed limit: {speed_limit:.2f} km/h')

    # Add a marker for the current position with speed limit
    folium.Marker(
        location=current_coords,
        popup=f'Speed Limit: {speed_limit:.2f} km/h',
        icon=folium.Icon(color='red')
    ).add_to(car_map)

    # Display the updated map
    display(car_map)

    # Pause briefly to create an animation effect
    time.sleep(0.1)

# Your OpenRouteService API key
api_key = '5b3ce3597851110001cf62487dab724e881e4bfeab36d60cd37e61f6'
client = openrouteservice.Client(key=api_key)

# Sample path points data
path_points = {
    'Longitude': [77.0984433, 77.088433, 77.078423, 77.068413, 77.058403, 77.049466],
    'Latitude': [28.8567367, 28.8467267, 28.8367167, 28.8267067, 28.8166967, 28.808122]
}

# Sample points data for additional markers
points = [
    (28.8567367, 77.0984433, 'Junction1', 'Signal1', 'District1', 'Yes', 30, 50),
    (28.8467267, 77.088433, 'Junction2', 'Signal2', 'District2', 'Yes', 45, 60),
    (28.8367167, 77.078423, 'Junction3', 'Signal3', 'District3', 'No', 60, 70),
    (28.8267067, 77.068413, 'Junction4', 'Signal4', 'District4', 'Yes', 15, 40),
    (28.8166967, 77.058403, 'Junction5', 'Signal5', 'District5', 'No', 50, 30),
    (28.808122, 77.049466, 'Junction6', 'Signal6', 'District6', 'Yes', 25, 55)
]

# Convert path points to coordinates
coords_path = [(lat, lon) for lon, lat in zip(path_points['Longitude'], path_points['Latitude'])]

# Generate route that follows the road
def get_route(client, start, end):
    route = client.directions(coordinates=[(start[1], start[0]), (end[1], end[0])], profile='driving-car', format='geojson')
    return [(coord[1], coord[0]) for coord in route['features'][0]['geometry']['coordinates']]

# Combine all segments
full_route = []
for i in range(len(coords_path) - 1):
    segment = get_route(client, coords_path[i], coords_path[i+1])
    full_route.extend(segment if i == 0 else segment[1:])  # avoid duplicate points

# Initial map setup
car_map = folium.Map(location=[coords_path[0][0], coords_path[0][1]], zoom_start=14)

# Add start and end markers
folium.Marker(
    location=[coords_path[0][0], coords_path[0][1]],
    popup='Start',
    icon=folium.Icon(color='green')
).add_to(car_map)

folium.Marker(
    location=[coords_path[-1][0], coords_path[-1][1]],
    popup='End',
    icon=folium.Icon(color='red')
).add_to(car_map)

# Add additional markers from points data
for lat, lon, junction, signal, district, green_light, changing_time, speed_limit in points:
    folium.Marker(
        location=[lat, lon],
        popup=(
            f'Junction: {junction}<br>'
            f'Signal: {signal}<br>'
            f'District: {district}<br>'
            f'Green Light: {green_light}<br>'
            f'Changing Time: {changing_time} s<br>'
            f'Speed Limit: {speed_limit} km/h'
        ),
        icon=folium.Icon(color='green')
    ).add_to(car_map)

# green markers for all points in coords_path
for lat, lon in coords_path:
    folium.Marker(
        location=[lat, lon],
        icon=folium.Icon(color='green')
    ).add_to(car_map)

# Save the initial map
car_map.save('car_movement_directions_map.html')
display(car_map)

# Animate car movement through full_route
for i in range(len(full_route)):
    current_coords = full_route[i]
    clear_output(wait=True)
    car_map = folium.Map(location=current_coords, zoom_start=14)

    # Add start and end markers
    folium.Marker(
        location=[coords_path[0][0], coords_path[0][1]],
        popup='Start',
        icon=folium.Icon(color='green')
    ).add_to(car_map)

    folium.Marker(
        location=[coords_path[-1][0], coords_path[-1][1]],
        popup='End',
        icon=folium.Icon(color='red')
    ).add_to(car_map)

    # Draw the route path
    folium.PolyLine(locations=full_route[:i+1], color='blue').add_to(car_map)

    # Simulate a random speed limit for the current position
    speed_limit = random.uniform(35, 37)
    print(f'Current speed limit: {speed_limit:.2f} km/h')

    # Add a marker for the current position with speed limit
    folium.Marker(
        location=current_coords,
        popup=f'Speed Limit: {speed_limit:.2f} km/h',
        icon=folium.Icon(color='red')
    ).add_to(car_map)

    # Add permanent green markers for all points in coords_path
    for lat, lon in coords_path:
        folium.Marker(
            location=[lat, lon],
            icon=folium.Icon(color='green')
        ).add_to(car_map)

    # Add additional markers from points data
    for lat, lon, junction, signal, district, green_light, changing_time, speed_limit in points:
        folium.Marker(
            location=[lat, lon],
            popup=(
                f'Junction: {junction}<br>'
                f'Signal: {signal}<br>'
                f'District: {district}<br>'
                f'Green Light: {green_light}<br>'
                f'Changing Time: {changing_time} s<br>'
                f'Speed Limit: {speed_limit} km/h'
            ),
            icon=folium.Icon(color='green')
        ).add_to(car_map)

    # Display the updated map
    display(car_map)

    # Pause briefly to create an animation effect
    time.sleep(0.001)

# Your OpenRouteService API key
api_key = '5b3ce3597851110001cf62487dab724e881e4bfeab36d60cd37e61f6'
client = openrouteservice.Client(key=api_key)

# Sample path points data
path_points = {
    'Longitude': [77.0984433, 77.088433, 77.078423, 77.068413, 77.049466],
    'Latitude': [28.8567367, 28.8467267, 28.8367167, 28.8267067, 28.808122]
}

# Sample points data for additional markers
points = [
    (28.8567367, 77.0984433, 'Junction1', 'Signal1', 'District1', 'Yes', 30, 50),
    (28.8467267, 77.088433, 'Junction2', 'Signal2', 'District2', 'Yes', 45, 60),
    (28.8367167, 77.078423, 'Junction3', 'Signal3', 'District3', 'No', 60, 70),
    (28.8267067, 77.068413, 'Junction4', 'Signal4', 'District4', 'Yes', 15, 40),
    (28.808122, 77.049466, 'Junction6', 'Signal6', 'District6', 'Yes', 25, 55)
]

# Convert path points to coordinates
coords_path = [(lat, lon) for lon, lat in zip(path_points['Longitude'], path_points['Latitude'])]

# Generate route that follows the road
def get_route(client, start, end):
    route = client.directions(coordinates=[(start[1], start[0]), (end[1], end[0])], profile='driving-car', format='geojson')
    return [(coord[1], coord[0]) for coord in route['features'][0]['geometry']['coordinates']]

# Combine all segments
full_route = []
for i in range(len(coords_path) - 1):
    segment = get_route(client, coords_path[i], coords_path[i+1])
    full_route.extend(segment if i == 0 else segment[1:])  # avoid duplicate points

# Initial map setup
car_map = folium.Map(location=[coords_path[0][0], coords_path[0][1]], zoom_start=14)

# Add start and end markers
folium.Marker(
    location=[coords_path[0][0], coords_path[0][1]],
    popup='Start',
    icon=folium.Icon(color='green')
).add_to(car_map)

folium.Marker(
    location=[coords_path[-1][0], coords_path[-1][1]],
    popup='End',
    icon=folium.Icon(color='red')
).add_to(car_map)

# Add additional markers from points data
for lat, lon, junction, signal, district, green_light, changing_time, speed_limit in points:
    folium.Marker(
        location=[lat, lon],
        popup=(
            f'Junction: {junction}<br>'
            f'Signal: {signal}<br>'
            f'District: {district}<br>'
            f'Green Light: {green_light}<br>'
            f'Changing Time: {changing_time} s<br>'
            f'Speed Limit: {speed_limit} km/h'
        ),
        icon=folium.Icon(color='green')
    ).add_to(car_map)

# Add green markers for all points in coords_path
for lat, lon in coords_path:
    folium.Marker(
        location=[lat, lon],
        icon=folium.Icon(color='green')
    ).add_to(car_map)

# Save the initial map
car_map.save('car_movement_directions_map.html')
display(car_map)

# Animate car movement through full_route
for i in range(len(full_route)):
    current_coords = full_route[i]
    clear_output(wait=True)
    car_map = folium.Map(location=current_coords, zoom_start=14)

    # Add start and end markers
    folium.Marker(
        location=[coords_path[0][0], coords_path[0][1]],
        popup='Start',
        icon=folium.Icon(color='green')
    ).add_to(car_map)

    folium.Marker(
        location=[coords_path[-1][0], coords_path[-1][1]],
        popup='End',
        icon=folium.Icon(color='red')
    ).add_to(car_map)

    # Draw the route path
    folium.PolyLine(locations=full_route[:i+1], color='blue').add_to(car_map)

    # Simulate a random speed limit for the current position
    speed_limit = random.uniform(35, 37)
    print(f'Current speed limit: {speed_limit:.2f} km/h')

    # Add a marker for the current position with speed limit
    folium.Marker(
        location=current_coords,
        popup=f'Speed Limit: {speed_limit:.2f} km/h',
        icon=folium.Icon(color='red')
    ).add_to(car_map)

    # Add permanent green markers for all points in coords_path
    for lat, lon in coords_path:
        folium.Marker(
            location=[lat, lon],
            icon=folium.Icon(color='green')
        ).add_to(car_map)

    # Add additional markers from points data
    for lat, lon, junction, signal, district, green_light, changing_time, speed_limit in points:
        folium.Marker(
            location=[lat, lon],
            popup=(
                f'Junction: {junction}<br>'
                f'Signal: {signal}<br>'
                f'District: {district}<br>'
                f'Green Light: {green_light}<br>'
                f'Changing Time: {changing_time} s<br>'
                f'Speed Limit: {speed_limit} km/h'
            ),
            icon=folium.Icon(color='green')
        ).add_to(car_map)

    # Display the updated map
    display(car_map)

    # Pause briefly to create an animation effect
    time.sleep(0.01)








