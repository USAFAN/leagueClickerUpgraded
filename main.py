#find picture on screen and click it
import pyautogui

import time
accepting = True
banned = False
onAcceptScreen = True
champ = "irelia"
enemyBan = "teemo"

while True:
    lockin = pyautogui.locateOnScreen('acceptpng.png',confidence=0.6,grayscale=True)
    banSearch= pyautogui.locateOnScreen('banSearch.png',confidence=0.6)
    #championPng = pyautogui.locateOnScreen('championPng.png',confidence=0.6,grayscale=True)
    champSearch = pyautogui.locateOnScreen('champSearch.png',confidence=0.6)

    
    print(lockin)
    print(banSearch)
    if lockin != None and accepting:
        print("found lockin")
        pyautogui.click(lockin)
        onAcceptScreen = True
    if champSearch != None:
        print("found banSearch")
        onAcceptScreen = False
        pyautogui.click(champSearch)
        #type "irelia" 
        pyautogui.typewrite(champ)
        time.sleep(3)

        #banned = True
    if banSearch != None:
        print("found banSearch")
        pyautogui.click(champSearch)
        #type "irelia" 
        pyautogui.typewrite(enemyBan)
        time.sleep(3)
        banned = True
    #reset varibles if we come back to the accept screen
    if onAcceptScreen:
        banned= False
    


