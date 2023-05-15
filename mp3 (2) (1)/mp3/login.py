import tkinter
import customtkinter 
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("600x440")
app.title('Login')

def button_function():
    app.destroy()
    w=customtkinter.CTk()
    w.geometry('1280x720')
    w.title('Welcome')
    l1=customtkinter.CTkLabel(master=w, text="Home Page", font=('Century Gothic', 60))
    l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    w.mainloop()


img1=ImageTk.PhotoImage(Image.open("1.jpg"))
l1=customtkinter.CTkLabel(master=app, image=img1)
l1.pack()


frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
l2.place(x=50,y=45)

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
entry1.place(x=50, y=110)

entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password")
entry2.place(x=50, y=165)

l2=customtkinter.CTkLabel(master=frame, text="Forget password", font=('Century Gothic', 12))
l2.place(x=165,y=195)

button1=customtkinter.CTkButton(master=frame, width=220, text='Login', corner_radius=6, command=button_function)
button1.place(x=50,y=240)

img2=customtkinter.CTkImage(Image.open("3.jpg").resize((20,20),Image.ANTIALIAS))
img3=customtkinter.CTkImage(Image.open("2.jpg").resize((20,20),Image.ANTIALIAS))

button2=customtkinter.CTkButton(master=frame, image=img2, text="Google", width=100, height=20, corner_radius=6, compound="left", text_color='black', fg_color='white', hover_color="#A4A4A4")
button2.place(x=50,y=290)

button3=customtkinter.CTkButton(master=frame, image=img3, text="Facebook", width=100, height=20, corner_radius=6, compound="left", text_color='black', fg_color='white', hover_color="#A4A4A4")
button3.place(x=170,y=290)

app.mainloop()