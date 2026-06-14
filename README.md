# 🚗 IoT Vehicle Tracking & Theft Prevention System

## 📌 Overview

The **IoT Vehicle Tracking & Theft Prevention System** is an industry-oriented smart transportation project that provides real-time vehicle tracking, geofencing, theft detection, location history logging, automated alert generation, and dashboard visualization.

This project simulates a GPS-enabled vehicle monitoring system using Python and demonstrates how modern fleet management and vehicle security solutions operate in the real world.

It is designed for students, IoT enthusiasts, and developers looking to build practical smart mobility applications and strengthen their GitHub portfolios.

---

# 🎯 Problem Statement

Vehicle theft and lack of real-time monitoring are major concerns for vehicle owners, fleet operators, logistics companies, and transportation services.

Traditional tracking solutions are often expensive and require specialized hardware.

This project provides a cost-effective and scalable solution capable of:

* Monitoring vehicle location
* Detecting unauthorized movement
* Triggering theft alerts
* Maintaining location history
* Visualizing vehicle movement on a dashboard

---

# 🚀 Features

✅ Real-Time GPS Tracking Simulation

✅ Vehicle Location Monitoring

✅ Geofence Detection

✅ Theft Detection Engine

✅ Alert Generation System

✅ Google Maps Integration

✅ Location History Logging

✅ CSV Data Storage

✅ PDF Report Generation

✅ Interactive Streamlit Dashboard

✅ Industry-Oriented Project Structure

✅ Beginner-Friendly Implementation

---

# 🏗️ System Architecture

```text
GPS Coordinates
       │
       ▼
GPS Simulator
       │
       ▼
Tracking Engine
       │
       ├────────► Geofence Detection
       │
       ├────────► Theft Detection
       │
       ▼
Alert System
       │
       ▼
Data Logger
       │
       ▼
CSV Storage
       │
       ▼
Dashboard Visualization
       │
       ▼
PDF Reports
```

---

# 📂 Project Structure

```text
IoT-Vehicle-Tracking-Theft-Prevention-System/
│
├── main.py
├── requirements.txt
│
├── python_simulation/
│   ├── gps_simulator.py
│   ├── geofence.py
│   ├── theft_detector.py
│   ├── alerts.py
│   └── logger.py
│
├── dashboard/
│   └── app.py
│
├── reports/
│   └── report_generator.py
│
├── data/
│   ├── vehicle_logs.csv
│   └── alerts.csv
│
├── outputs/
│   └── vehicle_report.pdf
│
└── docs/
    └── config.py
```

---

# ⚙️ Technologies Used

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Core Development     |
| Pandas     | Data Processing      |
| Geopy      | Distance Calculation |
| Streamlit  | Dashboard            |
| Plotly     | Data Visualization   |
| ReportLab  | PDF Reports          |
| CSV        | Data Storage         |

---

# 🔧 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/IoT-Vehicle-Tracking-Theft-Prevention-System.git

cd IoT-Vehicle-Tracking-Theft-Prevention-System
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Start Vehicle Tracking Simulation

```bash
python main.py
```

Select Mode:

```text
1 - Normal Movement
2 - Geofence Breach
3 - Theft Simulation
```

---

## Launch Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard Features:

* Vehicle Location Map
* Tracking History
* Status Analytics
* Alert Monitoring
* Route Visualization

---

# 📍 Google Maps Integration

Each GPS record automatically generates a Google Maps link:

```text
https://maps.google.com/?q=LATITUDE,LONGITUDE
```

Example:

```text
https://maps.google.com/?q=28.6139,77.2090
```

---

# 🚨 Theft Detection Logic

The system continuously checks the distance between the vehicle and the authorized parking location.

### Conditions

#### SAFE

Vehicle remains inside the geofence.

#### GEOFENCE BREACH

Vehicle exits the authorized zone.

#### THEFT DETECTED

Vehicle travels significantly outside the predefined safety boundary.

---

# 📊 Dashboard Preview

The dashboard displays:

* Live Location Data
* Vehicle Route
* GPS Coordinates
* Status Distribution
* Theft Alerts
* Geofence Alerts

---

# 📁 Reports

The system automatically stores:

### Vehicle Logs

```text
Timestamp
Latitude
Longitude
Status
Alert
Maps Link
```

Stored In:

```text
data/vehicle_logs.csv
```

### Alert Logs

Stored In:

```text
data/alerts.csv
```

### PDF Reports

Generated Using:

```bash
python reports/report_generator.py
```

Output:

```text
outputs/vehicle_report.pdf
```

---

# 🧪 Simulation Scenarios

### Normal Movement

Vehicle moves within safe boundaries.

### Geofence Breach

Vehicle leaves authorized area.

### Theft Scenario

Vehicle moves far beyond permitted range.

### Generated Outputs

```text
SAFE

GEOFENCE BREACH

THEFT DETECTED
```

---

# 🌍 Real-World Applications

### Fleet Management

* Truck Tracking
* Driver Monitoring
* Route Optimization

### Ride Sharing

* Vehicle Tracking
* Driver Safety

### School Transportation

* School Bus Monitoring
* Parent Notifications

### Personal Vehicles

* Theft Prevention
* Parking Monitoring

### Logistics Industry

* Asset Tracking
* Cargo Security

---

# 🔮 Future Enhancements

* MQTT Integration
* ESP32 Hardware Support
* Real GPS Module Integration
* Node-RED Dashboard
* Mobile Application
* SMS Notifications
* Email Alerts
* AI-Based Theft Prediction
* Driver Behavior Analysis
* Cloud Database Storage

---

# 💼 Skills Demonstrated

* IoT System Design
* Python Programming
* GPS Tracking
* Geofencing
* Theft Detection Algorithms
* Dashboard Development
* Data Logging
* Report Generation
* Smart Transportation Systems
* Real-Time Monitoring

---

# 🎓 Interview Question

### Explain Your Project

This project is a Python-based IoT Vehicle Tracking and Theft Prevention System that simulates GPS-enabled vehicle monitoring. It tracks vehicle movement, detects geofence violations, generates theft alerts, logs location history, creates PDF reports, and visualizes vehicle data using an interactive Streamlit dashboard. The project demonstrates real-world IoT concepts used in fleet management, smart transportation, and vehicle security systems.

---

# 📌 Repository Topics

```text
iot
python
gps-tracking
vehicle-tracking
theft-detection
geofencing
streamlit
fleet-management
smart-transportation
real-time-monitoring
```

---

# ⭐ If you found this project useful, consider giving it a star!

Made with ❤️ using Python and IoT Concepts.
