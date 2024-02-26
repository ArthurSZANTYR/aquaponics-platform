import time
import datetime
import RPi.GPIO as GPIO
import json  # Importer le module json

# Pins Setup
pump1Pin = 26
tdsPin = 24
led1Pin = 13

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([tdsPin], GPIO.IN)
GPIO.setup([pump1Pin], GPIO.OUT)
GPIO.setup([led1Pin], GPIO.OUT)

# Création des objets PWM pour chaque LED
pwm_led1 = GPIO.PWM(led1Pin, 1000)  # Fréquence de 1000 Hz

# Démarrage des PWM avec un duty cycle de 0 (LED éteinte)
pwm_led1.start(0)

# Chemin du fichier JSON
fichier_json = 'data.json'

def read_pump1_values():    
    with open(fichier_json, 'r') as file:
        data = json.load(file)
        fromUser = data.get('fromUser', {})
        pump1OnValue = fromUser.get('pump1OnValue', 0)  # 0 est une valeur par défaut si la clé n'existe pas
        pump1OffValue = fromUser.get('pump1OffValue', 0)
        
    return int(pump1OnValue), int(pump1OffValue)

def pump1_status():
    time_on, time_off = read_pump1_values()
    time_on *= 60
    time_off *= 60

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


def read_led1_intensity():    
    with open(fichier_json, 'r') as file:
        data = json.load(file)
        fromUser = data.get('fromUser', {})
        led1IntensityValue = fromUser.get('led1IntensityValue', 0)  # 0 est une valeur par défaut si la clé n'existe pas

def read_led1_start_hour():    
    with open(fichier_json, 'r') as file:
        data = json.load(file)
        fromUser = data.get('fromUser', {})
        led1IntensityValue = fromUser.get('led1StartValue', 0)

def read_led1_on_time():    
    with open(fichier_json, 'r') as file:
        data = json.load(file)
        fromUser = data.get('fromUser', {})
        led1IntensityValue = fromUser.get('led1OnValue', 0)

    return int(led1IntensityValue)

def set_led_intensity(led_pwm, intensity):
    # Convertir la valeur d'intensité (0-10) en pourcentage (0-100)
    duty_cycle = intensity * 10
    led_pwm.ChangeDutyCycle(duty_cycle)

def update_led_status(start_hour, on_time, led_pwm, intensity):
    # Obtenir l'heure actuelle sous forme d'entier
    now_hour = datetime.datetime.now().hour
    print(now_hour)
    print(start_hour)
    print(start_hour + on_time)

    # Vérifier si l'heure actuelle est dans le bon créneau
    if start_hour <= now_hour < start_hour + on_time:
        set_led_intensity(led_pwm, intensity)
    else:
        set_led_intensity(led_pwm, 0)

def update_system_data(temperature, tds):
    with open(fichier_json, 'r+') as file:
        data = json.load(file)
        data['fromSystem']['temperature'] = temperature
        data['fromSystem']['tds'] = tds
        
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()


try:
    while True:
        #pump control by user
        pump1_status()

        # Gestion TDS (exemple)
        tds = read_tds()
        print(f"TDS : {tds}")

        update_led_status(read_led1_start_hour(), read_led1_on_time, pwm_led1, intensity = read_led1_intensity())

        # Gestion de la température (exemple)
        temperature = 25  # Remplacer par une vraie lecture de température

        update_system_data(temperature, tds)
        print("Mise à jour des données environnementales dans data.json")


        # Délai avant la prochaine vérification
        time.sleep(5)  # Pause de 5 secondes

except KeyboardInterrupt:
    GPIO.cleanup()
