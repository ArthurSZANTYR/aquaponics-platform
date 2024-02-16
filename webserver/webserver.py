from flask import Flask, render_template, send_from_directory, request
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

    # Mettre à jour data.json avec la nouvelle valeur
    with open('data.json', 'r+') as file:
        file_data = json.load(file)
        file_data['pumpInterval'] = data['pumpInterval']  # Assurez-vous que cette clé correspond à votre fichier JSON
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.truncate()  # Supprime le reste du fichier si nécessaire

    return {'status': 'success'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
