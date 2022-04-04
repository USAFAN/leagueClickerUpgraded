import pyautogui
import time


#for 10 times
for i in range(40):

    #print mouse position
    dur=.2
    pyautogui.click(836, 705, duration=dur)
    #time.sleep(25)
    
    pyautogui.click(934,722,duration=dur)
    pyautogui.click(1202,930,duration=dur)
    time.sleep(1)

    print("sleep")
    #if the escape key is pressed, break the loop
    if pyautogui.keyDown('q'):
        print('ESC pressed')
        break
