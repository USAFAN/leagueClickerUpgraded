import os
from tkinter import Tk, Button, Label, filedialog
from moviepy.editor import VideoFileClip

def compress_video(input_path, output_path):
    try:
        video = VideoFileClip(input_path)
        compressed_video = video.resize(video.size)  # Keep the original dimensions
        compressed_video.write_videofile(output_path, bitrate="1000k")  # Adjust the target bitrate as needed
        video.close()
        compressed_video.close()
        print(f"Compressed {input_path}")
    except Exception as e:
        print(f"Failed to compress {input_path}: {str(e)}")

def process_folder(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith((".mp4", ".avi", ".mkv")):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_folder)
                output_path = os.path.join(output_folder, relative_path)
                compress_video(input_path, output_path)

def browse_folder(label):
    folder_path = filedialog.askdirectory()
    label.config(text=folder_path)

def compress_videos_gui():
    root = Tk()
    root.title("Video Compressor")

    input_label = Label(root, text="Input Folder:")
    input_label.pack()

    input_folder_label = Label(root, text="")
    input_folder_label.pack()

    input_button = Button(root, text="Browse", command=lambda: browse_folder(input_folder_label))
    input_button.pack()

    output_label = Label(root, text="Output Folder:")
    output_label.pack()

    output_folder_label = Label(root, text="")
    output_folder_label.pack()

    output_button = Button(root, text="Browse", command=lambda: browse_folder(output_folder_label))
    output_button.pack()

    compress_button = Button(root, text="Compress Videos", command=lambda: process_folder(input_folder_label.cget("text"), output_folder_label.cget("text")))
    compress_button.pack()

    root.mainloop()

# Run the GUI
compress_videos_gui()
