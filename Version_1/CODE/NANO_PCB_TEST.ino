//  Hehe Armadillo hehe
//
//      ,::////;::-.
//     /:'///// ``::>/|/
//   .',  ||||    `/( e\
//-==~-'`-Xm````-mm-' `-_\ 
//
//  Eduard BreakoutShieldTest Testboard Polling Version


#include <EasyNeoPixels.h>          // Include an easier way to select certain LEDs etc


#define LED_PIN 13
#define LED_COUNT 25

void setup() {

// ==== OUTPUT PINS ====

 // A0–A5 als Output setzen (Bits 0–5 von DDRC auf 1)
  DDRC |= 0b00111111;

  // A0–A5 auf HIGH setzen (Bits 0–5 von PORTC auf 1)
  PORTC |= 0b00111111;

// ==== INPUT PINS ====

  // PORTD (D1–D6 = PD1–PD6) als Input
  DDRD &= ~0b11111110;  // PD1–PD6 als Input (lassen PD0 in Ruhe)
  PORTD &= ~0b11111110; // Kein Pullup an PD1 – PD6


  // PORTB: D8–D12 = PB0–PB4
  DDRB &= 0b00011111;   // PB0–PB4 als Input
  PORTB &= ~0b00011111; // Kein Pullup an PD8 - PD12

// Initialize NeoPixel Matrix
  setupEasyNeoPixels(LED_PIN, LED_COUNT);

// Set all Neopixel to red

  for(int i = 0; i < 26; i++){
      writeEasyNeoPixel(i, 8, 0, 0);
    }

  delay(1000);
}

void loop() {


  //Pin D1 - D6 Input und Abfrage

  //delay(20);
  
  for(int pin = 0; pin < 6; pin++){
     //delay(20);
    if(digitalRead(pin) == HIGH){
      writeEasyNeoPixel(pin, 0, 8, 0);
    }else{
      writeEasyNeoPixel(pin, 8, 0, 0);
    }
  }

  //Pin D7 - D13 als input und Abfrage aber dann die korresponderiende LED + 6 mit anmachen

  //delay(20);
  
  for(int pin = 6; pin < 12; pin++){
     //delay(20);
    if(digitalRead(pin) == HIGH){
      writeEasyNeoPixel(pin, 0, 8, 0);
      writeEasyNeoPixel((pin+6), 0, 8, 0);
    }else{
      writeEasyNeoPixel(pin, 8, 0, 0);
      writeEasyNeoPixel((pin+6), 8, 0, 0);
    }
  }

}
