import tkinter as tk
from tkinter import *
import pytube
from pytube import YouTube
import customtkinter
from PIL import ImageTk, Image
import os.path
import glob

#from moviepy.editor import *

def download_video():
   
    video_url = url_entry.get()
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        video.download('Downloads/')
        status_label.configure(text="Video downloaded successfully!")
    except pytube.exceptions.PytubeError as e:
        status_label.configure(text="Error: " + str(e))

def convert_to_mp3():
    video_file = file_entry.get()
    try:
        yt = YouTube(video_file)
        video =  yt.streams.filter(only_audio=True).first()
        download_file = video.download("Downloads/")
        base, ext = os.path.splitext(download_file)
        new_file = base + '.mp3'
        os.rename(download_file, new_file)
        status_label.configure(text="Conversion to MP3 completed!")
    except OSError as e:
        status_label.configure(text="Error: " + str(e))
       

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("1920x800")
root.title('Youtube downloader and mp3 converter')

img1=ImageTk.PhotoImage(Image.open("1.jpg"))
l1=customtkinter.CTkLabel(master=root, image=img1)
l1.pack()

frame=customtkinter.CTkFrame(master=l1, width=600, height=400, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Youtube downloader & mp3 converter", font=('Century Gothic', 25))
l2.place(x=110,y=80)

url_entry=customtkinter.CTkEntry(master=frame, width=300, placeholder_text="Enter Youtube URL for download")
url_entry.place(x=150, y=110)

button1=customtkinter.CTkButton(master=frame, width=300, text='Download', corner_radius=6, command=download_video)
button1.place(x=150,y=150)

file_entry=customtkinter.CTkEntry(master=frame, width=300, placeholder_text="Enter Youtube URL for converting")
file_entry.place(x=150, y=210)

button1=customtkinter.CTkButton(master=frame, width=300, text='Convert', corner_radius=6, command=convert_to_mp3)
button1.place(x=150,y=250)

status_label = customtkinter.CTkLabel(root, text="")
status_label.place(x=680,y=500)

root.mainloop()