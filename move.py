import pyfirmata
import time

board = pyfirmata.Arduino('COM3') #Porta usb que se encontra ligado
PIN_RED_LED1 = 9
PIN_GREEN_LED1 = 10
PIN_BLUE_LED = 11


#Alerta de Ligado

for i in range(5):
    board.digital[PIN_RED_LED1].write(1)
    time.sleep(0.2)
    board.digital[PIN_RED_LED1].write(0)
    time.sleep(0.2)


