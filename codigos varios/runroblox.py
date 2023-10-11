##############
##############codigo para poder estar farmeando afk en un juego tonto de roblox
##############
import time
import ctypes
import pynput
import time
from keys import *

print("YAAAA")
countdown = 5
inicio = input("Ingresa cuando quieres que empiece: ")
if inicio == "ya":
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)
    while True:
        HoldKey(W)
        
        time.sleep(5)
