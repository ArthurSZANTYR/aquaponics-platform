echo "Bienvenue chez UpFarm"
echo "............... Lancement de la ferme............."
cd aquaponie-local/aquaponics-platform
source ./aqua-venv/bin/activate
cd webserver
python3 gpio.py &
python3 webserver.py


