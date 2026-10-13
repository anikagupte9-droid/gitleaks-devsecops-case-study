from flask import Flask, jsonify, request
import os

app = Flask(__name__)

API_KEY = os.getenv("TELEMETRY_API_KEY", "server-test-key")


@app.route("/api/telemetry", methods=["GET"])
def telemetry():
    auth_header = request.headers.get("Authorization")

    if auth_header != f"Bearer {API_KEY}":
        return jsonify({"error": "Unauthorized"}), 401

    data = {
        "vehicle": "Athena",
        "speed_kmh": 72.4,
        "battery_voltage": 312.6,
        "battery_current": 48.2,
        "motor_torque_nm": 86.5,
        "motor_temperature_c": 54.1
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(port=5000, debug=True)