
from tkinter import *


f = open('rezults.txt')
n = float(f.readline())
z = float(f.readline())
count = float(f.readline())
auto = float(f.readline())
f.close()

tk = Tk()
tk.title('Clicker')
tk.geometry("1500x800")


def nplus():
    global n
    n = round((n + z), 3)
    label1['text'] = str(n) + '$'


def nsbros():
    global n
    global z
    global count
    n = 0
    z = 0.1
    count = 0.4
    label1['text'] = str(n) + '$'
    label2['text'] = 'За клик: ' + str(round(z, 3)) + '$'
    label3['text'] = 'Стоимость улучшения: ' + str(round(count, 3)) + '$'
    label6['text'] = 'Автоклик: ' + str(round(auto, 3)) + '$'


def dopclick():
    global n
    global z
    global count
    if n >= count:
        n = round((n - count), 3)
        z = z + z/4
        count = z * 4
    label1['text'] = str(n) + '$'
    label2['text'] = 'За клик: ' + str(round(z, 3)) + '$'
    label3['text'] = 'Стоимость улучшения: ' + str(round(count, 3)) + '$'
    label6['text'] = 'Автоклик: ' + str(round(auto, 3)) + '$'


def autocliker():
    global n
    global z
    global count
    while __name__ == "__main__":
        
    label1['text'] = str(n) + '$'
    label2['text'] = 'За клик: ' + str(round(z, 3)) + '$'
    label3['text'] = 'Стоимость улучшения: ' + str(round(count, 3)) + '$'
    label6['text'] = 'Автоклик: ' + str(round(auto, 3)) + '$'


autocliker()
label1 = Label(tk, text=str(round(n, 3))+'$', font=('Helvetica 100'))
label1.pack()

label2 = Label(tk, text='За клик: '+str(round(z, 3))+'$', font=('Helvetica 30'))
label2.pack()
label3 = Label(tk, text='Стоимость улучшения: '+str(round(count, 3))+'$', font=('Helvetica 30'))
label3.pack()

btn1 = Button(text="Клик", background="#000", foreground="#fff",
              padx="60", pady="30", font="Helvetica 50", command=nplus)

btn1.pack()
label4 = Label(tk, text='', font=('Helvetica 30'))
label4.pack()
btn3 = Button(text="Улучшение", background="#000", foreground="#fff",
              padx="60", pady="10", font="Helvetica 25", command=dopclick)
btn3.pack()
label5 = Label(tk, text='', font=('Helvetica 30'))
label5.pack()
btn2 = Button(text="Сброс", background="#000", foreground="#fff",
              padx="20", pady="8", font="16", command=nsbros)
btn2.pack()

label6 = Label(tk, text='', font=('Helvetica 30'))
label6.pack()

mainloop()
f = open('rezults.txt', "w")
f.write(str(n) + '\n')
f.write(str(z) + '\n')
f.write(str(count) + '\n')
f.close()
