import pyautogui
import time
i = 0
msg = "me and pill cosby are going bot we are duo"
while True:
    i+=1
    print(i)
    champSearch = pyautogui.locateOnScreen('chat.png',confidence=0.7)
    print(champSearch)
    if champSearch != None:
        print("found lockinPng")
        pyautogui.click(champSearch,duration=0.1)
        #type msg variable
        pyautogui.typewrite(msg,interval=0.01)
        pyautogui.press('enter')
        time.sleep(2)
    time.sleep(2)