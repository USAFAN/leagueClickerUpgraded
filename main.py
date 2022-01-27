#find picture on screen and click it
import pyautogui

import time
accepting = True
banned = False
onAcceptScreen = True
champ = "irelia"
enemyBan = "teemo"
lockedIn = False

while True:
    lockin = pyautogui.locateOnScreen('acceptpng.png',confidence=0.6,grayscale=True)
    banSearch= pyautogui.locateOnScreen('banSearch.png',confidence=0.7)
    #championPng = pyautogui.locateOnScreen('championPng.png',confidence=0.6,grayscale=True)
    champSearch = pyautogui.locateOnScreen('champSearch.png',confidence=0.7)

    print(champSearch)
    print(lockin)
    print(banSearch)
    #if key "-" is pressed, exit program
    if pyautogui.keyDown('-'):
        print("Exiting")
        exit()
    if lockin != None and accepting:
        print("found lockin")
        pyautogui.click(lockin)
        onAcceptScreen = True
        time.sleep(5)
    if champSearch != None and not lockedIn:
        print("found banSearch")
        onAcceptScreen = False
        #click search box
        pyautogui.click(champSearch)
        
        #type "irelia" 
        pyautogui.typewrite(champ)
        time.sleep(.5)
        #click first champ icon
        pyautogui.click(champSearch.left-250,champSearch.top+50,duration=0.5)
        lockedIn = True



        #banned = True
    if banSearch != None and not banned:
        print("found banSearch")
        pyautogui.click(banSearch)
        #type "irelia" 
        pyautogui.typewrite(enemyBan)
        time.sleep(.5)
        #click first champ icon
        pyautogui.click(banSearch.left-250,banSearch.top+50,duration=0.5)
        #time.sleep(5)
        banned = True
    #reset varibles if we come back to the accept screen
    if onAcceptScreen:
        banned= False
        lockedIn = False
    


