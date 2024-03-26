echo "/////////...........Bienvenue............/////////"
echo "............... Lancement de la ferme............."
echo ".................................................."
echo "//////////////////////////////////////////////////"
cd aquaponics-platform
source ./aqua-venv/bin/activate
cd webserver
python3 gpio.py &
python3 webserver.py &
xdg-open http://172.21.73.18:8000/index.html


