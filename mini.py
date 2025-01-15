from flask import Flask, jsonify
from flask_cors import CORS
import serial
import threading

app = Flask(__name__)
CORS(app)  # Allow React app to access the backend

# Replace 'COM3' with your Arduino's port
arduino = serial.Serial('COM3', 9600, timeout=1)

sensor_data = {"value": 0}

def read_sensor_data():
    global sensor_data
    while True:
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').strip()
            if line.isdigit():
                sensor_data["value"] = int(line)

@app.route('/sensor', methods=['GET'])
def get_sensor_data():
    return jsonify(sensor_data)

if __name__ == "__main__":
    # Start the Serial reading thread
    threading.Thread(target=read_sensor_data, daemon=True).start()
    app.run(debug=True)
