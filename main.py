from tkinter import *
import webbrowser, os


def openNews():
    webbrowser.open('https://vk.com/drift_gta/update?act=s&id=18366511')


def openVk():
    webbrowser.open('https://vk.com/drift_gta')


def downloadGtaSa():
    webbrowser.open('https://gta-max.com/758-skachat_gta_san_andreas_original.html')


def downloadSAMP():
    webbrowser.open('https://gta-max.com/576-skachat_sa_mp_0_3_7_samp.html')


window = Tk()
window.title('"GTA SAMP • РУССКИЙ ДРИФТ СЕРВЕР • RDS •" - Launcher 32bit')
window.resizable(width=False, height=False)
window.geometry('640x375')
window.iconbitmap('data\\icon.ico')

photo = PhotoImage(file="data\\fon.png")
one = Label(window, image=photo)
one.image = photo  # just keeping a reference
one.grid()

butNews = Button(window, text='''Смотреть новости
проекта SAMP''')
butNews.config(width=22, height=2, bg='gainsboro', fg='black', command=openNews)
butNews.place(x=470, y=80)

butVk = Button(window, text='''Страница сервера
GTA SAMP 0.3.7''')
butVk.config(width=22, height=2, bg='gainsboro', fg='black', command=openVk)
butVk.place(x=470, y=122)

butDownloadGtaSa = Button(window, text='''Загрузить чистую
версию GTA SA''')
butDownloadGtaSa.config(width=22, height=2, bg='gainsboro', fg='black', command=downloadGtaSa)
butDownloadGtaSa.place(x=470, y=164)

butDownloadSAMP = Button(window, text='''Загрузить клиент
SAMP 0.3.7''')
butDownloadSAMP.config(width=22, height=2, bg='gainsboro', fg='black', command=downloadSAMP)
butDownloadSAMP.place(x=470, y=206)

window.mainloop()