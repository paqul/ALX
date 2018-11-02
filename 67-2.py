from datetime import date as d

#---------------------------HOTEL---------------------------#
def exit_function():
    print("Do zobaczenia!")
    exit()

def forumarz_rezerwacji(var1, var2, var3, var4, var5, var6, var7, var8, ile_dni, ile_osob, sniadanie, imie):
    print("\n"*3)
    print("================================")
    print("|  FORMULARZ    REJESTRACYJNY  |")
    print("|------------------------------|")
    print("| Data przybycia:  %i%i-%i%i-%i%i%i%i  |" % (var7, var8, var5, var6, var1, var2, var3, var4))
    print("| Ilość dni pobytu:       %3i  |" % ile_dni)
    print("| Ilość osób:             %3i  |" % ile_osob)
    print("| Śniadania w każdy dzień: %s |" % sniadanie)
    print("| Rezerwujący: %15s |" % imie)
    print("|------------------------------|")
    print("|  ŻYCZYMY   MIŁEGO   POBYTU   |")
    print("|     W   NASZYM   HOTELU      |")
    print("================================")
    exit_function()


def termin_przybycia():
    print("Podaj date przybycia do hotelu w formacie (rrrr-mm-dd) np. 2018-12-07")
    while True:
        data_przybycia=input("Data przybycia: ")
        tab = []
        for var in data_przybycia:
            try:
                var = int(var)
                tab.append(var)
            except:
                myslnik = var
        if len(tab) == 8:
            dzien = int(("%i" + "%i") % (tab[6], tab[7]))
            miesiac = int(("%i" + "%i") % (tab[4], tab[5]))
            if dzien > 31 or miesiac > 12:
                print("Popełniłeś błąd przy wpisywaniu daty - proszę sprawź to i wpisz jeszcze raz poprawnie!")
                termin_przybycia()
            else:
                try:
                    if data_przybycia == ("%i%i%i%i-%i%i-%i%i"% (tab[0], tab[1], tab[2], tab[3], tab[4], tab[5], tab[6], tab[7])):
                        if data_przybycia > str(d.today()):
                            print("Podana data: %s - została zaakceptowana" % data_przybycia)
                            return tab[0], tab[1], tab[2], tab[3], tab[4], tab[5], tab[6], tab[7]
                        else:
                            print("Podana data jest z przeszłości lub teraźniejszości, podaj ją jeszcze raz najbliższy możliwy termin rezerwacji to jutro!")
                except IndexError:
                    print("Podałeś datę przybycia w niewłaściwym formacie")
        else:
            print("Podales date w niewłaściwym formacie - spróboj jeszcze raz")



def ilosc_dni():
    while True:
        try:
            ile_dni = int(input("Podaj liczbę dni, przez jaką zostaniesz w hotelu: "))
            if ile_dni > 731:
                print("Jeżeli chcesz zostać w hotelu powyżej dwóch lat to powinieneś to osobiście ustalić z włąścicielem bezpośrednio podczas pobytu")
                print("Wpisz np 14 dni - przyjedź na 2 tygodnie i resztę swojego pobytu ustal z właścicielem")
            elif ile_dni <= 0:
                print("Dalsze wypełnianie formularza nie ma sensu, skoro nawet 1 dnia nie zostaniesz w hotelu")
                while True:
                    dec = input("Czy chcesz zacząc wypełniać formularz od początku: (t/n)")
                    dec = dec.lower()
                    if dec == "t":
                        main()
                    elif dec == "n":
                        exit_function()
                    else:
                        print("Wpisałeś nie poprawnie")
            else:
                return ile_dni
        except ValueError:
            print("Podaj prosze ilość dni (nie używaj ułamków)")


def ilosc_osob():
    while True:
        try:
            ile_osob = int(input("Podaj ile osob z tobą przyjedzie?, Jeżeli będziesz sam to wpisz \"0\""))
            ile_osob += 1
            if ile_osob > 100:
                print("Jeżeli chcesz zabrać ze sobą regiment wojska to proszę o bezpośredni kontakt z hotelem")
            else:
                return ile_osob
        except ValueError:
            print("Podaj prosze ilość osób które przybędą razem z tobą (nie używaj ułamków)")


def sniadanie():
    while True:
        sniadanie = input("Czy chcesz zamówić dodatkowo śniadanie w hotelu na każdy dzień pobytu: (T/N)")
        sniadanie = sniadanie.lower()
        if sniadanie == "t":
            return "tak"
        elif sniadanie == "n":
            return "nie"
        else:
            print("Wpisałeś nie poprawnie")


def imie_fun():
    imie = input("Podaj swoje imie: ")
    imie_OK = imie                      #takie szybkie obejscie :)
    imie = list(imie)
    counter_error = 0
    for sprawdz in imie:
        if sprawdz.isdigit() == True or sprawdz in "~!@#$%^&*()_+-={}[]'\/,.<>":
            counter_error += 1
    if counter_error >= 1:
        print("Błąd! - Podaj imie bez cyfr oraz znaków innych niż litery w imieniu!")
        return imie_fun()
    else:
        return imie_OK.capitalize()


def rezerwacja():
    print("Prosze o podanie natepujacych informacji w celu rezerwacji w naszym hotelu")
    [var1, var2, var3, var4, var5, var6, var7, var8] = termin_przybycia()
    days = ilosc_dni()
    people = ilosc_osob()
    breakfest = sniadanie()
    name = imie_fun()
    return forumarz_rezerwacji(var1, var2, var3, var4, var5, var6, var7, var8, days, people, breakfest, name)


def opishotelu():
    print("Nasz hotel wogole jest super i inny \"marketingowy belkot\", \ntak aby zachecic Cie do rezerwacji i wydania pieniedzy na hotel!")
    while True:
        decyzja=input("Czy napewno chcesz wyjsc z aplikacji? (t/n)")
        if decyzja == "t":
            exit_function()
        elif decyzja == "n":
            main()
        else:
            print("Wpisz \"t\" lub \"n\"")


def main():
    print("Witaj w aplikacji Hotelowej!\nCzy chcesz zarezerwować sobie miejsce w Hotelu? (t/n)", end="")
    while True:
        decyzja=input()
        if decyzja == "t":
            rezerwacja()
        elif decyzja == "n":
            opishotelu()
        else:
            print("Wpisz \"t\" lub \"n\"", end="")


main()
