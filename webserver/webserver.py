from flask import Flask, render_template, send_from_directory, request, jsonify
import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def dashboard():
    return render_template('index.html')

@app.route('/pump1.html')
def pump():
    return render_template('pump1.html')

@app.route('/led1.html')
def led1():
    return render_template('led1.html')

@app.route('/led2.html')
def led2():
    return render_template('led2.html')

@app.route('/data.json')
def data_json():
    return send_from_directory(os.getcwd(), 'data.json')

@app.route('/update-pump-interval', methods=['POST'])
def update_pump_interval():
    data = request.get_json()
    print(data)  # Pour le débogage, affiche les données reçues

    # Accéder au sous-objet 'fromUser' pour obtenir les valeurs
    fromUser = data.get('fromUser', {})

    # Mettre à jour data.json avec les nouvelles valeurs
    with open('data.json', 'r+') as file:
        file_data = json.load(file)

        # Assurez-vous que 'fromUser' existe dans file_data, sinon créez-le
        if 'fromUser' not in file_data:
            file_data['fromUser'] = {}
        
        # Mise à jour des valeurs
        if 'pump1OnValue' in fromUser:
            file_data['fromUser']['pump1OnValue'] = fromUser['pump1OnValue']
        if 'pump1OffValue' in fromUser:
            file_data['fromUser']['pump1OffValue'] = fromUser['pump1OffValue']
        
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.truncate()  # Supprime le reste du fichier si nécessaire

    return jsonify({'status': 'success'}), 200

@app.route('/update-led-interval', methods=['POST'])
def update_led_interval():
    data = request.get_json()
    print(data)  # Pour le débogage, affiche les données reçues

    # Accéder au sous-objet 'fromUser' pour obtenir les valeurs
    fromUser = data.get('fromUser', {})

    # Mettre à jour data.json avec les nouvelles valeurs
    with open('data.json', 'r+') as file:
        file_data = json.load(file)

        # Assurez-vous que 'fromUser' existe dans file_data, sinon créez-le
        if 'fromUser' not in file_data:
            file_data['fromUser'] = {}
        
        # Mise à jour des valeurs
        if 'led1IntensityValue' in fromUser:
            file_data['fromUser']['led1IntensityValue'] = fromUser['led1IntensityValue']
        if 'led2IntensityValue' in fromUser:
            file_data['fromUser']['led2IntensityValue'] = fromUser['led2IntensityValue']
        if 'led1OnValue' in fromUser:
            file_data['fromUser']['led1OnValue'] = fromUser['led1OnValue']
        if 'led2OnValue' in fromUser:
            file_data['fromUser']['led2OnValue'] = fromUser['led2OnValue']

        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.truncate()  # Supprime le reste du fichier si nécessaire

    return jsonify({'status': 'success'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
