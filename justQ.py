import pyautogui
import time
i = 0
while True:
    i+=1
    print(i)
    champSearch = pyautogui.locateOnScreen('lockinPng.png',confidence=0.7)
    print(champSearch)
    if champSearch != None:
        print("found lockinPng")
        pyautogui.click(champSearch,duration=0.5)
        time.sleep(5)
        
    time.sleep(3)