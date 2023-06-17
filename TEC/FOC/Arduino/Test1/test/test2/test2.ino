// Librerias
#include <LiquidCrystal.h>

const int sensorPin1 = 1;  // Pin del primer fotosensor
const int sensorPin2 = 0;  // Pin del segundo fotosensor
int umbral1 = 0;           // Umbral para el primer sensor
int umbral2 = 0;           // Umbral para el segundo sensor
float distanciaSensores = 12.2; // Distancia de los sensores


float velocidad = 0; // Variable para la velocidad
float tiempoInicial = 0;
float tiempoFinal = 0;
float tiempoDiferencia = 0;

// Sensor de sonido

int trigPin = 11;
int echoPin = 12;
long pingTravelTime;
float distance_cm;
int umbralDistancia = 0;  // Umbral para la distancia máxima en centímetros

// LCD
LiquidCrystal lcd(9, 8, 7, 6, 5, 4);

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  lcd.begin(16, 4);
  Serial.begin(9600);
  umbralSonido();
  calibrarUmbrales();
}

void loop() {
  // Verificar si el objeto está presente en el primer fotosensor
  if (analogRead(sensorPin1) < umbral1) {
    tiempoInicial = millis();  // Registrar el tiempo inicial
    Serial.println(tiempoInicial);
  }

  // Verificar si el objeto está presente en el segundo fotosensor
  if (analogRead(sensorPin2) < umbral2 && tiempoInicial != 0) {
    tiempoFinal = millis();                          // Registrar el tiempo final
    tiempoDiferencia = (tiempoFinal - tiempoInicial);  // Calcular la diferencia de tiempo

    velocidad = distanciaSensores / ((tiempoDiferencia)/1000);

    lcd.setCursor(0, 0);
    lcd.print("SPEED: ");
    lcd.setCursor(0, 1);
    lcd.print(velocidad);
    lcd.print(" cm/s.");

    // Reiniciar los tiempos para esperar el siguiente objeto
    tiempoInicial = 0;
    tiempoFinal = 0;
    tiempoDiferencia = 0;
    velocidad = 0;
    
  }

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  pingTravelTime = pulseIn(echoPin, HIGH);
  distance_cm = pingTravelTime / 58.0;  // Convertir el tiempo de viaje a distancia en centímetros

  if (distance_cm < umbralDistancia) {
    lcd.setCursor(0, 2);
    lcd.print("DISTANCE: ");
    lcd.setCursor(0, 3);
    lcd.print(distance_cm);
    lcd.print(" cm.");
  }

  delay(100);
}

void umbralSonido()
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  pingTravelTime = pulseIn(echoPin, HIGH);
  distance_cm = pingTravelTime / 58.0;  // Convertir el tiempo de viaje a distancia en centímetros

  umbralDistancia = distance_cm - 2;

  Serial.println(umbralDistancia);
  Serial.println("cm");

  lcd.setCursor(0, 0);
  lcd.print(umbralDistancia);

  delay(600);
}

void calibrarUmbrales() {
  lcd.setCursor(0, 0);
  lcd.print("No coloque nada");
  lcd.setCursor(0, 0);
  lcd.setCursor(0,1);
  lcd.print("frente a los");
  lcd.setCursor(0,2);
  lcd.print("sensores");

  for (int i = 0; i < 3; i++) {
    lcd.setCursor(0, 3);
    lcd.print("Calibrando en ");
    lcd.print(3 - i);
    lcd.print(" segundos");
    delay(1000);
  }

  int lectura1 = analogRead(sensorPin1);
  umbral1 = lectura1 - 1;  // Ajustar el umbral para el primer sensor
  Serial.println(umbral1);

  int lectura2 = analogRead(sensorPin2);
  umbral2 = lectura2 - 1;  // Ajustar el umbral para el segundo sensor
  Serial.println(umbral2);

  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print(umbral1);
  lcd.setCursor(0, 1);
  lcd.print(umbral2);

  delay(800);

  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("SPEED:");

  lcd.setCursor(0, 2);
  lcd.print("DISTANCE:");
}
