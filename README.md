Real-Time Monitoring System for Rideau Canal Skateway
Introduction
The Rideau Canal Skateway in Ottawa, a cherished attraction, requires constant monitoring to ensure the safety of skaters. This project presents a Real-Time Monitoring System that uses simulated IoT sensors, processes the collected data in real-time, and stores it for analysis. By analyzing metrics like ice thickness and weather conditions, the system helps detect unsafe conditions, enhancing visitor safety.

Table of Contents
System Overview
Features
Technologies Used
Installation
Usage
System Architecture
Step-by-Step Implementation
Simulating IoT Sensors
Setting up Azure IoT Hub
Configuring Azure Stream Analytics
Azure Blob Storage Setup
Example Outputs
Results
Contributors
License
System Overview
The monitoring system simulates sensors installed at three locations along the Rideau Canal Skateway:

Dow's Lake
Fifth Avenue
National Arts Centre (NAC)
Key components:

Simulated Sensors generate ice and weather data every 10 seconds.
Azure IoT Hub collects and routes sensor data.
Azure Stream Analytics processes the data for actionable insights.
Azure Blob Storage organizes and stores processed data.
Features
Real-time monitoring of ice thickness, snow accumulation, and temperatures.
Simulates three distinct locations with unique data streams.
Automated processing and storage of sensor data for analysis.
Organized data storage in Azure Blob Storage.
Technologies Used
Python: Sensor simulation script.
Azure IoT Hub: For collecting and routing sensor data.
Azure Stream Analytics: Real-time data processing.
Azure Blob Storage: Storage for processed data.
Installation
Prerequisites
Azure Account
Python 3.x installed on your local machine.
Required Python libraries:
bash
Copy code
pip install azure-iot-device
Usage
Simulating Sensors
Add your Primary Connection String from Azure IoT Hub to the Python script.
Run the simulation script:
bash
Copy code
python IoTSensorSimulation.py
Accessing Processed Data
Navigate to the Azure portal.
Open the Blob Storage container created for this project.
Browse files organized by date and time.
System Architecture
The system operates in four key stages:

Data Generation: Sensors generate JSON data every 10 seconds.
Data Collection: Data is sent to Azure IoT Hub.
Real-Time Processing: Azure Stream Analytics calculates metrics like average ice thickness and maximum snow accumulation.
Data Storage: Processed data is saved in JSON format in Azure Blob Storage.
Step-by-Step Implementation
1. Simulating IoT Sensors
Sensors generate data in the following format:

json
Copy code
{  
  "location": "Dow's Lake",  
  "iceThickness": 27,  
  "surfaceTemperature": -1,  
  "snowAccumulation": 8,  
  "externalTemperature": -4,  
  "timestamp": "2024-11-23T12:00:00Z"  
}
How to Run
Install the required Python library:
bash
Copy code
pip install azure-iot-device
Add the Primary Connection String from the IoT Hub to the script.
Run the script:
bash
Copy code
python IoTSensorSimulation.py
2. Setting up Azure IoT Hub
Create an IoT Hub in the Azure portal.
Add devices for each location:
Dow's Lake
Fifth Avenue
NAC
Copy the Primary Connection String for each device.
Enable message routing to Azure Stream Analytics.
3. Configuring Azure Stream Analytics
Create a Stream Analytics Job in the Azure portal.
Add:
Input: Azure IoT Hub.
Output: Azure Blob Storage.
Use the following SQL query to process the data:
sql
Copy code
SELECT  
    System.Timestamp AS windowEndTime,  
    location,  
    AVG(iceThickness) AS avgIceThickness,  
    MAX(snowAccumulation) AS maxSnowAccumulation  
FROM  
    IoTHubInput  
GROUP BY  
    TumblingWindow(minute, 5), location
Save the configuration and start the job.
4. Azure Blob Storage Setup
Create a Blob Storage container.
Organize files by date and time:
sql
Copy code
blob-storage-container/  
  ├── date=2024-11-23/  
      ├── hour=12/  
          └── results_2024-11-23T12:05:00Z.json  
Example Processed Data File
json
Copy code
{  
  "windowEndTime": "2024-11-23T12:05:00Z",  
  "location": "Dow's Lake",  
  "avgIceThickness": 26.5,  
  "maxSnowAccumulation": 9  
}
Example Outputs
Raw Sensor Data
json
Copy code
{  
  "location": "Fifth Avenue",  
  "iceThickness": 28,  
  "surfaceTemperature": -2,  
  "snowAccumulation": 5,  
  "externalTemperature": -6,  
  "timestamp": "2024-11-23T12:00:00Z"  
}
Processed Data (Stored in Blob Storage)
json
Copy code
{  
  "windowEndTime": "2024-11-23T12:05:00Z",  
  "location": "Dow's Lake",  
  "avgIceThickness": 26.5,  
  "maxSnowAccumulation": 9  
}
Results
Real-time processing calculates average ice thickness and maximum snow accumulation every 5 minutes for each location.
Processed data is stored in Azure Blob Storage in an organized structure, allowing easy retrieval and analysis.


