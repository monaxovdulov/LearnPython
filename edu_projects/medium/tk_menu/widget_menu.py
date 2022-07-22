from tkinter import *
import webbrowser

root = Tk()
root.geometry("400x400")


def callback():
    webbrowser.open_new(r"https://www.youtube.com/channel/UCmrpI-1BwmqnXJX_bShpApA")


def callback2():
    webbrowser.open_new(r"https://www.youtube.com/channel/UCYj855bxMDGP0-9L0kiFWTg")


def callback3():
    webbrowser.open_new(r"https://t.me/+zjD49vNNAZw5Mzli")


my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu)

my_menu.add_cascade(label='Обо мне', menu=file_menu)
file_menu.add_command(label="Ютуб канал1", command=callback)
# file_menu.add_separator()
file_menu.add_command(label='Ютуб канал2', command=callback2)
file_menu.add_command(label='тг', command=callback3)

root.mainloop()
