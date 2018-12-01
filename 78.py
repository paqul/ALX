from tkinter import *

#-------------------Engine---------------------------
class PotrzebnyObjekt():
       def __init__(self):
              self.counter = 0

haslo = "python"
pokazhaslo = []

for i in range(0,len(haslo)):
    pokazhaslo.append("-")

listapomocnicza = []

def pomocnicza():
       buttonA.configure(state=DISABLED)
       buttonB.configure(state=DISABLED)
       buttonC.configure(state=DISABLED)
       buttonD.configure(state=DISABLED)
       buttonE.configure(state=DISABLED)
       buttonF.configure(state=DISABLED)
       buttonG.configure(state=DISABLED)
       buttonH.configure(state=DISABLED)
       buttonI.configure(state=DISABLED)
       buttonJ.configure(state=DISABLED)
       buttonK.configure(state=DISABLED)
       buttonL.configure(state=DISABLED)
       buttonM.configure(state=DISABLED)
       buttonN.configure(state=DISABLED)
       buttonO.configure(state=DISABLED)
       buttonP.configure(state=DISABLED)
       buttonR.configure(state=DISABLED)
       buttonS.configure(state=DISABLED)
       buttonT.configure(state=DISABLED)
       buttonU.configure(state=DISABLED)
       buttonW.configure(state=DISABLED)
       buttonX.configure(state=DISABLED)
       buttonY.configure(state=DISABLED)
       buttonZ.configure(state=DISABLED)
       wprowadzhaslo.configure(state=DISABLED)
       buttonSprawdz.configure(state=DISABLED)


def sprawdz():
       if wprowadzhaslo.get().lower() == haslo:
              pomocnicza()
              haslodisplay.configure(text=("WYGRAŁEŚ !!! Hasło: %s" % haslo), fg="green")
       else:
              try:
                     licznik.counter += 1
                     rysunek.configure(image=img[licznik.counter])
              except:
                     pomocnicza()
                     haslodisplay.configure(text="PRZEGRAŁEŚ!!! Hasło: %s" % haslo, fg="red")

def wprowadzanie_liter(litera):
    if litera not in haslo:
           try:
                  licznik.counter += 1
                  rysunek.configure(image=img[licznik.counter])
           except:
                  pomocnicza()
                  haslodisplay.configure(text="PRZEGRAŁEŚ!!! Hasło: %s" % haslo, fg="red")

    for x in range(0, len(haslo)):
        if haslo[x] == litera:
            pokazhaslo[x]=haslo[x]
            listapomocnicza.append(litera)
            haslodisplay.configure(text=pokazhaslo)
            # print(pokazhaslo)
            if (len(listapomocnicza) == len(haslo)):
                   pomocnicza()
                   haslodisplay.configure(text=("WYGRAŁEŚ !!! Hasło: %s" % haslo), fg="green")

def a():
       return wprowadzanie_liter("a")

def b():
       return wprowadzanie_liter("b")

def c():
       return wprowadzanie_liter("c")

def d():
       return wprowadzanie_liter("d")

def e():
       return wprowadzanie_liter("e")

def f():
       return wprowadzanie_liter("f")

def g():
       return wprowadzanie_liter("g")

def h():
       return wprowadzanie_liter("h")

def i():
       return wprowadzanie_liter("i")

def j():
       return wprowadzanie_liter("j")

def k():
       return wprowadzanie_liter("k")

def l():
       return wprowadzanie_liter("l")

def m():
       return wprowadzanie_liter("m")

def n():
       return wprowadzanie_liter("n")

def o():
       return wprowadzanie_liter("o")

def p():
       return wprowadzanie_liter("p")

def r():
       return wprowadzanie_liter("r")

def s():
       return wprowadzanie_liter("s")

def t():
       return wprowadzanie_liter("t")

def u():
       return wprowadzanie_liter("u")

def w():
       return wprowadzanie_liter("w")

def x():
       return wprowadzanie_liter("x")

def y():
       return wprowadzanie_liter("y")

def z():
       return wprowadzanie_liter("z")

#---------------------GUI----------------------------

licznik = PotrzebnyObjekt()
root = Tk()
img = [PhotoImage(file="wisielec_0.png"), PhotoImage(file="wisielec_1.png"), PhotoImage(file="wisielec_2.png"),
       PhotoImage(file="wisielec_3.png"), PhotoImage(file="wisielec_4.png"), PhotoImage(file="wisielec_5.png"),
       PhotoImage(file="wisielec_6.png")]


root.title("Gra Wisielec")
root.resizable(False, False)

frame1 = Frame(root, height=250, width=500)
frame2 = Frame(root, height=250, width=500)
frame3 = Frame(root, height=250, width=1000)

rysunek = Label(frame1, image=img[0], bg="grey", bd=20)
rysunek.grid(row=0, column=0)

buttonA = Button(frame2, text="A", height=4, width=10, command=a)
buttonA.grid(row=0, column=0)
buttonB = Button(frame2, text="B", height=4, width=10, command=b)
buttonB.grid(row=0, column=1)
buttonC = Button(frame2, text="C", height=4, width=10, command=c)
buttonC.grid(row=0, column=2)
buttonD = Button(frame2, text="D", height=4, width=10, command=d)
buttonD.grid(row=0, column=3)
buttonE = Button(frame2, text="E", height=4, width=10, command=e)
buttonE.grid(row=0, column=4)
buttonF = Button(frame2, text="F", height=4, width=10, command=f)
buttonF.grid(row=0, column=5)
emplabel1 = Label(frame2, text="", height=1, width=10).grid(row=1, column=0, columnspan=6)

buttonG = Button(frame2, text="G", height=4, width=10, command=g)
buttonG.grid(row=2, column=0)
buttonH = Button(frame2, text="H", height=4, width=10, command=h)
buttonH.grid(row=2, column=1)
buttonI = Button(frame2, text="I", height=4, width=10, command=i)
buttonI.grid(row=2, column=2)
buttonJ = Button(frame2, text="J", height=4, width=10, command=j)
buttonJ.grid(row=2, column=3)
buttonK = Button(frame2, text="K", height=4, width=10, command=k)
buttonK.grid(row=2, column=4)
buttonL = Button(frame2, text="L", height=4, width=10, command=l)
buttonL.grid(row=2, column=5)
emplabel2 = Label(frame2, text="", height=1, width=10).grid(row=3, column=0, columnspan=6)

buttonM = Button(frame2, text="M", height=4, width=10, command=m)
buttonM.grid(row=4, column=0)
buttonN = Button(frame2, text="N", height=4, width=10, command=n)
buttonN.grid(row=4, column=1)
buttonO = Button(frame2, text="O", height=4, width=10, command=o)
buttonO.grid(row=4, column=2)
buttonP = Button(frame2, text="P", height=4, width=10, command=p)
buttonP.grid(row=4, column=3)
buttonR = Button(frame2, text="R", height=4, width=10, command=r)
buttonR.grid(row=4, column=4)
buttonS = Button(frame2, text="S", height=4, width=10, command=s)
buttonS.grid(row=4, column=5)
emplabel3 = Label(frame2, text="", height=1, width=10).grid(row=5, column=0, columnspan=6)

buttonT = Button(frame2, text="T", height=4, width=10, command=t)
buttonT.grid(row=6, column=0)
buttonU = Button(frame2, text="U", height=4, width=10, command=u)
buttonU.grid(row=6, column=1)
buttonW = Button(frame2, text="W", height=4, width=10, command=w)
buttonW.grid(row=6, column=2)
buttonX = Button(frame2, text="X", height=4, width=10, command=x)
buttonX.grid(row=6, column=3)
buttonY = Button(frame2, text="Y", height=4, width=10, command=y)
buttonY.grid(row=6, column=4)
buttonZ = Button(frame2, text="Z", height=4, width=10, command=z)
buttonZ.grid(row=6, column=5)

haslodisplay = Label(frame3, text=pokazhaslo, font="Arial 20 bold", height=4, width=55)
haslodisplay.grid(row=0, column=0, columnspan=2)

emplabel4 = Label(frame3, text="Wprowadz hasło:", height=2).grid(row=1, column=0, sticky=E)

wprowadzhaslo = Entry(frame3)
wprowadzhaslo.grid(row=1, column=1, sticky=W)

emplabel5 = Label(frame3, text="", height=2).grid(row=2, column=0)

buttonSprawdz = Button(frame3, text="Sprawdz haslo", command=sprawdz)
buttonSprawdz.grid(row=3, column=0, columnspan=2)

emplabel6 = Label(frame3, text="", height=2).grid(row=4, column=0)

frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
frame3.grid(row=1, column=0, columnspan=2)

root.mainloop()