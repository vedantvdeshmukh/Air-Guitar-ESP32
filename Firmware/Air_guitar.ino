#include <Wire.h>
#include "I2Cdev.h"
#include "MPU6050.h"
MPU6050 mpu;

// Button pins
#define B1 25
#define B2 33
#define B3 32

// Strum control
unsigned long lastStrumTime = 0;
const int strumDelay = 80 ;    // 🔥 reduced from 400 → FAST response
const int threshold = 12000;  // adjust if needed

void setup() {
  Serial.begin(115200);

  pinMode(B1, INPUT_PULLUP);
  pinMode(B2, INPUT_PULLUP);
  pinMode(B3, INPUT_PULLUP);

  Wire.begin();
  Wire.setClock(400000); // 🔥 faster MPU communication

  mpu.initialize();

  Serial.setTimeout(5); // 🔥 faster serial

  Serial.println("Air Guitar Ready");
}

String getChord() {
  bool b1 = !digitalRead(B1);
  bool b2 = !digitalRead(B2);
  bool b3 = !digitalRead(B3);

  if (!b1 && !b2 && !b3) return "C";
  if (!b1 && !b2 && b3)  return "D";
  if (!b1 && b2 && !b3)  return "E";
  if (!b1 && b2 && b3)   return "F";
  if (b1 && !b2 && !b3)  return "G";
  if (b1 && !b2 && b3)   return "A";
  if (b1 && b2 && !b3)   return "Em";
  if (b1 && b2 && b3)    return "Am";

  return "C";
}

void loop() {
  int16_t ax, ay, az;
  mpu.getAcceleration(&ax, &ay, &az);

  unsigned long currentTime = millis();

  // 🔥 improved strum detection (fast + clean)
  if (abs(ay) > threshold && (currentTime - lastStrumTime > strumDelay)) {

    String chord = getChord();
    Serial.println(chord);

    lastStrumTime = currentTime;
  }
}