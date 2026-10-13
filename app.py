import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEMETRY_API_KEY = os.getenv("TELEMETRY_API_KEY")
TELEMETRY_API_URL = "http://127.0.0.1:5000/api/telemetry"

headers = {
    "Authorization": f"Bearer {TELEMETRY_API_KEY}"
}

response = requests.get(
    TELEMETRY_API_URL,
    headers=headers
)

if response.status_code == 200:
    telemetry = response.json()

    print("\nVehicle Telemetry")
    print("-----------------")
    print(f"Vehicle: {telemetry['vehicle']}")
    print(f"Speed: {telemetry['speed_kmh']} km/h")
    print(f"Battery Voltage: {telemetry['battery_voltage']} V")
    print(f"Battery Current: {telemetry['battery_current']} A")
    print(f"Motor Torque: {telemetry['motor_torque_nm']} Nm")
    print(f"Motor Temperature: {telemetry['motor_temperature_c']} °C")
else:
    print("Telemetry request failed:", response.status_code)