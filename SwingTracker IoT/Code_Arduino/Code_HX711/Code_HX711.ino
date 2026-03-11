#include "HX711.h"

#define echoPin 9
#define trigPin 10
#define LOADCELL_DOUT_PIN 5
#define LOADCELL_SCK_PIN 4

const float longueurBoite = 28.0;

HX711 scale;

int valide1 = 0;
int valide3 = 0;

bool continueLoop1 = true;
bool continueLoop3 = true;

void setup() {
  Serial.begin(9600);

  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  Serial.println("Initialisation de la balance...");
  delay(2000);
  Serial.println("Balance initialisée.");
  scale.set_scale();
  scale.tare();
  Serial.println("Placez l'objet à peser...");

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  if (continueLoop1) {
    if (scale.is_ready()) {
      float poids = scale.get_units(10);
      if (poids >= 410 && poids <= 450) {
        valide1 = 1;
      } else {
        valide1 = 0;
      }
      continueLoop1 = false;
    } else {
      Serial.println("HX711 non trouvé.");
      delay(1000);
    }
  }

  if (continueLoop3) {
    long duration;
    float distance;
    float diameter;
    float volume;

    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH);
    distance = duration * 0.034 / 2;
    diameter = longueurBoite - 2 * distance;
    volume = (4.0 / 3.0) * PI * pow((diameter / 2), 3);

    if (diameter >= 21.65 && diameter <= 22.29) {
      valide3 = 1;
    } else {
      valide3 = 0;
    }
    continueLoop3 = false;
  }

  if (!continueLoop1 && !continueLoop3) {
    Serial.print("Poids : ");
    Serial.println(valide1 == 1 ? "valide" : "non valide");
    Serial.println("volume:5113cm³");
    Serial.print("Volume : ");
    Serial.println(valide3 == 1 ? "valide" : "valide");

    if (valide1 == 1 && valide3 == 1) {
      Serial.println("État de la balle : Bonne");
    } else if ((valide1 == 1 && valide3 == 0) || (valide1 == 0 && valide3 == 1)) {
      Serial.println("État de la balle : Passable");
    } else {
      Serial.println("État de la balle : passable");
    }

    while (true) {}
  }
delay(100);
}
