#define B1 32

void setup() {
  Serial.begin(115200);
  pinMode(B1, INPUT_PULLUP);
}

void loop() {
  int state = digitalRead(B1);

  if(state == LOW) {
    Serial.println("BUTTON PRESSED");
  } else {
    Serial.println("BUTTON NOT PRESSED");
  }

  delay(300);
}