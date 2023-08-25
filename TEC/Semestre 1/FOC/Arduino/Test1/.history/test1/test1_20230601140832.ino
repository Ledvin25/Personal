void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(10, LOW);
  digitalWrite(13, HIGH);
  delay(200);
  digitalWrite(13, LOW);
  digitalWrite(10, HIGH);
  delay(200);
}
