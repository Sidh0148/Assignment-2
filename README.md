# Assignment-2
# Rideau Canal Skateway Monitoring

## Scenario Description

The Rideau Canal Skateway, a historic and world-renowned attraction in Ottawa, needs constant monitoring to ensure skater safety. Your team has been hired by the National Capital Commission (NCC) to build a real-time data streaming system that will:

- Simulate IoT sensors to monitor ice conditions and weather factors along the canal.
- Process incoming sensor data to detect unsafe conditions in real time.
- Store the results in Azure Blob Storage for further analysis.

### Problem Addressed:
This solution helps monitor the conditions of the ice and weather to ensure the safety of people skating on the Rideau Canal. The system simulates IoT sensors to provide real-time data, process it, and store the data for further review.

## System Architecture

Below is a high-level overview of the system architecture:

1. **IoT Sensors** push simulated data to **Azure IoT Hub**.
2. **Azure Stream Analytics** processes incoming data in real-time.
3. The processed data is stored in **Azure Blob Storage** for further analysis.

![Architecture Diagram](architecture-diagram.png)

## Implementation Details

### IoT Sensor Simulation

The simulated IoT sensors generate data every 10 seconds at three locations on the Rideau Canal: Dow's Lake, Fifth Avenue, and NAC. The data includes:

- Ice Thickness (in cm)
- Surface Temperature (in °C)
- Snow Accumulation (in cm)
- External Temperature (in °C)

#### Example JSON Payload:
```json
{
  "location": "Dow's Lake",
  "iceThickness": 27,
  "surfaceTemperature": -1,
  "snowAccumulation": 8,
  "externalTemperature": -4,
  "timestamp": "2024-11-23T12:00:00Z"
}
### Azure IoT Hub Configuration

1. **Create an IoT Hub** in the Azure portal.
2. **Add devices to the IoT Hub** to simulate sensor data from Dow's Lake, Fifth Avenue, and NAC.
3. **Use the connection string provided** for each device to push simulated data to the IoT Hub.

### Azure Stream Analytics Job

The Stream Analytics job is configured as follows:

1. **Input Source**: Data from IoT Hub.
2. **Query Logic**: Aggregates the data over a 5-minute window, calculating average ice thickness and maximum snow accumulation.
3. **Output Destination**: The processed data is sent to Azure Blob Storage.

#### Sample SQL Query:
```sql
SELECT
    location,
    AVG(iceThickness) AS avgIceThickness,
    MAX(snowAccumulation) AS maxSnowAccumulation
INTO
    [BlobOutput]
FROM
    [IoTHubInput]
GROUP BY
    location, TumblingWindow(minute, 5)

