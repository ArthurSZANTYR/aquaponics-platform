import time
import datetime
import RPi.GPIO as GPIO
import json  # Importer le module json

# Pins Setup
pump1Pin = 26
tdsPin = 24

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([tdsPin], GPIO.IN)
GPIO.setup([pump1Pin], GPIO.OUT)

# Chemin du fichier JSON
fichier_json = 'data.json'

def read_pump1_values():    
    with open(fichier_json, 'r') as file:
        data = json.load(file)
        pump1OnValue = data.get('pump1OnValue', 0)  # 0 est une valeur par défaut si la clé n'existe pas
        pump1OffValue = data.get('pump1OffValue', 0)
        
    return int(pump1OnValue), int(pump1OffValue)

def pump1_status():
    time_on, time_off = read_pump1_values()

    now = datetime.datetime.now()
    
    temps_ecoule = now.hour * 3600 + now.minute * 60 + now.second    # Calculer le temps écoulé depuis minuit en secondes

    cycle_total = time_on + time_off

    if temps_ecoule % cycle_total < time_on:  #si temps ecoulé divisible par temp cycle on change de status
        GPIO.output(pump1Pin, GPIO.HIGH)
        return "pump1Pin: HIGH"
    else:
        GPIO.output(pump1Pin, GPIO.LOW)
        return "pump1Pin: LOW"

def read_tds():
    analog_value = GPIO.input(tdsPin)
    #voltage = analog_value / ADC_RESOLUTION * VREF
    #tds_value = voltage 
    return analog_value


try:
    while True:
        #pump control by user
        pump1_status()

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
    GPIO.cleanup()
