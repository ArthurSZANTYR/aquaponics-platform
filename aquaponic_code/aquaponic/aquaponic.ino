const int pompePin = 2;
const int led1Pin = 9;

//pompe time control
unsigned long previousMillisPump = 0; // Variable pour suivre le temps écoulé pour la pompe
const long pumpOnDuration = 180000; //3min30 //90000; // Durée d'activation de la pompe (1 minute 30 secondes en millisecondes)
const long pumpOffDuration = 240000; //4min30 // Durée de désactivation de la pompe (15 minutes en millisecondes)
bool pompeActive = false;

//led1 time control
unsigned long previousMillisLED = 0;
const long ledOffDuration = 90000;//28800000; // Durée de 8 heures pour la LED éteinte (en millisecondes)
const long ledOnDuration = 90000;//57600000; // Durée de 16 heures pour la LED allumée (en millisecondes)

// Setup for the stepper motor
const int stepPin = 2;
const int dirPin = 15;
const int sleepPin = 16;
const int enablePin = 4;
const int stepsPerRev = 200;
int pulseWidthMicros = 1000;  // microseconds
int millisBtwnSteps = 10000;


void setup() {
  Serial.begin(9600);
  pinMode(pompePin, OUTPUT);
  pinMode(led1Pin, OUTPUT);
}

void loop() {
  unsigned long currentMillis = millis(); // Obtenez le temps actuel

  // Contrôle de la pompe
  if (!pompeActive && (currentMillis - previousMillisPump >= pumpOffDuration)) {
    previousMillisPump = currentMillis; // Réinitialiser le temps précédent
    digitalWrite(pompePin, HIGH); // Activez la pompe
    pompeActive = true;
  } else if (pompeActive && (currentMillis - previousMillisPump >= pumpOnDuration)) {
    previousMillisPump = currentMillis; // Réinitialiser le temps précédent
    digitalWrite(pompePin, LOW); // Désactivez la pompe
    pompeActive = false;
  }

  //control led1
  // Contrôle de la LED pour 16 heures (Allumée) après 8 heures (Éteinte)
  if (currentMillis - previousMillisLED <= ledOffDuration) {
    // Si moins de 8 heures se sont écoulées, garder la LED éteinte
    analogWrite(led1Pin, 0); // Éteindre la LED
  } else if (currentMillis - previousMillisLED <= ledOffDuration + ledOnDuration) {
    // Si moins de 16 heures au total se sont écoulées, allumer la LED
    analogWrite(led1Pin, 127); // Allumer la LED
  } else {
    // Réinitialiser le temps pour recommencer le cycle 24 heures
    previousMillisLED = currentMillis;
  }


}

// function to turn the stepper motor and nurrish fish
void nourish() {
  //turn on the stepper
  //Serial.println(F("Distribution of food"));  
  //digitalWrite(LED_v, HIGH);

  //wake up the stepper
  digitalWrite(sleepPin, HIGH);
  digitalWrite(enablePin, LOW);
  delay(2000);
  
  digitalWrite(dirPin, LOW);  // Enables the motor to move in a particular direction
    // Makes 200 pulses for making one full cycle rotation
  for (int i = 0; i < 1 * stepsPerRev; i++) 
  {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(pulseWidthMicros);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(millisBtwnSteps);
  }
  //turn off the stepper
  digitalWrite(sleepPin,LOW);
  digitalWrite(enablePin, HIGH);
  //digitalWrite(LED_v, LOW);
}
