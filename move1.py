from pyfirmata import Arduino, util
from flask import Flask, render_template
import time

app = Flask(__name__)

board = Arduino('COM3') # Alterar para o porta serial correspondente no seu sistema

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led/<int:status>')
def led(status):
    pin = 9
    board.digital[pin].write(status)
    return 'Led is %s' % ('on' if status else 'off')

@app.route('/piscar-led/<int:pin>')
def blink(pin):
    for i in range(10):
        board.digital[pin].write(1)
        time.sleep(0.5)
        board.digital[pin].write(0)
        time.sleep(0.5)
    return "Led piscando no pino " + str(pin)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
