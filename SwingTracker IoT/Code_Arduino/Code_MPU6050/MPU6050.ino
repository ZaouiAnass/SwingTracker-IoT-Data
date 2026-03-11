#include <Wire.h>
#include <MPU6050.h>
#include <SoftwareSerial.h>

// Déclaration des objets pour MPU6050 et HC-05
MPU6050 mpu;
SoftwareSerial BTSerial(10, 11); // RX, TX pour HC-05

// Variables pour stocker les valeurs de l'accéléromètre
float ax, ay, az, vx, vy, vz;
float theta_x, theta_y;

void setup() {
  Serial.begin(9600);
  BTSerial.begin(9600);
  
  // Initialisation du MPU6050
  Wire.begin();
  mpu.initialize();
  if (!mpu.testConnection()) {
    Serial.println("MPU6050 connection failed");
    while (1);
  }
}

void loop() {
  // Lecture des valeurs de l'accéléromètre
  int16_t axRaw, ayRaw, azRaw;
  mpu.getAcceleration(&axRaw, &ayRaw, &azRaw);
  ax = axRaw / 16384.0; // Convertir les données brutes en g
  ay = ayRaw / 16384.0;
  az = azRaw / 16384.0;

  // Calcul de l'angle de frappe
  theta_x = atan2(ay, sqrt(ax * ax + az * az));
  theta_y = atan2(ax, az);
  float theta = sqrt(sq(theta_x) + sq(theta_y)) * 180 / PI;

  // Intégration numérique pour calculer la vitesse
  long currentTime = millis();
  static long previousTime = 0;
  float deltaTime = (currentTime - previousTime) / 1000.0;
  previousTime = currentTime;

  vx += ax * deltaTime;
  vy += ay * deltaTime;
  vz += az * deltaTime;
  float V = sqrt(sq(vx) + sq(vy) + sq(vz));

  // Transmission des données via Bluetooth
  BTSerial.print("Angle θ: ");
  BTSerial.print(theta);
  BTSerial.print(" degrees, Vitesse V: ");
  BTSerial.print(V);
  BTSerial.println(" m/s");

  // Affichage des données pour débogage
  Serial.print("Angle θ: ");
  Serial.print(theta);
  Serial.print(" degrees, Vitesse V: ");
  Serial.print(V);
  Serial.println(" m/s");

  delay(100); // Attente avant la prochaine lecture
}
