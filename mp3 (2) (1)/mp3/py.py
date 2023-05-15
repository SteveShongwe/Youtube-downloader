import tkinter as tk
import pytube
from pytube import YouTube
#import customtkinter
import os.path
#import glob
#from PIL import ImageTk, Image
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

def convert_to_mp3():
    video_url = url_entry.get()
    try:
        yt = YouTube(video_url)
        video = yt.streams.filter(only_audio=True).first()
        download_file = video.download('Downloads/')
        base, ext = os.path.splitext(download_file)
        new_file = base + '.mp3'
        os.rename(download_file, new_file)
        status_label.config(text="Video downloaded successfully!")
        #print("Downloaded")
        #convert_to_mp3(dvideo)
    except pytube.exceptions.PytubeErrclearor as e:
        status_label.config(text="Error: " + str(e))


root = tk.Tk()
root.title("YouTube and MP3 Downloader")

url_label = tk.Label(text="YouTube URL:", font=('Century Gothic', 20))
url_label.place(x=50,y=45)
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

convert_button = tk.Button(root, text="Convert to MP3", command=download_video)
convert_button.pack()

file_label = tk.Label(root, text="Video File Path:")
file_label.pack()
file_entry = tk.Entry(root, width=50)
file_entry.pack()

convert_button = tk.Button(root, text="Convert to MP3", command=convert_to_mp3)
convert_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()