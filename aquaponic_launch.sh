echo "/////////...........Bienvenue............/////////"
echo "............... Lancement de la ferme............."
echo ".................................................."
echo "//////////////////////////////////////////////////"
<<<<<<< HEAD
ls
=======
>>>>>>> 97bf130aed03f5e720233489d0f380f1923b0c69
cd aquaponics-platform
source ./aqua-venv/bin/activate
cd webserver
python3 gpio.py &
python3 webserver.py


