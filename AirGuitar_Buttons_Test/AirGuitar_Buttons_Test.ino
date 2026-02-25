void setup() {
  Serial.begin(115200);
  pinMode(32, INPUT_PULLUP);
}

void loop() {
  Serial.println(digitalRead(32));
  delay(500);
}