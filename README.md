# Assignment-2

Here’s a structured and professional README.md file for your project:

Real-Time Monitoring System for Rideau Canal Skateway
Scenario Description
The Rideau Canal Skateway, a historic attraction in Ottawa, requires constant monitoring to ensure the safety of skaters. Adverse weather conditions and fluctuating ice quality pose significant risks. The National Capital Commission (NCC) has tasked our team with designing a real-time monitoring system that:

Simulates IoT sensors to track ice conditions and weather factors.
Processes sensor data in real time to detect unsafe conditions.
Stores aggregated data in Azure Blob Storage for analysis.
This system enables proactive safety measures and historical trend analysis, ensuring a safe and enjoyable skating experience.

System Architecture
Below is the data flow for the system:

IoT Sensors: Simulate ice and weather metrics at three key locations along the canal:

Dow's Lake
Fifth Avenue
NAC
Azure IoT Hub: Collects real-time telemetry data from simulated IoT sensors.

Azure Stream Analytics: Processes data to calculate aggregated metrics (e.g., average ice thickness) and detect unsafe conditions.

Azure Blob Storage: Stores processed data for further analysis.


Implementation Details
1. IoT Sensor Simulation
Data Generation
Simulated IoT sensors generate telemetry data every 10 seconds. The generated data includes:

Ice Thickness (cm)
Surface Temperature (°C)
Snow Accumulation (cm)
External Temperature (°C)
Timestamp
Example JSON Payload
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
Script
We developed a Python script to simulate sensor data and push it to Azure IoT Hub. The script uses the Azure IoT SDK.

2. Azure IoT Hub Configuration
To set up the IoT Hub:

Create an IoT Hub in the Azure portal.
Add IoT Devices for each simulated sensor.
Retrieve the Primary Connection String for device authentication.
Configure message routing to enable integration with Azure Stream Analytics.
3. Azure Stream Analytics Job
Job Configuration
Input Source: Azure IoT Hub.
Query Logic: Aggregates telemetry data over a 5-minute tumbling window to calculate:
Average ice thickness.
Maximum snow accumulation.
Sample SQL Query
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
Output Destination: Azure Blob Storage.
4. Azure Blob Storage
Processed data is stored in JSON format with the following structure:

json
Copy code
{  
  "windowEndTime": "2024-11-23T12:05:00Z",  
  "location": "Dow's Lake",  
  "avgIceThickness": 26.5,  
  "maxSnowAccumulation": 9  
}  
Folder Structure
Data is organized by date and time for easy retrieval:

sql
Copy code
blob-storage-container/  
  ├── date=2024-11-23/  
      ├── hour=12/  
          └── results_2024-11-23T12:05:00Z.json  
Usage Instructions
1. Running the IoT Sensor Simulation
Clone the repository.
Install dependencies:
bash
Copy code
pip install azure-iot-device  
Run the script:
bash
Copy code
python IoTSensorSimulation.py  
2. Configuring Azure Services
Set up Azure IoT Hub and register devices.
Create and configure Azure Stream Analytics job using the provided SQL query.
Create an Azure Blob Storage container for output storage.
3. Accessing Stored Data
Navigate to the Blob Storage container in the Azure portal.
Locate files based on date and time.
Download and view JSON files for analysis.
Results
Key Findings
Aggregated metrics, such as average ice thickness and maximum snow accumulation, are calculated and stored every 5 minutes.
Sample output files can be found in the Blob Storage container under the corresponding date and time folders.
Reflection
Challenges Faced
Simulating realistic data patterns: Addressed by implementing randomized but controlled ranges for sensor values.
Setting up secure IoT Hub communication: Overcame by using device authentication with connection strings.
Query optimization in Stream Analytics: Resolved by testing various windowing functions.
