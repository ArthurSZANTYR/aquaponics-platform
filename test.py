import Adafruit_DHT
import time

# Configuration du capteur :
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 2  # Assurez-vous que ce numéro de broche est correct pour votre configuration

def read_dht11():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temperature = {:.1f} °C".format(temperature))
        print("Humidite = {:.1f} %".format(humidity))
    else:
        print("Echec de lecture du capteur. Verifiez votre cablage.")

def main():
    while True:
        read_dht11()
        time.sleep(10)  # Attend 10 secondes avant de relire

if _name_ == "_main_":
    main()