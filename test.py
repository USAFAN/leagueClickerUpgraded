import pyautogui
import time
while True:

    champSearch = pyautogui.locateOnScreen('champSearch.png',confidence=0.6)
    print(champSearch)
    #click coords on screen
    if champSearch != None:
        print("found champSearch")
        pyautogui.click(champSearch.left-250,champSearch.top+50,duration=0.5)
        time.sleep(16)
