import random

class GPSSimulator:

    def __init__(self):
        self.base_lat = 28.6139
        self.base_lon = 77.2090

    def normal_movement(self):

        lat = self.base_lat + random.uniform(-0.002, 0.002)
        lon = self.base_lon + random.uniform(-0.002, 0.002)

        return lat, lon

    def geofence_breach(self):

        lat = self.base_lat + random.uniform(0.01, 0.02)
        lon = self.base_lon + random.uniform(0.01, 0.02)

        return lat, lon

    def theft_movement(self):

        lat = self.base_lat + random.uniform(0.03, 0.05)
        lon = self.base_lon + random.uniform(0.03, 0.05)

        return lat, lon