import time
import datetime
import RPi.GPIO as GPIO
import json  # Importer le module json

# Pins Setup
led1Pin = 13
led2Pin = 3
led3Pin = 4
pompePin = 26
tdsPin = 24

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([led1Pin, led2Pin, led3Pin, pompePin], GPIO.OUT)
GPIO.setup([tdsPin], GPIO.IN)

# Création des objets PWM pour chaque LED
pwm_led1 = GPIO.PWM(led1Pin, 1000)  # Fréquence de 1000 Hz
pwm_led2 = GPIO.PWM(led2Pin, 1000)
pwm_led3 = GPIO.PWM(led3Pin, 1000)

# Démarrage des PWM avec un duty cycle de 0 (LED éteinte)
pwm_led1.start(0)
pwm_led2.start(0)
pwm_led3.start(0)

#TDS setup
VREF = 5.0
ADC_RESOLUTION = 1024.0

# Chemin du fichier JSON
fichier_json = 'data.json'

def read_pump_interval():
    with open(fichier_json, 'r') as file:
        data = json.load(file)
        return int(data.get('pumpInterval', 0))  # Utilisez une valeur par défaut de 0 si non trouvé


def set_led_intensity(led_pwm, intensity):
    # Convertir la valeur d'intensité (0-10) en pourcentage (0-100)
    duty_cycle = intensity * 10
    led_pwm.ChangeDutyCycle(duty_cycle)

def read_tds():
    analog_value = GPIO.input(tdsPin)
    voltage = analog_value / ADC_RESOLUTION * VREF
    tds_value = voltage # Ici, insérez la formule correcte pour calculer la valeur TDS
    return tds_value

try:
    while True:
        #pump control by user
        pump_interval = read_pump_interval()


        # Gestion TDS (exemple)
        tds = read_tds()
        print(f"TDS : {tds}")

        # Gestion de la température (exemple)
        temperature = 25  # Remplacer par une vraie lecture de température

        # Écriture dans le fichier JSON
        data = {
            "temperature": temperature,
            "tds": tds
        }
        
        with open(fichier_json, 'w') as f:
            json.dump(data, f)
        
        print(f"Écriture dans {fichier_json}: {data}")

        # Délai avant la prochaine vérification
        time.sleep(5)  # Pause de 5 secondes

except KeyboardInterrupt:
    pwm_led1.stop()
    pwm_led2.stop()
    pwm_led3.stop()
    GPIO.cleanup()
