import pyautogui
import time

import multiprocessing
# for playing note.wav file

print('playing sound using  playsound')

i = 0


while True:
    try:
        #open a file called counter.txt and add a new line to it with the current time in texas time
        with open('counter.txt', 'a') as f:
            f.write(time.strftime('%H:%M:%S\n'))
        i+=1
        print(i)
        champSearch = pyautogui.locateOnScreen('lockinPng.png',confidence=0.7)
        print(champSearch)
        if champSearch != None:
             #play sound on a new thread then delete it
            
            time.sleep(0.5)
            
            #pyautogui.click(champSearch)
            print('locked in')
            time.sleep(1)
            
            print('playing sound using  playsound')
            print("found lockinPng")
            pyautogui.click(champSearch,duration=0.5)
            time.sleep(5)
            
        time.sleep(3)
    except:
        pass