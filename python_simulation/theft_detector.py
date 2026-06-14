from geopy.distance import geodesic
from docs.config import *

def detect_theft(lat, lon):

    distance = geodesic(
        (SAFE_LATITUDE, SAFE_LONGITUDE),
        (lat, lon)
    ).km

    if distance > THEFT_DISTANCE_KM:
        return True

    return False