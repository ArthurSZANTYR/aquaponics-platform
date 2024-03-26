echo "/////////...........Bienvenue............/////////"
echo "............... Lancement de la ferme............."
echo ".................................................."
echo "//////////////////////////////////////////////////"
ls
cd aquaponics-platform
source ./aqua-venv/bin/activate
cd webserver
python3 gpio.py &
python3 webserver.py


