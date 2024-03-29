#include <Servo.h>

// Define the servo pins
const int panServoPin = 9;  // Connect to the pan servo
const int tiltServoPin = 10; // Connect to the tilt servo

// Initialize the servos
Servo panServo;
Servo tiltServo;

void setup() {
  // Attach servos to their respective pins
  panServo.attach(panServoPin);
  tiltServo.attach(tiltServoPin);

  // Set initial servo positions (adjust as needed)
  panServo.write(90);  // Center position for pan
  tiltServo.write(90); // Center position for tilt

  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // Read data from Python (format: "x,y")
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int commaIndex = data.indexOf(',');
    if (commaIndex != -1) {
      int faceX = data.substring(0, commaIndex).toInt();
      int faceY = data.substring(commaIndex + 1).toInt();

      // Map face position to servo angles (adjust as needed)
      int panAngle = map(faceX, 0, 640, 0, 180); // Assuming 640x480 resolution
      int tiltAngle = map(faceY, 0, 480, 0, 180);

      // Move the servos
      panServo.write(panAngle);
      tiltServo.write(tiltAngle);
    }
  }
}
