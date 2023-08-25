void encenderRojo();
void encenderAmarillo();
void encenderVerde();
void apagar();
int i;

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  encenderRojo();
  delay(500);
  for(i=0;i<5;i++)
  {
    apagar();
    delay(200);
    encenderRojo();
    delay(200);
  }
  apagar();	
  encenderAmarillo();
  for(i=0;i<5;i++)
  {
    apagar();
    delay(200);
    encenderAmarillo();
    delay(200);
  }
  apagar();
  encenderVerde();
  delay(10000);
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