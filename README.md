# Assignment-2
# Real-Time Monitoring System for Rideau Canal Skateway

## Introduction

The Rideau Canal Skateway in Ottawa, a cherished attraction, requires constant monitoring to ensure the safety of skaters. This project presents a **Real-Time Monitoring System** that uses simulated IoT sensors, processes the collected data in real-time, and stores it for analysis. By analyzing metrics like ice thickness and weather conditions, the system helps detect unsafe conditions, enhancing visitor safety.

---

## Table of Contents

- [System Overview](#system-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [System Architecture](#system-architecture)
- [Step-by-Step Implementation](#step-by-step-implementation)
  - [Simulating IoT Sensors](#1-simulating-iot-sensors)
  - [Setting up Azure IoT Hub](#2-setting-up-azure-iot-hub)
  - [Configuring Azure Stream Analytics](#3-configuring-azure-stream-analytics)
  - [Azure Blob Storage Setup](#4-azure-blob-storage-setup)
- [Example Outputs](#example-outputs)
- [Results](#results)

## System Overview
![Untitled diagram-2024-11-30-082444](https://github.com/user-attachments/assets/c16b0d3b-ae44-468c-aa9b-f3177650d186)


The monitoring system simulates sensors installed at three locations along the Rideau Canal Skateway:
1. Dow's Lake
2. Fifth Avenue
3. National Arts Centre (NAC)

Key components:
- **Simulated Sensors** generate ice and weather data every 10 seconds.
- **Azure IoT Hub** collects and routes sensor data.
- **Azure Stream Analytics** processes the data for actionable insights.
- **Azure Blob Storage** organizes and stores processed data.

---

## Features

- Real-time monitoring of ice thickness, snow accumulation, and temperatures.
- Simulates three distinct locations with unique data streams.
- Automated processing and storage of sensor data for analysis.
- Organized data storage in Azure Blob Storage.

---

## Technologies Used

- **Python**: Sensor simulation script.
- **Azure IoT Hub**: For collecting and routing sensor data.
- **Azure Stream Analytics**: Real-time data processing.
- **Azure Blob Storage**: Storage for processed data.
## Installation

### Prerequisites

- [Azure Account](https://azure.microsoft.com/)
- Python 3.x installed on your local machine.
- Required Python libraries:
  ```bash
  pip install azure-iot-device

## Usage

### Simulating Sensors

1. Add your **Primary Connection String** from Azure IoT Hub to the Python script.
2. Run the simulation script:
   ```bash
   python IoTSensorSimulation.py


---

## System Architecture

The system operates in four key stages:

1. **Data Generation**: Sensors generate JSON data every 10 seconds.
2. **Data Collection**: Data is sent to Azure IoT Hub.
3. **Real-Time Processing**: Azure Stream Analytics calculates metrics like average ice thickness and maximum snow accumulation.
4. **Data Storage**: Processed data is saved in JSON format in Azure Blob Storage.

---
## Step-by-Step Implementation

### 1. Simulating IoT Sensors

Sensors generate data in the following format:

```json
{
import json
import random
import time
from azure.iot.device import IoTHubDeviceClient

# Replace with your IoT Device Connection String
CONNECTION_STRING = "Connection String"

def generate_sensor_data(location):
    """Generate random sensor data."""
    return {
        "location": location,
        "iceThickness": random.randint(15, 30),  # cm
        "surfaceTemperature": random.uniform(-5, 5),  # °C
        "snowAccumulation": random.randint(0, 20),  # cm
        "externalTemperature": random.uniform(-10, 5),  # °C
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }

{
def send_data(client, location):
    """Send data to IoT Hub."""
    while True:
        data = generate_sensor_data(location)
        client.send_message(json.dumps(data))
        print(f"Sent data: {data}")
        time.sleep(20)  # Send data every 20 seconds

if __name__ == "__main__":
    # Initialize IoT Hub Device Client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    location = "Fifth Ave"  # Change for each device
    send_data(client, location)
}
```
#### How to Run

1. Install the required Python library:
   ```bash
   pip install azure-iot-device
``
2. Add the **Primary Connection String** from the IoT Hub to the script.
3. Run the script:
   ```bash
   python IoTSensorSimulation.py
```
### 2. Setting up Azure IoT Hub

1. Create an **IoT Hub** in the Azure portal.
2. Add devices for each location:
   - Dow's Lake
   - Fifth Avenue
   - NAC
3. Copy the **Primary Connection String** for each device.
4. Enable message routing to **Azure Stream Analytics**.

```yaml
# Example YAML configuration for IoT Hub routing
IoTHub:
  devices:
    - name: "Dow's Lake"
      connectionString: "PrimaryConnectionStringForDowLake"
    - name: "Fifth Avenue"
      connectionString: "PrimaryConnectionStringForFifthAve"
    - name: "NAC"
      connectionString: "PrimaryConnectionStringForNAC"
  messageRouting: "Enabled"
```
### 3. Configuring Azure Stream Analytics

1. Create a **Stream Analytics Job** in the Azure portal.
2. Add:
   - **Input**: Azure IoT Hub.
   - **Output**: Azure Blob Storage.
3. Use the following SQL query to process the data:
   ```sql
   SELECT  
       System.Timestamp AS windowEndTime,  
       location,  
       AVG(iceThickness) AS avgIceThickness,  
       MAX(snowAccumulation) AS maxSnowAccumulation  
   FROM  
       IoTHubInput  
   GROUP BY  
       TumblingWindow(minute, 5), location
``
### 4. Azure Blob Storage Setup

1. Create a **Blob Storage** container.
2. Organize files by date and time:

#### Example Processed Data File

```json
{  
  "windowEndTime": "2024-11-23T12:05:00Z",  
  "location": "Dow's Lake",  
  "avgIceThickness": 26.5,  
  "maxSnowAccumulation": 9  
}
```
---

## Example Outputs

### Raw Sensor Data

```json
{  
  "location": "Fifth Avenue",  
  "iceThickness": 28,  
  "surfaceTemperature": -2,  
  "snowAccumulation": 5,  
  "externalTemperature": -6,  
  "timestamp": "2024-11-23T12:00:00Z"  
}
```
### Processed Data (Stored in Blob Storage)
```json
{  
  "windowEndTime": "2024-11-23T12:05:00Z",  
  "location": "Dow's Lake",  
  "avgIceThickness": 26.5,  
  "maxSnowAccumulation": 9  
}
```
## Results
Real-time processing calculates average ice thickness and maximum snow accumulation every 5 minutes for each location. Processed data is stored in Azure Blob Storage in an organized structure, allowing easy retrieval and analysis.
---.


