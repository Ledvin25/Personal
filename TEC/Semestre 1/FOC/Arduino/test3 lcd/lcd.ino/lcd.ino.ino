/* 
                CREADO POR      :{==[=======>>>> ELECTROALL <<<<<=======]==}
                INSTAGRAM       : https://www.instagram.com/carlos_j_fuentess/ ó  @carlos_j_fuentess
                FACEBOOK        : https://web.facebook.com/ELECTROALL.ELECTRONICA/?_rdc=1&_rdr
                PÁGINA WEB      : https://www.electroallweb.com/
                YOUTUBE         : https://www.youtube.com/c/ELECTROALL
           ________________________________________________________
                 {==[=======> (PANTALLA LCD BÁSICO) <=======]==}
           ________________________________________________________
*/

#include <LiquidCrystal.h> // incluimos la libreria de la pantalla lcd

LiquidCrystal lcd (9,8,7,6,5,4); //reconocemos los pines de uso

void setup() {
  lcd.begin(16,4); // Reconocemos y empezamos el LCD
}

void loop() {
lcd.setCursor (0,0); // (Columna fila) 
lcd.print("SPEED: 1.4 M/S"); // imprimimos en la pantalla la palabra electroall en la primera fila

lcd.setCursor (0,2);     // (columna fila) 
lcd.print ("DISTANCE: 4CM"); // imprimimos en la pantalla la palabra electroallm en la seguna fila
}