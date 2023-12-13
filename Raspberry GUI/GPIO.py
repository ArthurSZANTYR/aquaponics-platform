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
pompePin = 2

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
        time_on_pompe = feuille['F2'].value * 30  # Convertir en secondes
        time_off_pompe = feuille['F3'].value * 30  # Convertir en secondes

        # Vérifier l'état de chaque LED
        print("LED 1:", check_led_status(heure_on_led1, heure_off_led1, led1Pin))
        print("LED 2:", check_led_status(heure_on_led2, heure_off_led2, led2Pin))
        print("LED 3:", check_led_status(heure_on_led3, heure_off_led3, led3Pin))

        # Gestion de la pompe
        if compteur_on < time_on_pompe // 30:
            GPIO.output(pompePin, GPIO.HIGH)
            print("Pompe: GPIO HIGH")
            compteur_on += 1
            compteur_off = 0
        elif compteur_off < time_off_pompe // 30:
            GPIO.output(pompePin, GPIO.LOW)
            print("Pompe: GPIO LOW")
            compteur_off += 1
            compteur_on = 0
        else:
            # Réinitialiser les compteurs si les deux conditions sont remplies
            compteur_on = 0
            compteur_off = 0

        # Délai avant la prochaine vérification
        time.sleep(5)  # Pause de 5 secondes

except KeyboardInterrupt:
    GPIO.cleanup()
