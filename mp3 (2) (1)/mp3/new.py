import tkinter as tk
import pytube
from pytube import YouTube
#from moviepy.editor import *

def download_video():
    video_url = url_entry.get()
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        video.download('Downloads/')
        status_label.config(text="Video downloaded successfully!")
    except pytube.exceptions.PytubeError as e:
        status_label.config(text="Error: " + str(e))

root = tk.Tk()
root.title("YouTube and MP3 Downloader")

# UI Elements
url_label = tk.Label(root, text="YouTube URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()