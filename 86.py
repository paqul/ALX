import pickle

class Firma():
    def __init__(self):
        self.firmy = []


    def dodaj_firme(self):
        self.nazwafirmy = input("Podaj nazwe firmy: ")
        self.firmy.append(self.nazwafirmy)
        print("Dodano firme")
        return self.firmy


    def usun_firme(self, relacja):
        counter_list=[]
        counter = -1
        tmp_firmy = []
        for sprawdzamrelacje in relacja:
            if sprawdzamrelacje[1] in self.firmy:
                tmp_firmy.append(sprawdzamrelacje[1])
        for firma in self.firmy:
            counter += 1
            if firma not in tmp_firmy:
                print(counter, firma)
                counter_list.append(counter)
        self.indeks = int(input("Podaj indeks firmy ktorą chcesz usunac"))
        if self.indeks in counter_list:
            self.firmy.pop(self.indeks)
            print("Usunieto firmę")
        else:
            print("Nie mozna usunac firmy o tym indeksie poniewaz ma przypisana relacje z pracownikami")


    def pokaz_firmy(self):
        for lp, firma in enumerate(self.firmy):
            print(firma)


class Pracownicy():
    def __init__(self):
        self.pracownicy = []


    def dodaj_pracownika(self):
        self.nazwapracownika = input("Podaj imie pracownika: ")
        self.pracownicy.append(self.nazwapracownika)
        print("Dodano pracownika")


    def usun_pracownika(self, relacja):
        counter_list=[]
        counter = -1
        tmp_pracownicy = []
        for sprawdzamrelacje in relacja:
            if sprawdzamrelacje[0] in self.pracownicy:
                tmp_pracownicy.append(sprawdzamrelacje[0])
        for pracownik in self.pracownicy:
            counter += 1
            if pracownik not in tmp_pracownicy:
                print(counter, pracownik)
                counter_list.append(counter)
        self.indeks = int(input("Podaj indeks pracownika ktorego chcesz usunac"))
        if self.indeks in counter_list:
            self.pracownicy.pop(self.indeks)
            print("Usunieto pracownika")
        else:
            print("Nie mozna usunac pracownika o tym indeksie poniewaz ma przypisana relacje z firmą")


    def pokaz_pracownikow(self):
        for lp, pracownik in enumerate(self.pracownicy):
            print(pracownik)


class Zatrudnienie():
    def __init__(self):
        self.relacja = []


    def przypisz_firme_do_pracownika(self, firmy, pracownicy):
        print(firmy)
        self.wyborfirmy = input("Podaj nazwe firmy: ")
        print(pracownicy)
        self.wyborpracownika = input("Podaj imie pracownika")
        if self.wyborfirmy in firmy and self.wyborpracownika in pracownicy:
            print("Przypisano pracownika: \"%s\" do firmy: \"%s\"" % (self.wyborpracownika, self.wyborfirmy))
            relacja = [self.wyborpracownika, self.wyborfirmy]
            self.relacja.append(relacja)
        elif self.wyborfirmy not in firmy and self.wyborpracownika in pracownicy:
            print("Podana firma nie istnieje w bazie danych")
        elif self.wyborpracownika not in pracownicy and self.wyborfirmy in firmy:
            print("Podany pracownik nie istnieje w bazie danych")
        else:
            print("Nie istnieje ani pracownik ani firma ktora podales w bazie danych")


    def usun_firme_pracownikowi(self):
        for lp, tmp in enumerate(self.relacja):
            print(lp, "Pracownik %s pracuje w firmie: %s" % (tmp[0],tmp[1]))
        wybor = int(input("Wybierz indeks relacji pomiedzy pracownikiem a firma do usuniecia"))
        print("Usunieto relacje pracownika z firma")
        self.relacja.pop(wybor)
        for lp, tmp in enumerate(self.relacja):
            print(lp, "Pracownik %s pracuje w firmie: %s" % (tmp[0], tmp[1]))

    def zatrudnienie_pracownikos(self):
        for tmp in self.relacja:
            print("Pracownik %s pracuje w firmie: %s" % (tmp[0],tmp[1]))


def run_sript():
    try:
        objekt_Firma = Firma()
        objekt_Pracownicny = Pracownicy()
        objekt_Zatrudnienie = Zatrudnienie()
        baza_danych = open("simple_data_base", "rb")
        objekt_Firma.firmy =pickle.load(baza_danych)
        objekt_Pracownicny.pracownicy = pickle.load(baza_danych)
        objekt_Zatrudnienie.relacja = pickle.load(baza_danych)
        baza_danych.close()
    except:
        objekt_Firma = Firma()
        objekt_Pracownicny = Pracownicy()
        objekt_Zatrudnienie = Zatrudnienie()
    finally:
        while True:
            decyzja = input("F - zarzadzaj firmami, P - zarzadzaj pracownikami, Z - zatrudnienie, Q - wyjscie: ").upper()
            if decyzja == "F":
                print("------- MODUL FIRMY -------")
                while True:
                    decyzja = input("D - dodaj firme, U - usun firme, P - pokaz firmy, W - wroc do glownego menu: ").upper()
                    if decyzja == "D":
                        objekt_Firma.dodaj_firme()
                    elif decyzja == "U":
                        objekt_Firma.usun_firme(objekt_Zatrudnienie.relacja)
                    elif decyzja == "P":
                        objekt_Firma.pokaz_firmy()
                    elif decyzja == "W":
                        break
                    else:
                        print("Wybierz jeszcze raz D/U/P")
            elif decyzja == "P":
                print("------- MODUL PRACOWNICY -------")
                while True:
                    decyzja = input("D - dodaj pracownika, U - usun pracownika, P - pokaz pracownikow, W - wroc do glownego menu:  ").upper()
                    if decyzja == "D":
                        objekt_Pracownicny.dodaj_pracownika()
                    elif decyzja == "U":
                        objekt_Pracownicny.usun_pracownika(objekt_Zatrudnienie.relacja)
                    elif decyzja == "P":
                        objekt_Pracownicny.pokaz_pracownikow()
                    elif decyzja == "W":
                        break
                    else:
                        print("Wybierz jeszcze raz D/U/P")
            elif decyzja == "Z":
                print(objekt_Firma.firmy, objekt_Pracownicny.pracownicy)
                print("------- MODUL ZATRUDNIENIE -------")
                while True:
                    decyzja = input("D - dodaj firme do pracownika, U - usun firme pracownikowi, P - pokaz zatrudnienie pracownikow, W - wroc do glownego menu:  ").upper()
                    if decyzja == "D":
                        objekt_Zatrudnienie.przypisz_firme_do_pracownika(objekt_Firma.firmy, objekt_Pracownicny.pracownicy)
                    elif decyzja == "U":
                        objekt_Zatrudnienie.usun_firme_pracownikowi()
                    elif decyzja == "P":
                        objekt_Zatrudnienie.zatrudnienie_pracownikos()
                    elif decyzja == "W":
                        break
                    else:
                        print("Wybierz jeszcze raz D/U/P")
            elif decyzja == "Q":
                baza_danych = open("simple_data_base", "wb")
                pickle.dump(objekt_Firma.firmy, baza_danych)
                pickle.dump(objekt_Pracownicny.pracownicy, baza_danych)
                pickle.dump(objekt_Zatrudnienie.relacja, baza_danych)
                baza_danych.close()
                exit()
            else:
                print("Wybierz jeszcze raz F/P/Z/Q")

run_sript()
