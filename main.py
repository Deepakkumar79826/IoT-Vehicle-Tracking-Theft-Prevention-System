import time

from datetime import datetime

from python_simulation.gps_simulator import GPSSimulator
from python_simulation.geofence import inside_geofence
from python_simulation.theft_detector import detect_theft
from python_simulation.alerts import generate_alert
from python_simulation.logger import save_log

gps = GPSSimulator()

print("Vehicle Tracking System Started")

mode = input(
    "\n1 Normal\n2 Geofence Breach\n3 Theft\nChoose: "
)

while True:

    if mode == "1":
        lat, lon = gps.normal_movement()

    elif mode == "2":
        lat, lon = gps.geofence_breach()

    else:
        lat, lon = gps.theft_movement()

    status = "SAFE"
    alert = "NONE"

    if not inside_geofence(lat, lon):
        status = "GEOFENCE BREACH"
        alert = "Vehicle Left Safe Zone"
        generate_alert(alert)

    if detect_theft(lat, lon):
        status = "THEFT DETECTED"
        alert = "Vehicle Theft Suspected"
        generate_alert(alert)

    maps_link = (
        f"https://maps.google.com/?q={lat},{lon}"
    )

    row = {
        "timestamp": datetime.now(),
        "latitude": lat,
        "longitude": lon,
        "status": status,
        "alert": alert,
        "maps": maps_link
    }

    save_log(row)

    print("\n====================")
    print(f"Latitude : {lat}")
    print(f"Longitude: {lon}")
    print(f"Status   : {status}")
    print(f"Alert    : {alert}")
    print(maps_link)

    time.sleep(5)