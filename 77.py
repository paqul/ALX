from tkinter import *

#---------------klasy------------------
class Listy():
    def __init__(self):
        self.pomocnicza_lista = []
        self.wartosc = []
        self.znaki = []
        self.liczba = []


# --------------funkcje----------------
def fun_zero():
    lista1.pomocnicza_lista.append(0)
    var.set(lista1.pomocnicza_lista)

def fun_jeden():
    lista1.pomocnicza_lista.append(1)
    var.set(lista1.pomocnicza_lista)

def fun_dwa():
    lista1.pomocnicza_lista.append(2)
    var.set(lista1.pomocnicza_lista)

def fun_trzy():
    lista1.pomocnicza_lista.append(3)
    var.set(lista1.pomocnicza_lista)

def fun_cztery():
    lista1.pomocnicza_lista.append(4)
    var.set(lista1.pomocnicza_lista)

def fun_piec():
    lista1.pomocnicza_lista.append(5)
    var.set(lista1.pomocnicza_lista)

def fun_szesc():
    lista1.pomocnicza_lista.append(6)
    var.set(lista1.pomocnicza_lista)

def fun_siedem():
    lista1.pomocnicza_lista.append(7)
    var.set(lista1.pomocnicza_lista)

def fun_osiem():
    lista1.pomocnicza_lista.append(8)
    var.set(lista1.pomocnicza_lista)

def fun_dziewiec():
    lista1.pomocnicza_lista.append(9)
    var.set(lista1.pomocnicza_lista)

def fun_mnoz():
    lista1.pomocnicza_lista.append("*")
    var.set(lista1.pomocnicza_lista)

def fun_odejmij():
    lista1.pomocnicza_lista.append("-")
    var.set(lista1.pomocnicza_lista)

def fun_dodaj():
    lista1.pomocnicza_lista.append("+")
    var.set(lista1.pomocnicza_lista)

def dzialanie(a, b, znak):
    if znak == "+":
        wynik = a+b
    elif znak == "-":
        wynik = a-b
    elif znak == "*":
        wynik = a*b
    return wynik

def fun_reset():
    lista1.pomocnicza_lista.clear()
    lista1.wartosc.clear()
    lista1.znaki.clear()
    lista1.liczba.clear()
    var.set(lista1.pomocnicza_lista)
    var2.set(lista1.pomocnicza_lista)

def wykonaj():
    # print(lista1.pomocnicza_lista, len(lista1.pomocnicza_lista))
    for lp, x in enumerate(lista1.pomocnicza_lista):
        lista1.wartosc.append(x)
        if x == "+" or x == "-" or x == "*" or lp+1 == len(lista1.pomocnicza_lista):
            if x == "+" or x == "-" or x == "*":
                lista1.znaki.append(x)
                lista1.wartosc.pop(lp)
                length = len(lista1.wartosc)
                liczba_tmp = "".join(map(str, lista1.wartosc))
                lista1.liczba.append(liczba_tmp)
            else:
                liczba_tmp2 = "".join(map(str, lista1.wartosc[length:len(lista1.wartosc)]))
                lista1.liczba.append(liczba_tmp2)
    if lista1.znaki[0] == "+":
        wynik = int(lista1.liczba[0])+int(lista1.liczba[1])
    elif lista1.znaki[0] == "-":
        wynik = int(lista1.liczba[0])-int(lista1.liczba[1])
    elif lista1.znaki[0] == "*":
        wynik = int(lista1.liczba[0])*int(lista1.liczba[1])
    var2.set(wynik)

def wyjscie():
    exit()

#--------------GUI------------------

root = Tk()
lista1 = Listy()
root.resizable(width=False, height=False)

objektmenu = Menu(root)
dodatkowazmiennamenu = Menu(objektmenu, tearoff=0)
dodatkowazmiennamenu.add_command(label="Exit", command=wyjscie)
objektmenu.add_cascade(label="Exit", menu=dodatkowazmiennamenu)
root.config(menu=objektmenu)

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)
frame3.grid(row=2, column=0)


var = StringVar()
var2 = StringVar()
dzialanie = Label(frame1, textvariable=var, bg="grey", height=2, width=50, anchor=E)
dzialanie.grid()

wynik = Label(frame2, textvariable=var2, bg="white", font=4, height=2, width=39, anchor=E)
wynik.grid()

odstep0 = Label(frame3)
odstep0.grid(row=0, column=0)

siedem = Button(frame3, text="7", width=5, height=3, command=fun_siedem)
siedem.grid(row=1, column=0)
osiem = Button(frame3, text="8", width=5, height=3, command=fun_osiem)
osiem.grid(row=1, column=1)
dziewiec = Button(frame3, text="9", width=5, height=3, command=fun_dziewiec)
dziewiec.grid(row=1, column=2)
razy = Button(frame3, text="*", width=5, height=3, command=fun_mnoz)
razy.grid(row=1, column=3)

odstep1 = Label(frame3)
odstep1.grid(row=2,column=0)

cztery = Button(frame3, text="4", width=5, height=3, command=fun_cztery)
cztery.grid(row=3, column=0)
piec = Button(frame3, text="5", width=5, height=3, command=fun_piec)
piec.grid(row=3, column=1)
szesc = Button(frame3, text="6", width=5, height=3, command=fun_szesc)
szesc.grid(row=3, column=2)
minus = Button(frame3, text="-", width=5, height=3, command=fun_odejmij)
minus.grid(row=3, column=3)

odstep2 = Label(frame3)
odstep2.grid(row=4,column=0)

jeden = Button(frame3, text="1", width=5, height=3, command=fun_jeden)
jeden.grid(row=5, column=0)
dwa = Button(frame3, text="2", width=5, height=3, command=fun_dwa)
dwa.grid(row=5, column=1)
trzy = Button(frame3, text="3", width=5, height=3, command=fun_trzy)
trzy.grid(row=5, column=2)
plus = Button(frame3, text="+", width=5, height=3, command=fun_dodaj)
plus.grid(row=5, column=3)

odstep3 = Label(frame3)
odstep3.grid(row=6, column=0)

zero = Button(frame3, text="0", width=5, height=3, command=fun_zero)
zero.grid(row=7, column=0)
rownasie = Button(frame3, text="=", width=12, height=3, command=wykonaj)
rownasie.grid(row=7, column=1, columnspan=2)
reszta = Button(frame3, text="R", width=5, height=3, command=fun_reset)
reszta.grid(row=7, column=3)

odstep4 = Label(frame3)
odstep4.grid(row=8, column=0)

mainloop()