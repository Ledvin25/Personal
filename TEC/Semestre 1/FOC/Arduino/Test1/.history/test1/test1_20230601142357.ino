void encenderRojo();

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  encenderVerde();
  delay(500);
  for(i=0,i<5,i++){
    apagar();
    delay(500);
    encenderVerde();
    delay(500);
  }
  apagar();	
  encenderAmarillo();
  for(i=0,i<5,i++){
    apagar();
    delay(500);
    encenderVerde();
    delay(500);
  }
  apagar();
  encenderRojo();
  delay(10000)
  
  
}
void encenderRojo() {
    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
    digitalWrite(11, HIGH);
  }
void encenderAmarillo() {
    digitalWrite(13, LOW);
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
  }
void encenderVerde() {
    digitalWrite(13, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
  }
void apagar() {
    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
  }