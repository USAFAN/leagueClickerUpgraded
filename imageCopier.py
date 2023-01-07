import tkinter as tk
from tkinter import filedialog, ttk
import os
import shutil
def select_source_folder():
    global source_folder
    source_folder = filedialog.askdirectory()
    print(f"Selected source folder: {source_folder}")

def select_destination_folder():
    global destination_folder
    destination_folder = filedialog.askdirectory()
    print(f"Selected destination folder: {destination_folder}")

def copy_images():
    num_files = 0
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                num_files += 1

    print("Copying images...")
    num_copied = 0
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                shutil.copy(os.path.join(root, file), destination_folder)
                num_copied += 1
                print(f"{num_copied}/{num_files} images copied")
    print("Done.")


root = tk.Tk()

source_button = tk.Button(text="Select Source Folder", command=select_source_folder)
destination_button = tk.Button(text="Select Destination Folder", command=select_destination_folder)
copy_button = tk.Button(text="Copy Images", command=copy_images)

source_button.pack()
destination_button.pack()
copy_button.pack()

root.mainloop()
