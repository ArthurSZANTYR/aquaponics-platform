from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_url_path='')

# Servir les fichiers statiques (html, js, css, images)
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('.', path)

# Route spécifique pour le fichier data.json
@app.route('/data.json')
def serve_data_json():
    with open('data.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)

# Page d'accueil servant index.html
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
