import serial
import time
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Flask app setup
app = Flask(__name__)
socketio = SocketIO(app)

# Replace 'COM3' with your Arduino port
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Wait for Arduino to initialize

# Serve the HTML file
@app.route('/')
def index():
    return render_template('index.html')

# WebSocket event to send data
@socketio.on('request_data')
def handle_request():
    try:
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').strip()  # Read data from Arduino
            emit('pulse_data', {'bpm': line})  # Send to client
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    socketio.run(app, debug=True)
