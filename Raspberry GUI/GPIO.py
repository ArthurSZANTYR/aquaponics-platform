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

def check_led_status(heure_on, heure_off, ledPin):
    # Obtenir l'heure actuelle sous forme d'entier
    now_hour = datetime.datetime.now().hour

    # Vérifier si l'heure actuelle est entre heure_on et heure_off
    if heure_on <= now_hour < heure_off:
        GPIO.output(ledPin, GPIO.HIGH)
        return "GPIO HIGH"
    else:
        GPIO.output(ledPin, GPIO.LOW)
        return "GPIO LOW"
    
def check_pompe_status(time_on, time_off):
    # Obtenir l'heure actuelle
    now = datetime.datetime.now()

    # Calculer les moments pour allumer et éteindre la pompe
    pompe_on_time = now.replace(minute=time_on, second=0, microsecond=0)
    pompe_off_time = now.replace(minute=time_off, second=0, microsecond=0)

    # Vérifier si l'heure actuelle est appropriée pour activer ou désactiver la pompe
    if pompe_on_time <= now < pompe_off_time:
        GPIO.output(pompePin, GPIO.HIGH)
        return "Pompe: GPIO HIGH"
    else:
        GPIO.output(pompePin, GPIO.LOW)
        return "Pompe: GPIO LOW"

# Initialisation des compteurs pour la pompe
compteur_on = 0
compteur_off = 0

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

        # Lire les valeurs pour la pompe
        time_on_pompe = feuille['F2'].value 
        time_off_pompe = feuille['F3'].value

        # Vérifier l'état de chaque LED
        print("LED 1:", check_led_status(heure_on_led1, heure_off_led1, led1Pin))
        print("LED 2:", check_led_status(heure_on_led2, heure_off_led2, led2Pin))
        print("LED 3:", check_led_status(heure_on_led3, heure_off_led3, led3Pin))

        # Gestion de la pompe
        print(check_pompe_status(time_on_pompe, time_off_pompe))

        # Délai avant la prochaine vérification
        time.sleep(30)  # Pause de 30 secondes

except KeyboardInterrupt:
    GPIO.cleanup()
