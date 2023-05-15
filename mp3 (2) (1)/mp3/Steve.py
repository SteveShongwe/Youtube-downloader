import tkinter as tk
import pytube
import os
from pytube import YouTube
#from moviepy.editor import *

def download_video():
    #video_url = url_entry.get()
    video_file = url_entry.get()
    try:
        yt = YouTube(video_file)
        video =  yt.streams.filter(only_audio=True).first()
        out_file = "Downloads/"
        download_file = video.download("Downloads/")
        base, ext = os.path.splitext(download_file)
        new_file = base + '.mp3'
        os.rename(download_file, new_file)
        status_label.config(text="Video downloaded successfully!")
        status_label.config(text="Conversion to MP3 completed!")
    except OSError as e:
        status_label.config(text="Error: " + str(e))
    '''
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        video.download('Downloads/')
        status_label.config(text="Video downloaded successfully!")
    except pytube.exceptions.PytubeError as e:
        status_label.config(text="Error: " + str(e))
    '''

def convert_to_mp3():
    video_file = url_entry.get()
    try:
        yt = YouTube(video_file)
        video =  yt.streams.filter(only_audio=True).first()
        out_file = "Downloads/"
        download_file = video.download(output_path=out_file)
        base, ext = os.path.splitext(download_file)
        new_file = base + '.mp3'
        os.rename(download_file, new_file)
        status_label.config(text="Video downloaded successfully!")
        status_label.config(text="Conversion to MP3 completed!")
    except OSError as e:
        status_label.config(text="Error: " + str(e))

root = tk.Tk()
root.title("YouTube and MP3 Downloader")

# UI Elements
url_label = tk.Label(root, text="YouTube URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack()

file_label = tk.Label(root, text="Video File Path:")
file_label.pack()
file_entry = tk.Entry(root, width=50)
file_entry.pack()

convert_button = tk.Button(root, text="Convert to MP3", command=convert_to_mp3)
convert_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
