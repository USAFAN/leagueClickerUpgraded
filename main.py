#find picture on screen and click it
import pyautogui


onAcceptScreen = False
banned = False

while True:
    lockin = pyautogui.locateOnScreen('acceptpng.png',confidence=0.6,grayscale=True)
    banSearch= pyautogui.locateOnScreen('banSearch.png',confidence=0.6,grayscale=True)
    championPng = pyautogui.locateOnScreen('championPng.png',confidence=0.6,grayscale=True)
    
    print(lockin)
    print(banSearch)
    if lockin != None:
        print("found lockin")
        pyautogui.click(lockin)
        onAcceptScreen = True
    if banSearch != None:
        print("found banSearch")
        onAcceptScreen = False
        pyautogui.click(banSearch)
        #type "irelia" 
        pyautogui.typewrite("irelia")
        banned = True
    #reset varibles if we come back to the accept screen
    if onAcceptScreen:
        banned= False
    


