import time
import datetime
import RPi.GPIO as GPIO
from openpyxl import load_workbook

# Chemin du fichier Excel existant
fichier_excel = 'Aquapo.xlsx'

# Pins Setup
led1Pin = 13
led2Pin = 3
led3Pin = 4
pompePin = 26

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([led1Pin, led2Pin, led3Pin, pompePin], GPIO.OUT)

# Création des objets PWM pour chaque LED
pwm_led1 = GPIO.PWM(led1Pin, 1000)  # Fréquence de 1000 Hz
pwm_led2 = GPIO.PWM(led2Pin, 1000)
pwm_led3 = GPIO.PWM(led3Pin, 1000)

# Démarrage des PWM avec un duty cycle de 0 (LED éteinte)
pwm_led1.start(0)
pwm_led2.start(0)
pwm_led3.start(0)


def set_led_intensity(led_pwm, intensity):
    # Convertir la valeur d'intensité (0-10) en pourcentage (0-100)
    duty_cycle = intensity * 10
    led_pwm.ChangeDutyCycle(duty_cycle)

def check_led_status(heure_on, heure_off, led_pwm, intensity):
    # Obtenir l'heure actuelle sous forme d'entier
    now_hour = datetime.datetime.now().hour

    # Vérifier si l'heure actuelle est entre heure_on et heure_off
    if heure_on <= now_hour < heure_off:
        set_led_intensity(led_pwm, intensity)
        return "LED ON avec intensité: " + str(intensity)
    else:
        set_led_intensity(led_pwm, 0)
        return "LED OFF"
    
def check_pompe_status(time_on, time_off):
    # Obtenir l'heure actuelle
    now = datetime.datetime.now()
    
    # Calculer le temps écoulé depuis minuit en secondes
    temps_ecoule = now.hour * 3600 + now.minute * 60 + now.second

    # Durée totale du cycle de la pompe (en secondes)
    cycle_total = time_on + time_off

    # Utilisation du modulo pour déterminer si la pompe doit être activée
    if temps_ecoule % cycle_total < time_on:
        GPIO.output(pompePin, GPIO.HIGH)
        return "Pompe: GPIO HIGH"
    else:
        GPIO.output(pompePin, GPIO.LOW)
        return "Pompe: GPIO LOW"

try:
    while True:
        # Charger le workbook (classeur) à chaque itération
        workbook = load_workbook(fichier_excel)
        feuille = workbook.active

        # Lire les heures pour les LEDs
        heure_on_led1 = feuille['B2'].value
        heure_off_led1 = feuille['B3'].value
        heure_on_led2 = feuille['C2'].value
        heure_off_led2 = feuille['C3'].value
        heure_on_led3 = feuille['D2'].value
        heure_off_led3 = feuille['D3'].value

        intensite_led1 = feuille['B4'].value
        intensite_led2 = feuille['C4'].value
        intensite_led3 = feuille['D4'].value

        # Lire les valeurs pour la pompe
        time_on_pompe = feuille['F2'].value*30   
        time_off_pompe = feuille['F3'].value*30  #en secondes

        # Vérifier l'état de chaque LED
        print("LED 1:", check_led_status(heure_on_led1, heure_off_led1, pwm_led1, intensite_led1))
        print("LED 2:", check_led_status(heure_on_led2, heure_off_led2, pwm_led2, intensite_led2))
        print("LED 3:", check_led_status(heure_on_led3, heure_off_led3, pwm_led3, intensite_led3))

        # Gestion de la pompe
        print(check_pompe_status(time_on_pompe, time_off_pompe))

        # Délai avant la prochaine vérification
        time.sleep(5)  # Pause de 30 secondes

except KeyboardInterrupt:
    pwm_led1.stop()
    pwm_led2.stop()
    pwm_led3.stop()
    GPIO.cleanup()
