from logging import NullHandler
from re import X

import pyautogui
import time
import keyboard


xy1=0
xy2=0
xy3=0
#for 10 times
print("setting pos1=q and pos2=w and pos3=e")
while True:  # making a loop
    
    try:  # used try so that if user pressed other than the given key error will not be shown
        # if the 3 global variables are not set
        
            
        
           
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('press q to store mouse position 1 of 3')
                #print mouse position
                print(pyautogui.position())
                  # finishing the loop
                xy1=pyautogui.position()
            if keyboard.is_pressed('w'):  # if key 'q' is pressed 
                print('press q to store mouse position 2 of 3')
                #print mouse position
                xy2=pyautogui.position()
                print(pyautogui.position())
                  # finishing the loop
            if keyboard.is_pressed('e'):  # if key 'q' is pressed 
                print('press q to store mouse position 3 of 3')
                #print mouse position
                xy3=pyautogui.position()
                print(pyautogui.position())
                  # finishing the loop
            #if the 3 global variables are no longer 0 break
            if xy1 != 0 and xy2 != 0 and xy3 != 0:
                print("break")
                break
            
    except:
        pass
print(xy1,xy2,xy3)
for i in range(140):

    #print mouse position
    dur=.3
    #click on the first position
    pyautogui.click(xy1,duration=dur)
    #pyautogui.click(88, 144, duration=dur)
    #time.sleep(25)
    
    pyautogui.click(xy2, duration=dur)
    pyautogui.click(xy3,duration=dur)
    time.sleep(1)

    print("sleep")
    #if the escape key is pressed, break the loop
    if pyautogui.keyDown('q'):
        print('ESC pressed')
        break
    print(i)
    #time.sleep(5)