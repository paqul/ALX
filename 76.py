from tkinter import *

lista_wylotow = ["Warszawa", "Łódź", "Gdańsk"]
lista_przylotow = ["Kraków", "Szczecin", "Poznań"]


def pobierz_dane():
    zbior_checkboxow = []
    imiedisplayx["text"] = imie.get()
    nazwiskodisplayx["text"] = nazwisko.get()
    wylotdisplayx["text"] = wylot_lista.get("active")
    przylotdisplayx["text"] = przylot_lista.get("active")
    miejsceVIPdisplayx["text"] = str(wybory.get())
    zbiorposilkow = [checkvar1.get(), checkvar2.get(), checkvar3.get()]
    for x in zbiorposilkow:
        if x.isdigit() == False:
            zbior_checkboxow.append(x)
    zbior_checkboxow_ostatni = ", ".join(map(str, zbior_checkboxow))
    if len(zbior_checkboxow_ostatni) <= 3:
        daniadisplayx["text"] = "Brak zamówionych dań"
    else:
        daniadisplayx["text"] = zbior_checkboxow_ostatni
    zmiennatext = dodatkoweuwagi.get(1.0, END)
    textdisplay["text"] = zmiennatext


root = Tk()
root.title("Bilet Lotniczy")

frame0 = Frame(root).grid(row=0, column=0, sticky=W)
frame02 = Frame(root).grid(row=0, column=5, sticky=W)
frame1 = Frame(root)
frame2 = Frame(root)

emptylbl = Label(frame0, text="", height=40, width=5).grid(row=0, column=0, rowspan=11)

opcjepodrozy = Label(frame1, text="Opcje podróży:", font="Arial 20 bold")
opcjepodrozy.grid(row=0, column=1, columnspan=4)

imie_label = Label(frame1, text="Imie:").grid(row=1, column=1, columnspan=1, sticky=E)
imie = Entry(frame1,  text="Imię:", width=25)
imie.grid(row=1, column=2, columnspan=1)

nazwisko_label = Label(frame1, text="Nazwisko:").grid(row=1, column=3, sticky=W, columnspan=1)
nazwisko = Entry(frame1, width=25)
nazwisko.grid(row=1, column=4, columnspan=1)

wylot_text = Label(frame1, text="Wylot z:", font="Arial", anchor=W).grid(row=2, column=1, columnspan=2)
przylot_text = Label(frame1, text="Przylot do:", font="Arial", anchor=W).grid(row=2, column=3, columnspan=2)

wylot_lista = Listbox(frame1, height=10, width=35, selectmode=BROWSE, exportselection=False)
for w in lista_wylotow:
    wylot_lista.insert(0, w)
wylot_lista.grid(row=3, column=1, sticky=W, columnspan=2)

przylot_lista = Listbox(frame1, height=10, width=35, selectmode=BROWSE, exportselection=False)
for p in lista_przylotow:
    przylot_lista.insert(0, p)
przylot_lista.grid(row=3, column=3, sticky=W, columnspan=2)

vip = Label(frame1, text="Miejsce VIP:", anchor=W).grid(row=4, column=1, columnspan=4, sticky=W)
wybory = StringVar()
wybor1 = Radiobutton(frame1, text="TAK", variable=wybory, value="TAK")
wybor1.deselect()
wybor1.grid(row=5, column=1, columnspan=2, sticky=W)

wybor2 = Radiobutton(frame1, text="NIE", variable=wybory, value="NIE")
wybor2.select()
wybor2.grid(row=5, column=2, columnspan=2, sticky=W)

dodatkowyposilek = Label(frame1, text="Dodatkowy Posiłek:", anchor=W).grid(row=6, column=1, columnspan=4, sticky=W)
checkvar1 = StringVar()
checkvar2 = StringVar()
checkvar3 = StringVar()

checkbox1 = Checkbutton(frame1, text="Danie gorące", variable=checkvar1, onvalue="Danie gorące", offvalue=0)
checkbox1.deselect()
checkbox1.grid(row=7, column=1, columnspan=4, sticky=W)

checkbox2 = Checkbutton(frame1, text="Przekąska", variable=checkvar2, onvalue="Przekąska", offvalue=0)
checkbox2.deselect()
checkbox2.grid(row=7, column=2, columnspan=2)

checkbox3 = Checkbutton(frame1, text="Zimny deser", variable=checkvar3, onvalue="Zimny deser", offvalue=0)
checkbox3.deselect()
checkbox3.grid(row=7, column=3, columnspan=4, sticky=W)

dodatkoweuwagi_tekst = Label(frame1, text="Dodatkowe uwagi:", anchor=W).grid(row=8, column=1, columnspan=4, sticky=W)
dodatkoweuwagi = Text(frame1, height=6, width=47, font=5)
dodatkoweuwagi.grid(row=9, column=1, columnspan=4, sticky=W)

pobierzdane = Button(frame1, text="Dokonaj rezerwacji", command=pobierz_dane)
pobierzdane.grid(row=10, column=1, columnspan=4, sticky=W)

frame1.grid(row=0, column=1, sticky=W)

emptylbl2 = Label(frame1, text="", height=40, width=5).grid(row=0, column=5, rowspan=15)

szczegolyinformacji = Label(frame2, text="Szczegóły rezerwacji:", font=("Arial 20 bold"), height=-1).grid(row=0, column=5, columnspan=2)

imiedisplay = Label(frame2, text="Imie:").grid(row=1, column=5, sticky=W)
imiedisplayx = Label(frame2, text="")
imiedisplayx.grid(row=1, column=6, sticky=W)

nazwiskodisplay = Label(frame2, text="Nazwisko:").grid(row=2, column=5, sticky=W)
nazwiskodisplayx = Label(frame2, text="")
nazwiskodisplayx.grid(row=2, column=6, sticky=W)

wylotdisplay = Label(frame2, text="Wylot:").grid(row=3, column=5, sticky=W)
wylotdisplayx = Label(frame2, text="")
wylotdisplayx.grid(row=3, column=6, sticky=W)

przylotdisplay = Label(frame2, text="Przylot:").grid(row=4, column=5, sticky=W)
przylotdisplayx = Label(frame2, text="")
przylotdisplayx.grid(row=4, column=6, sticky=W)

miejsceVIPdisplay = Label(frame2, text="Miejsce VIP:").grid(row=5, column=5, sticky=W)
miejsceVIPdisplayx = Label(frame2, text="")
miejsceVIPdisplayx.grid(row=5, column=6, sticky=W)

daniadisplay = Label(frame2, text="Dania:").grid(row=6, column=5, sticky=W)
daniadisplayx = Label(frame2, text="", width=30, anchor=W)
daniadisplayx.grid(row=6, column=6, sticky=W)

Uwagidisplay = Label(frame2, text="Uwagi:").grid(row=7, column=5, sticky=W)
textdisplay = Label(frame2, text="")
textdisplay.grid(row=8, column=5, sticky=W, columnspan=2)

frame2.grid(row=0, column=2, sticky=N, rowspan=1)

emptylbl3 = Label(frame2, text="", height=40, width=5).grid(row=0, column=8, rowspan=25)

root.mainloop()