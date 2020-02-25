from tkinter import *
import webbrowser, os


window = Tk()
window.title('"GTA SAMP • РУССКИЙ ДРИФТ СЕРВЕР • RDS •" - Launcher 32bit')
window.resizable(width=False, height=False)
window.geometry('640x375')
window.iconbitmap('data\\icon.ico')

photo = PhotoImage(file="data\\fon.png")
one = Label(window, image=photo)
one.image = photo  # just keeping a reference
one.grid()



window.mainloop()