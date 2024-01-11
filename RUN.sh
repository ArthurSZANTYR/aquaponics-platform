echo "Lancement des commandes"
cd aquaponics-platform
source source aqua-venv/bin/activate
cd Raspberry\ GUI/
nohup python GPIO.py &
python Code\ Raspberry.py 
