import tkinter as tk 
def red(button):
    button.config(bg="#ff9595")

def green(button):
    button.config(bg="#c1ff95")    

win=tk.Tk()

win.title("qwiz")
win.geometry("600x800")
win.config(bg="#ffffff")
text=tk.Label(win, text="Квиз", bg="#ffffff", fg="#000754", font=("Impact", 25))
text.pack()

name=tk.Label(win, text="Имя Фамилия", bg="#ffffff", fg="#f28100", font=("Impact", 12))
pen=tk.Entry(win, width=45)

name.place(x=20, y=60)
pen.place(x=20, y=90)
#вопрос один
text1=tk.Label(win, text="1.Что добавляют в щи по старым русским рецептам?", bg="#ffffff")
qwe1=tk.Button(win, text="Сметана")
qwe2=tk.Button(win, text="Простокваша")
qwe3=tk.Button(win, text="Творог")
qwe4=tk.Button(win, text="Кефир")

qwe1.config(width=11, command=lambda: red(qwe1))
qwe2.config(command=lambda: green(qwe2))
qwe3.config(width=11, command=lambda: red(qwe3))
qwe4.config(width=11, command=lambda: red(qwe4))

text1.place(x=20, y=130)
qwe1.place(x=20, y=160)
qwe2.place(x=20, y=190)
qwe3.place(x=150, y=160)
qwe4.place(x=150, y=190)
#вопрос два
text2=tk.Label(win, text="2.Назовите страну с самой высокой продолжительностью жизни?", bg="#ffffff")

var1=tk.Button(win, text="Китай")
var2=tk.Button(win, text="Россия")
var3=tk.Button(win, text="Италия")
var4=tk.Button(win, text="Франция")

var1.config(width=11, command=lambda: green(var1))
var2.config(width=11, command=lambda: red(var2))
var3.config(width=11, command=lambda: red(var3))
var4.config(width=11, command=lambda: red(var4))

text2.place(x=20, y=230)
var1.place(x=20, y=260)
var2.place(x=20, y=290)
var3.place(x=150, y=260)
var4.place(x=150, y=290)
#Вопрос три
text3=tk.Label(win, text="3.Какой фрукт является объектом раздора?", bg="#ffffff")

fru1=tk.Button(win, text="Апельсин")
fru2=tk.Button(win, text="Киви")
fru3=tk.Button(win, text="Груша")
fru4=tk.Button(win, text="Яблоко")

fru1.config(width=11, command=lambda: red(fru1))
fru2.config(width=11, command=lambda: red(fru2))
fru3.config(width=11, command=lambda: red(fru3))
fru4.config(width=11, command=lambda: green(fru4))

text3.place(x=20, y=330)
fru1.place(x=20, y=360)
fru2.place(x=20, y=390)
fru3.place(x=150, y=360)
fru4.place(x=150, y=390)

#Вопрос четыре
text4=tk.Label(win, text="4.Эта фигура на шахматной доске делает только диагональный ход. Какая?", bg="#ffffff")

sln1=tk.Button(win, text="Слон")
sln2=tk.Button(win, text="Ладья")
sln3=tk.Button(win, text="Конь")
sln4=tk.Button(win, text="Пешка")

sln1.config(width=11, command=lambda: green(sln1))
sln2.config(width=11, command=lambda: red(sln2))
sln3.config(width=11, command=lambda: red(sln3))
sln4.config(width=11, command=lambda: red(sln4))

text4.place(x=20, y=430)
sln1.place(x=20, y=460)
sln2.place(x=20, y=490)
sln3.place(x=150, y=460)
sln4.place(x=150, y=490)

#Вопрос пять
text5=tk.Label(win, text="5.В грамматике какой страны все существительные должны писаться с большой буквы?", bg="#ffffff")

ger1=tk.Button(win, text="Россия")
ger2=tk.Button(win, text="Казахстан")
ger3=tk.Button(win, text="Англия")
ger4=tk.Button(win, text="Германия")

ger1.config(width=11, command=lambda: red(ger1))
ger2.config(width=11, command=lambda: red(ger2))
ger3.config(width=11, command=lambda: red(ger3))
ger4.config(width=11, command=lambda: green(ger4))

text5.place(x=20, y=530)
ger1.place(x=20, y=560)
ger2.place(x=20, y=590)
ger3.place(x=150, y=560)
ger4.place(x=150, y=590)


win.mainloop()
