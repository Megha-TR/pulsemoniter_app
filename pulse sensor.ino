#include <PulseSensorPlayground.h>

const int PulseWire = 0;   // 'S' Signal pin connected to A0
const int LED13 = 13;      // The on-board Arduino LED
int Threshold = 550;       // Adjust Threshold for more accurate detection

PulseSensorPlayground pulseSensor;  // Creates a PulseSensor object

void setup() {
  Serial.begin(9600);

  // Configure the PulseSensor object
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.blinkOnPulse(LED13);       // Blink on-board LED with heartbeat
  pulseSensor.setThreshold(Threshold);   

  // Double-check PulseSensor creation
  if (pulseSensor.begin()) {
    // Serial.println("PulseSensor object created!");
  }
}

void loop() {
  if (pulseSensor.sawStartOfBeat()) {  // If a heartbeat is detected
    int myBPM = pulseSensor.getBeatsPerMinute();  // Get BPM
    // Serial.println("♥ A HeartBeat Happened!");
    // Serial.print("BPM: ");
    Serial.println(myBPM);  // Send BPM to serial monitor

    tone(8, 1000, 250);  // Sound a tone for 250ms
  }

  delay(20);  // Short delay to allow time for sensor readings
}
