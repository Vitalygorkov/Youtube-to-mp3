# from tkinter import *
#
# root = Tk()
# Label(text="Имя:").grid(row=0, column=0)
# Entry(width=80).grid(row=0, column=1, columnspan=3)
#
#
# def getmp3(link):
#     print(link)
#
# Button(text="Вставить").grid(row=2, column=2)
# # Button(text="Отменить").grid(row=2, column=3)
#
# root.mainloop()
from pytube import YouTube
from moviepy.editor import *
from tkinter import *  # Импортируем модуль

root = Tk()  # Создаем главное окно программы
root.title('Мой первый графический интерфейс')  # Устанавливаем заголовок
root.wm_attributes("-topmost", 1)  # Делаем отображение окна поверх всех остальных
root.geometry('350x150')  # устанавливем размер окна

# n = 0
# def click(event):  # функция вызываемая при нажатии на кнопку
#     global n
#     n += 1
#     print('Вы нажали на кнопку', n, 'раз')

def getmp3(event):
    print(E1.get())
    L2 = Label(root, text=E1.get())
    L2.pack(side=BOTTOM)
    yt = YouTube(E1.get())
    # print(yt.streams.filter(only_audio=True).first())
    print(yt.title.replace('.', '').replace('|', ''))
    # print(yt.keywords)
    yt.streams.filter(only_audio=True).first().download()
    L3 = Label(root, text='Скачивание, подождите')
    L3.pack(side=BOTTOM)
    video = AudioFileClip(yt.title.replace('.', '').replace('|', '') + '.mp4')
    video.write_audiofile(yt.title.replace('.', '').replace('|', '') + '.mp3')
    L4 = Label(root, text='Готово')
    L4.pack(side=BOTTOM)

# text_url = Entry(width=80,
# bad side "last": must be top, bottom, left, or right
L1 = Label(root, text="Url")
L1.pack( side = TOP)
E1 = Entry(root, bd =1)
E1.pack(side = TOP)

but_1 = Button(text='Скачать',  # Создаем кнопку и присваиваем ее в переменную
               width=5, height=1,  # Устанавливаем размер кнопки
               bg='white', fg='green',  # цвет фона и надписи
               activebackground='#77DDE7',  # цвет нажатой кнопки
               activeforeground='#FF2400',  # цвет надписи когда кнопка нажата
               font='Hack 16')  # устанавливаем шрифт и размер надписи
# but_1.bind('<Button-1>', click)  # Обработчик событий
but_1.bind('<Button-1>', getmp3)  # Обработчик событий

but_1.pack(side = TOP)  # используем метод pack для отображения кнопки
root.mainloop()  # запускаем главный цикл обработки событий