from math import radians, sin, cos, acos

def find_spots_in_radius(spots, **kwargs):
    latitude = kwargs['latitude']
    longitude = kwargs['longitude']
    radius = kwargs['radius']
    earth_radius = 6371.01

    spots_in_radius = []

    for spot in spots:
        s_lat = radians(spot['latitude'])
        s_lon = radians(spot['longitude'])

        distance = earth_radius * acos(sin(latitude)*sin(s_lat) + cos(latitude)*cos(s_lat)*cos(longitude - s_lon))
        print("Distance is {distance}")

        if distance <= radius:
            spots_in_radius.append(spot)
        
    return spots_in_radius
