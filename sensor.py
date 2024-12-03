import json
import random
import time
from azure.iot.device import IoTHubDeviceClient

# Replace with your IoT Device Connection String
CONNECTION_STRING = "connection string"

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

def send_data(client, location):
    """Send data to IoT Hub."""
    while True:
        data = generate_sensor_data(location)
        client.send_message(json.dumps(data))
        print(f"Sent data: {data}")
        time.sleep(20)  # Send data every 10 seconds

if __name__ == "__main__":
    # Initialize IoT Hub Device Client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    location = "Dow's Lake"  # Change for each device
    send_data(client, location)
