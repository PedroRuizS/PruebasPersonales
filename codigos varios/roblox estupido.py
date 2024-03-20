import concurrent.futures
import random
import keyboard
import pydirectinput
import pyautogui
import TwitchPlays_Connection
from keys import *

#########Activar para pvz, dejar comentado pa lo demas#############
pydirectinput.FAILSAFE = False
##################### Codigo Para pasarse un juego de rpblox feo


TWITCH_CHANNEL = 'eljicaleto8' 

STREAMING_ON_TWITCH = True


YOUTUBE_CHANNEL_ID = "YOUTUBE_CHANNEL_ID_HERE" 


YOUTUBE_STREAM_URL = None

##################### MESSAGE QUEUE
MESSAGE_RATE = 0.5
MAX_QUEUE_LENGTH = 20
MAX_WORKERS = 100 # Maximum number of threads you can process at a time 

last_time = time.time()
message_queue = []
thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)
active_tasks = []
pyautogui.FAILSAFE = False

##########################################################


""" countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1) """

if STREAMING_ON_TWITCH:
    t = TwitchPlays_Connection.Twitch()
    t.twitch_connect(TWITCH_CHANNEL)
else:
    t = TwitchPlays_Connection.YouTube()
    t.youtube_connect(YOUTUBE_CHANNEL_ID, YOUTUBE_STREAM_URL)

def handle_message(message):
    aux=""
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print("Got this message from " + username + ": " + msg)

#############################################################################################################        
        ###################################
        #CODIGO DE TELCADO
        ####################################
        countdown = 5

        if msg=="00'":
            print("primero")  
            aux=False  
            print(aux) 

        if msg=="11":
            print("primero")  
            aux=True
            print(aux) 
        
        if msg=="d":
            if aux== True:
                HoldAndReleaseKey(W, .5)
                HoldAndReleaseKey(SPACE, .5)
                print("1")
                aux=True 
                print(aux) 

            if aux== False:
                HoldAndReleaseKey(W, .5)
                HoldAndReleaseKey(D, .5)
                HoldAndReleaseKey(SPACE, .5)
                print("2")
                aux=True         
        
        if msg=="i" :
            if aux== True:
                HoldAndReleaseKey(W, .5)
                HoldAndReleaseKey(A, .5)
                HoldAndReleaseKey(SPACE, .5)
                aux=False 
                print("3")
            if aux== False:
                HoldAndReleaseKey(W, .5)
                HoldAndReleaseKey(SPACE, .5)
                aux=False
                print("4")    
     
        if msg=="a":
            HoldAndReleaseKey(W, .5)
            HoldAndReleaseKey(SPACE, .5)   
        if msg=="autoclick":
            while countdown > 0:
             print(countdown)
             countdown -= 1
             pydirectinput.mouseDown(button="left")
             time.sleep(0.001)
             pydirectinput.mouseUp(button="left") 
             pydirectinput.mouseDown(button="left")
             time.sleep(0.001)
             pydirectinput.mouseUp(button="left") 
             pydirectinput.mouseDown(button="left")
             time.sleep(0.001)
             pydirectinput.mouseUp(button="left") 
             time.sleep(0.01)
###################entre hileras la distancia es de 65 pixeles

    except Exception as e:
        print("Encountered exception: " + str(e))


while True:

    active_tasks = [t for t in active_tasks if not t.done()]

    #Check for new messages
    new_messages = t.twitch_receive_messages();
    if new_messages:
        message_queue += new_messages; # New messages are added to the back of the queue
        message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

    messages_to_handle = []
    if not message_queue:
        # No messages in the queue
        last_time = time.time()
    else:
        # Determine how many messages we should handle now
        r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
        n = int(r * len(message_queue))
        if n > 0:
            # Pop the messages we want off the front of the queue
            messages_to_handle = message_queue[0:n]
            del message_queue[0:n]
            last_time = time.time();

    # If user presses Shift+Backspace, automatically end the program
    if keyboard.is_pressed('shift+backspace'):
        exit()

    if not messages_to_handle:
        continue
    else:
        for message in messages_to_handle:
            if len(active_tasks) <= MAX_WORKERS:
                active_tasks.append(thread_pool.submit(handle_message, message))
            else:
                print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')
 