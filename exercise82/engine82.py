class Kursanci():
    def __init__(self):
        self.kursanci = []

    def dodaj_kursanta(self):
        self.imie = input("Podaj imie kursanta: ")
        self.nazwisko = input("Podaj nazwisko kursanta: ")
        self.kursant = ("%s %s" % (self.imie, self.nazwisko))
        self.kursanci.append(self.kursant)
        print("Dodano kursanta")
        self.lista_kursantow()


    def lista_kursantow(self):
        if len(self.kursanci) != 0:
            for self.lp, self.kursant in enumerate(self.kursanci):
                self.lista = (self.lp, str(self.kursant))
                print(self.lp, str(self.kursant))
        else:
            print("Lista jest pusta")


    def zmien_kursanta(self):
        self.index = int(input("Podaj index do zmiany: "))
        self.imie = input("Podaj imie kursanta: ")
        self.nazwisko = input("Podaj nazwisko kursanta: ")
        self.kursant = ("%s %s" % (self.imie, self.nazwisko))
        self.kursanci.insert(self.index, self.kursant)
        self.kursanci.pop(self.index+1)
        print("Zmieniono dane kursanta")
        self.lista_kursantow()


    def usun_kursanta(self):
        self.lista_kursantow()
        self.index = int(input("Podaj index do usuniecia: "))
        self.kursanci.pop(self.index)
        print("Usunieto kursanta")
        self.lista_kursantow()


class Wykladowca(Kursanci):
    def __init__(self, wykladowca):
        super().__init__()
        self.wykladowca = wykladowca


class Kurs(Wykladowca):
    def __init__(self, nazwa, wykladowca):
        super().__init__(wykladowca)
        self.nazwa = nazwa
        print("Witaj na kursie: \"%s\", prowadzonym przez \"%s\"" % ( self.nazwa, self.wykladowca))
        self.menu()


    def menu(self):
        while True:
            decyzja = input("D - Dodaj kursanta, L - Lista kursantow, Z - Zmien kursanta, U - Usun kursanta, Q - wyjscie").upper()
            if decyzja == "D":
                self.dodaj_kursanta()
            elif decyzja == "L":
                self.lista_kursantow()
            elif decyzja == "Z":
                self.zmien_kursanta()
            elif decyzja == "U":
                self.usun_kursanta()
            elif decyzja == "Q":
                print("Wykladowca \"%s\" dziekuje za wspolprace przy zarzadzaniu kursem: \"%s\" " % (self.wykladowca, self.nazwa))
                exit()
            else:
                print("Wpisz: D lub L lub Z lub U lub Q")
