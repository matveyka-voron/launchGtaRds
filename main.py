from tkinter import *
import webbrowser, os


def openNews():
    webbrowser.open('https://vk.com/drift_gta/update?act=s&id=18366511')


def openVk():
    webbrowser.open('https://vk.com/drift_gta')


window = Tk()
window.title('"GTA SAMP • РУССКИЙ ДРИФТ СЕРВЕР • RDS •" - Launcher 32bit')
window.resizable(width=False, height=False)
window.geometry('640x375')
window.iconbitmap('data\\icon.ico')

photo = PhotoImage(file="data\\fon.png")
one = Label(window, image=photo)
one.image = photo  # just keeping a reference
one.grid()

butNews = Button(window, text='Смотреть новости проекта')
butNews.config(width=22, height=2, bg='gainsboro', fg='black', command=openNews)
butNews.place(x=470, y=80)

butVk = Button(window, text='''Страница сервера
GTA SAMP 0.3.7''')
butVk.config(width=22, height=2, bg='gainsboro', fg='black', command=openVk)
butVk.place(x=470, y=122)

window.mainloop()