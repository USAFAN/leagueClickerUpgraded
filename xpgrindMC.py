import pyautogui
import time

#after 10 seconds, click the mouse every 11 seconds
#delay=input("Enter delay u want between clicks: ")
#print(delay)
#c#licks = input("Enter number of clicks u want: ")
#@print("YOU HAVE 5 SECONDS TO LOCK IN TO MINECRAFT")

time.sleep(5)
for i in range(int(55555)):
    #pyautogui.click()
    #ask the user for a number make sure it is a number then put it in the variable i
    
    #left click
    pyautogui.leftClick()
    print('clicked '+str(i+1))
    time.sleep(int(11))
    
    