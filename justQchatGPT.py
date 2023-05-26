import pyautogui
import time
from playsound import playsound
import multiprocessing

def main():
    print('Playing sound using playsound')

    i = 0

    while True:
        try:
            # Open a file called counter.txt and append the current time in Texas time
            with open('counter.txt', 'a') as f:
                f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - Q Search\n')

            i += 1
            print(i)

            # Search for the lockinPng.png image on all screens
            q_search = pyautogui.locateOnScreen('lockinPng.png', confidence=0.7)
            print(str(q_search)+"q")
            
            garen_search = pyautogui.locateOnScreen('garenLockin2.png', confidence=0.9)
            print(str(garen_search)+"graen")
          
            mord_search = pyautogui.locateOnScreen('mordBan.png', confidence=0.9)
            print(str(mord_search)+"mord")
            pick_search = pyautogui.locateOnScreen('pick.png', confidence=0.9)
            print(str(pick_search)+"pick")
            ban_search = pyautogui.locateOnScreen('ban.png', confidence=0.9)
            print(str(ban_search)+"ban")
            if q_search is not None:
                # Play sound on a new process
                print("q found")
                multiprocessing.Process(target=playsound, args=('D:\python2022\leagueClickerUpgraded\promt.mp3',)).start()

                time.sleep(0.5)

                print('Locked in')
                time.sleep(1)
                print('Playing sound using playsound')
                print("Found lockinPng")

                # Click on the found image
                pyautogui.click(q_search, duration=0.5)

                time.sleep(5)
            if garen_search is not None and pick_search is not None:
                print("garen found")
                multiprocessing.Process(target=playsound, args=('D:\python2022\leagueClickerUpgraded\demacia.mp3',)).start()
                pyautogui.click(garen_search, duration=0.5)
                time.sleep(0.5)
                

                

                print('Locked in graen')
                
                print('Playing sound using playsound')
                print("Found lockinPng")

               
                

                time.sleep(10)
            if mord_search is not None and ban_search is not None:
                print("mordbanned")
                multiprocessing.Process(target=playsound, args=('D:\python2022\leagueClickerUpgraded\can.mp3',)).start()
                pyautogui.click(mord_search, duration=0.5)
                time.sleep(0.5)
                

                

                print('mord banned')
                
                print('Playing sound using playsound')
                print("Found lockinPng")

               
                

                time.sleep(10)

            time.sleep(3)
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()