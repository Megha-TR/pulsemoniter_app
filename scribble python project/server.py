from flask import Flask, jsonify, render_template
import serial

app = Flask(__name__)

# Initialize the serial connection to Arduino
# Update 'COM3' to the correct port for your Arduino
arduino = serial.Serial("COM4",9600, timeout=1)
@app.route('/')
def index():
    return render_template('index.html')  # Renders the main frontend page

@app.route('/pulse', methods=['GET'])
def get_pulse():
    try:
        if arduino.in_waiting > 0:  # Check if there's data in the serial buffer
            data = arduino.readline().decode('utf-8').strip()  # Read and decode the data
            return jsonify({'pulse': int(data)})  # Send pulse data to the frontend
    except Exception as e:
        print(f"Error reading from Arduino: {e}")
    return jsonify({'pulse': None})  # Return None if no data is available

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)