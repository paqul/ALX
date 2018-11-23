#----------------zmienne poczatkowe--------------------#


pamiec_podreczna= []


#------------------klasy-------------------------------#


class Student():

    def __init__(self):
        self.imie = input("Imie studenta: ")
        self.nazwisko = input("Nazwisko studenta: ")
        self.nr_indeksu = self.walidacja_nr_ideksu()
        self.grupa = self.walidacja_grupy()


    def walidacja_nr_ideksu(self):
        while True:
            self.nr_indeksu = (input("Podaj numer indeksu: "))
            if self.nr_indeksu.isdigit() == True:
                return self.nr_indeksu
            else:
                print("Wprowadzono NIEcyfry - jeszcze raz")


    def walidacja_grupy(self):
        while True:
            self.grupa = (input("Numer grupy studenta: "))
            if self.grupa.isdigit() == True:
                return self.grupa
            else:
                print("Wprowadzono NIEcyfry - jeszcze raz")

    def modyfikuj(self):
        self.imie = input("Imie studenta: ")
        self.nazwisko = input("Nazwisko studenta: ")
        self.nr_indeksu = self.walidacja_nr_ideksu()
        self.grupa = self.walidacja_grupy()


    def dane(self):
        dane = "%10s| %10s| %15s| %4s\n" % (self.nr_indeksu, self.imie, self.nazwisko, self.grupa)
        return dane


    def __str__(self):
        return ("%s, %s, %s, %s" % (self.nr_indeksu, self.imie, self.nazwisko, self.grupa))


#------------------funkcje-----------------------------#


def dodaj():
    student = Student()
    pamiec_podreczna.append(student.dane())
    try:
        pamiec_pliku = open("plik.txt", "a")
    except IOError:
        pamiec_pliku = open("plik.txt", "w")
    finally:
        for line in pamiec_podreczna:
            pamiec_pliku.write(line)
            print("Dopisano studenta do Bazy Danych (plik.txt)")
        pamiec_pliku.close()
    pamiec_podreczna.remove(student.dane())
    del student


def usun():
    tresc = open("plik.txt", "r")
    wszystkie_dane = tresc.readlines()
    tresc.close()
    print("Dostepne nazwiska do usuniecia:")
    for LP, string in enumerate(wszystkie_dane):
        print(len(wszystkie_dane[LP][23:39]),wszystkie_dane[LP][23:39])
    chars = input("Podaj nazwisko ktore ma zostac usuniete z listy: ")
    chars = ("%16s" % chars)
    usunieto = False
    for lp, string in enumerate(wszystkie_dane):
        if chars == wszystkie_dane[lp][23:39]:
            wszystkie_dane.pop(lp)
            tresc = open("plik.txt", "w")
            tresc.writelines(wszystkie_dane)
            tresc.close()
            print("Usunieto wskazane nazwisko")
            usunieto = True
    if LP == lp and usunieto != True:
        print("Podane nazwisko nie istnieje w bazie")


def pokaz():
    print("Nr indeksu|    Imie:  |    Nazwisko:   | Grupa:")
    pamiec_podreczna = open("plik.txt", "r")
    for tmp in pamiec_podreczna:
        print(tmp, end="")
    pamiec_podreczna.close()


def szukaj():
    tresc = open("plik.txt", "r")
    wszystkie_dane = tresc.readlines()
    tresc.close()
    chars = input("Podaj ciag znakow dotyczacy szukanego studenta: ")
    for lp, string in enumerate(wszystkie_dane):
        if chars in string:
            print(string, end="")


def zmien():
    tresc = open("plik.txt", "r")
    wszystkie_dane = tresc.readlines()
    tresc.close()
    print("Dostepni użytkownicy edycji:")
    print("      Imie:        Nazwisko:")
    for LP, string in enumerate(wszystkie_dane):
        print(wszystkie_dane[LP][11:22], wszystkie_dane[LP][23:39])
    wybrane = input("Podaj nazwisko ktore ma zostac edytowane: ")
    wybrane = ("%16s" % wybrane)
    mod = False
    for lp, tmp in enumerate(wszystkie_dane):
        if wybrane == wszystkie_dane[lp][23:39]:
            wszystkie_dane.pop(lp)
            student = Student()
            wszystkie_dane.append(student.dane())
            mod = True
            print("Zmodyfikowano status studenta")
    if LP == lp and mod != True:
        print("Podane nazwisko nie istnieje w bazie")
    pamiec_pliku = open("plik.txt", "w")
    for line in wszystkie_dane:
        pamiec_pliku.write(line)
    pamiec_pliku.close()
    print("Nr indeksu|    Imie:  |    Nazwisko:   | Grupa:")
    for tmp in wszystkie_dane:
        print(tmp, end="")


def main():
    while True:
        decyzja = input("D-dodaj, U-usuń, P-pokaz, S-szukaj, Z - zmień, Q-wyjscie").upper()
        if decyzja == "D": #OK
            dodaj()
        elif decyzja == "U": #OK
            usun()
        elif decyzja == "P":  #OK
            pokaz()
        elif decyzja == "S": #OK
            szukaj()
        elif decyzja == "Z": #OK
            zmien()
        elif decyzja == "Q": #OK
            exit()


main()
