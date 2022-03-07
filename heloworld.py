from tkinter import *
import time
from xml.etree.ElementPath import _callback
root = Tk()
from tkinter import ttk
root.attributes('-topmost', True)
def lift_window():
    
    root.lift()
    print("lift")
        #root.after(1000, lift_window)
        #time.sleep(2)

a = Label(root, text ="Hello World")
a.pack()
root.after(100, lift_window,callback=1)
root.mainloop()