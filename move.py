import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

while True:
    board.digital[11].write(0)
    board.digital[9].write(0)
    time.sleep(0.5)
    board.digital[11].write(0)
    board.digital[9].write(0)
    time.sleep(0.5)