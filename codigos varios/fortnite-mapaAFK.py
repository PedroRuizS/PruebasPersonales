##############
##############codigo para poder estar farmeando afk en un juego tonto de fornai
##############
import time
import ctypes
import pynput
import time
from keys import *
import pydirectinput
print("YAAAA")
countdown = 5
inicio = input("Ingresa cuando quieres que empiece: ")
if inicio == "ya":
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)
    while True:

        HoldAndReleaseKey(A, .5)
        HoldAndReleaseKey(D, .5)
        pydirectinput.mouseDown(button="left")
        time.sleep(1)
        pydirectinput.mouseUp(button="left")
        time.sleep(1)