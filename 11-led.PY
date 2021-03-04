# LIGANDO UM LED
from pyfirmata import Arduino
import lcd
import time

board=Arduino ('COM5')
lcd.escrever(board, 0, 0, 'LIGANDO UM LED')
lcd.escrever(board, 0, 1, 'SGMTEC1')
while True:
    board.digital[7].write(1)
    time.sleep(0.5)
    board.digital[7].write(0)
    time.sleep(0.5)
board.exit()