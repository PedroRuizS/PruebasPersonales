### Ps voy a hacer una documentacion medianamente decente por si alguien ocupa este codigo en algun momento
### Primero ocupamos,tener intaladas varias cosas, Python (obvio(de preferencia instalado en PATH)), y las bibliotecas
###de python keyboard, pywin32, pyautogui, pillow y opencv-python, para instalarlas solo te vas al simbolo de sistema
### le escribes "pip install (nombre de la biblioteca)" OBVIAMENTE SIN LOS ESTOS COSOS "" NOSEAN MENSOS


from pyautogui import *
import keyboard
import pyautogui
import time#estas dos no las tienes q instalar no seas wei
import random 
import win32api, win32con #importamos todas las mugrosas bibliotecas que instalamos

#ok pues ahi va, win32 lo vamos a usar para hacer clics, podriamos usar pyautog
# ui tmb, pero segun chatgpt, win32 es mas rapido
#time lo vamos a usar para darle un tiempo de delay entre las cosas y asi


# ,gggggggggggggg                                                                                    
#dP""""""88""""""                                                                                    
#Yb,_    88                                                                                          
# `""    88                                         gg                                               
#     ggg88gggg                                     ""                                               
 #       88   8gg      gg   ,ggg,,ggg,     ,gggg,   gg     ,ggggg,    ,ggg,,ggg,    ,ggg,     ,g,    
  #      88    I8      8I  ,8" "8P" "8,   dP"  "Yb  88    dP"  "Y8ggg,8" "8P" "8,  i8" "8i   ,8'8,   
  #gg,   88    I8,    ,8I  I8   8I   8I  i8'        88   i8'    ,8I  I8   8I   8I  I8, ,8I  ,8'  Yb  
   #"Yb,,8P   ,d8b,  ,d8b,,dP   8I   Yb,,d8,_    __,88,_,d8,   ,d8' ,dP   8I   Yb, `YbadP' ,8'_   8) 
    # "Y8P'   8P'"Y88P"`Y88P'   8I   `Y8P""Y8888PP8P""Y8P"Y8888P"   8P'   8I   `Y8888P"Y888P' "YY8P8P
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    

def clickDer():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    return
def is_color_in_range(pixel, target, tolerancia):
    return all(abs(pixel[i] - target[i]) <= tolerancia for i in range(3))

def encontrarColor(screenshot, target, tolerancia):
    ancho, alto = screenshot.size

    for x in range(0, ancho, 5):  # Escanear de 5 en 5 píxeles para mayor eficiencia
        for y in range(0, alto, 5):
            pixel = screenshot.getpixel((x, y))
            if is_color_in_range(pixel, target, tolerancia):
                return (x, y)   # Devuelve las coordenadas del píxel si coincide con el color

    return None

def escaneoRegion(region, color, tolerancia=15):
    inicio_x, inicio_y, ancho, alto = region
    screenshot = pyautogui.screenshot(region=(inicio_x, inicio_y, ancho, alto))
    for x in range(0, ancho, 5):  # Escanear de 5 en 5 píxeles para mayor eficiencia
        for y in range(0, alto, 5):
            pixel = screenshot.getpixel((x, y))
            if is_color_in_range(pixel, color, tolerancia):
                return (inicio_x + x, inicio_y + y)





 #,ggg, ,ggg,_,ggg,                                  
#dP""Y8dP""Y88P""Y8b                                 
#Yb, `88'  `88'  `88                                 
# `"  88    88    88               gg                
     #88    88    88               ""                
     #88    88    88    ,gggg,gg   gg    ,ggg,,ggg,  
    # 88    88    88   dP"  "Y8I   88   ,8" "8P" "8, 
   #  88    88    88  i8'    ,8I   88   I8   8I   8I 
  #   88    88    Y8,,d8,   ,d8b,_,88,_,dP   8I   Yb,
 #    88    88    `Y8P"Y8888P"`Y88P""Y88P'   8I   `Y8
#                                                    
                                                    
                                                    
                                                    
   # Obtener las dimensiones de la pantalla
screen_width, screen_height = pyautogui.size()

# Calcular las coordenadas del centro
center_x = screen_width // 2
center_y = screen_height // 2                                                 
                                                    
print("estoy vivo")
while keyboard.is_pressed('l') == False: 
    pyautogui.keyDown('w')
    time.sleep(2)
    pyautogui.keyUp('w')
    pyautogui.keyDown('D')
    time.sleep(2)
    pyautogui.keyUp('D')
    pyautogui.keyDown('S')
    time.sleep(2)
    pyautogui.keyUp('S')
    pyautogui.keyDown('A')
    time.sleep(2)
    pyautogui.keyUp('A')

print("un loop")
#    resultado = escaneoRegion((344, 367, 1282 - 344, 50), (30, 31, 242), 10)
#   #pyautogui.displayMousePosition()
#    if resultado:
#        pyautogui.moveTo(center_x, center_y)
#        time.sleep(0.1)
#        pyautogui.moveTo(resultado)
#        pyautogui.keyDown('w')
#        time.sleep(2)
#        pyautogui.keyUp('w')
#    time.sleep(0.5)
