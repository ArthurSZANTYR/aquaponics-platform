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

@app.route('/data.json')
def data_json():
    return send_from_directory(os.getcwd(), 'data.json')

@app.route('/update-pump-interval', methods=['POST'])
def update_pump_interval():
    data = request.get_json()
    print(data)  # Pour le débogage, affiche les données reçues

    # Mettre à jour data.json avec les nouvelles valeurs
    with open('data.json', 'r+') as file:
        file_data = json.load(file)
        # Mise à jour de pump1OnValue et pump1OffValue dans data.json
        if 'pump1OnValue' in data:
            file_data['pump1OnValue'] = data['pump1OnValue']
        if 'pump1OffValue' in data:
            file_data['pump1OffValue'] = data['pump1OffValue']
        
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.truncate()  # Supprime le reste du fichier si nécessaire

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
