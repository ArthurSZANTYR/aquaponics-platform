from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data.json')
def data_json():
    return send_from_directory(os.getcwd(), 'data.json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
