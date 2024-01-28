from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO
import os
from gpiozero import LED

app = Flask(__name__)
socketio = SocketIO(app)

# Initialiser les LEDs
led26 = LED(26)
led20 = LED(20)
led21 = LED(21)
led16 = LED(16)

# Valeurs par défaut des LEDs
gpio_values = {
    26: False,
    20: False,
    21: True,
    16: True
}

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('public', path)

@socketio.on('connect')
def on_connect():
    for pin, value in gpio_values.items():
        socketio.emit(f'GPIO{pin}', value)

@socketio.on('GPIO<Toggle>')
def handle_gpio_toggle(data):
    pin = data['pin']
    gpio_values[pin] = not gpio_values[pin]
    led = globals()[f'led{pin}']
    led.value = gpio_values[pin]
    socketio.emit(f'GPIO{pin}', gpio_values[pin])

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80)
