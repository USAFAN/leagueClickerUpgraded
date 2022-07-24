import pyautogui
import time


#for 10 times
for i in range(140):

    #print mouse position
    dur=.3
    pyautogui.click(88, 144, duration=dur)
    #time.sleep(25)
    
    pyautogui.click(120, 190, duration=dur)
    pyautogui.click(400,420,duration=dur)
    time.sleep(1)

    print("sleep")
    #if the escape key is pressed, break the loop
    if pyautogui.keyDown('q'):
        print('ESC pressed')
        break
    print(i)
