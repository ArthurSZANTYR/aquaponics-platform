import serial
import time

# Initialiser la connexion série (assurez-vous que le port est correct)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(f"Valeur lue du capteur TDS: {line}")
        # Ici, vous pouvez ajouter un traitement supplémentaire des données
