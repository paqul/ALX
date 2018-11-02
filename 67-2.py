#---------------------------HOTEL---------------------------#

def forumarz_rezerwacji(ile_dni, ile_osob, sniadanie, imie):
    print("================================")
    print("|  FORMULARZ    REJESTRACYJNY  |")
    print("|------------------------------|")
    print("| Data przybycia: (in progres) |")
    print("| Ilość dni pobytu:       %3i  |" % ile_dni)
    print("| Ilość osób:             %3i  |" % ile_osob)
    print("| Śniadania w każdy dzień: %s |" % sniadanie)
    print("| Rezerwujący: %15s |" % imie)
    print("|------------------------------|")
    print("|  ŻYCZYMY   MIŁEGO   POBYTU   |")
    print("|     W   NASZYM   HOTELU      |")
    print("================================")


def termin_przybycia():
    print("Podaj date przybycia do hotelu w formacie (rrrr-mm-dd) np. 2018-12-07\n")
    data_przybycia=input("Data przybycia: %i %i %i %i - %i %i - %i %i")
    print("Data przybycia zostala zarezerwowana na", data_przybycia)
    print(type(data_przybycia))


def ilosc_dni():
    while True:
        try:
            ile_dni = int(input("Podaj liczbę dni, przez jaką zostaniesz w hotelu: "))
            if ile_dni > 731:
                print("Jeżeli chcesz zostać w hotelu powyżej dwóch lat to powinieneś to osobiście ustalić z włąścicielem bezpośrednio podczas pobytu")
                print("Wpisz np 14 dni - przyjedź na 2 tygodnie i resztę swojego pobytu ustal z właścicielem")
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
        return imie_OK


def rezerwacja():
    print("Prosze o podanie natepujacych informacji w celu rezerwacji w naszym hotelu")
    # termin_przybycia()
    days = ilosc_dni()
    people = ilosc_osob()
    breakfest = sniadanie()
    name = imie_fun()
    return forumarz_rezerwacji(days, people, breakfest, name)


def opishotelu():
    print("Nasz hotel wogole jest super i inny \"marketingowy belkot\", \ntak aby zachecic Cie do rezerwacji i wydania pieniedzy na hotel!")
    while True:
        decyzja=input("Czy napewno chcesz wyjsc z aplikacji? (t/n)")
        if decyzja == "t":
            print("Do zobaczenia!")
            exit()
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


# rezerwacja()
# main()
# termin_przybycia()
