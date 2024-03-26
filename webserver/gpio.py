import time
import datetime
import RPi.GPIO as GPIO
import json  # Importer le module json
import os
import glob
import serial

# Initialiser la connexion série avec arduino (usb)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

# Pins Setup
pump1Pin = 26
tdsPin = 24
led1Pin = 13
led2Pin = 19

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([tdsPin], GPIO.IN)
GPIO.setup([pump1Pin], GPIO.OUT)
GPIO.setup([led1Pin], GPIO.OUT)
GPIO.setup([led2Pin], GPIO.OUT)

# Création des objets PWM pour chaque LED
pwm_led1 = GPIO.PWM(led1Pin, 1000)  # Fréquence de 1000 Hz
pwm_led2 = GPIO.PWM(led2Pin, 1000)

# Démarrage des PWM avec un duty cycle de 0 (LED éteinte)
pwm_led1.start(0)
pwm_led2.start(0)

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
    #lecture sur port analogique arduino
    print("tesssssssssst ttttttttttttddddddddddddddddsssssssssssssss")
    print(ser.in_waiting)
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)

    return int(line)


def read_led1_intensity():    
    with open(fichier_json, 'r') as file:
        data = json.load(file)
        fromUser = data.get('fromUser', {})
        led1IntensityValue = fromUser.get('led1IntensityValue', 0)  # 0 est une valeur par défaut si la clé n'existe pas
    return int(led1IntensityValue)

def read_led1_start_hour():    
    with open(fichier_json, 'r') as file:
        data = json.load(file)
        fromUser = data.get('fromUser', {})
        led1StartValue = fromUser.get('led1StartValue', 0)
    return int(led1StartValue)

def read_led1_on_time():    
    with open(fichier_json, 'r') as file:
        data = json.load(file)
        fromUser = data.get('fromUser', {})
        led1OnValue = fromUser.get('led1OnValue', 0)
    return int(led1OnValue)

def read_led2_intensity():    
    with open(fichier_json, 'r') as file:
        data = json.load(file)
        fromUser = data.get('fromUser', {})
        led2IntensityValue = fromUser.get('led2IntensityValue', 0)  # 0 est une valeur par défaut si la clé n'existe pas
    return int(led2IntensityValue)

def read_led2_start_hour():    
    with open(fichier_json, 'r') as file:
        data = json.load(file)
        fromUser = data.get('fromUser', {})
        led2StartValue = fromUser.get('led2StartValue', 0)
    return int(led2StartValue)

def read_led2_on_time():    
    with open(fichier_json, 'r') as file:
        data = json.load(file)
        fromUser = data.get('fromUser', {})
        led2OnValue = fromUser.get('led2OnValue', 0)
    return int(led2OnValue)

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


######### DS18B20 temp ##########
        # 1 - wire GPIO4 - voir fichier de config 

#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')
#
#base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'
#
#def read_temp_raw():
#    f = open(device_file, 'r')
#    lines = f.readlines()
#    f.close()
#    return lines
#
#def read_temp():
#    lines = read_temp_raw()
#    while lines[0].strip()[-3:] != 'YES':
#        time.sleep(0.2)
#        lines = read_temp_raw()
#    equals_pos = lines[1].find('t=')
#    if equals_pos != -1:
#        temp_string = lines[1][equals_pos+2:]
#        temp_c = float(temp_string) / 1000.0
#        return temp_c
#    return 25

###############################################

try:
    while True:
        #pump control by user
        pump1_status()
        
        update_led_status(read_led1_start_hour(), read_led1_on_time(), pwm_led1, intensity = read_led1_intensity())
        update_led_status(read_led2_start_hour(), read_led2_on_time(), pwm_led2, intensity = read_led2_intensity())

        # Gestion de la température
        #temperature = read_temp()
        temperature = 25
        tds = read_tds()
        print(f"TDS : {tds}")
        #tds = 1225

        update_system_data(temperature, tds)
        print("Mise à jour des données environnementales dans data.json")


        #Délai avant la prochaine vérification
        time.sleep(5)  # Pause de 5 secondes

except KeyboardInterrupt:
    GPIO.cleanup()
