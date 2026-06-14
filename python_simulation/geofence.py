from geopy.distance import geodesic
from docs.config import *

def inside_geofence(lat, lon):

    distance = geodesic(
        (SAFE_LATITUDE, SAFE_LONGITUDE),
        (lat, lon)
    ).km

    return distance <= GEOFENCE_RADIUS_KM