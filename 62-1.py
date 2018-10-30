#------------------------SKLEP---------------------------#

#-----------------Spis przedmiotów w sklepie-------------#
        #### nazwa  # cena # ilość #####

sklep = {1: ['Arbuz', 3.50, 10],
         2: ["Banan", 2.99, 2],
         3: ["Cebula", 9.99, 1],
         4: ["Wisnia", 0.5, 100],
         5: ["Morela", 5.45, 15],
         6: ["Jablko", 1.51, 8]}

#-----------------Tablica zamowienia---------------------#

zamowienie = []


def exit_function():
    print("Do następnego razu...\nZegnaj")
    exit()


def sprawdzenie_ilosci_produktu(numer_produktu, zamowiona_ilosc):
    sprawdz_ilosc = sklep[numer_produktu][2]
    if sprawdz_ilosc >= zamowiona_ilosc:
        print("Ok, mamy tyle w magazynie, laduje...")
        return zamowiona_ilosc
    elif sprawdz_ilosc < zamowiona_ilosc:
        print("Przykro mi, nie mamy takiej ilości wybranego produktu, Moze zechcesz kupic cos innego?")
        return twoj_wybor()


def cena_produktu(id, ilosc_produktu):
    cenaxilosc = ilosc_produktu * sklep[id][1]
    print("%s w ilosci zamówionej kosztuje: %d" % (sklep[id][0], cenaxilosc), "PLN")
    return sklep[id][0], ilosc_produktu, cenaxilosc


def dodaj_do_zamowienia(nazwa_produktu, zamowiona_ilosc, cena_calkowita):
    zamowienie.append([nazwa_produktu, zamowiona_ilosc, cena_calkowita])
    return zamowienie


def rachunek(zamowienie):
    pieniadze = 0
    for powtorz in range(0, len(zamowienie)):
        pieniadze += zamowienie[powtorz][2]
    return pieniadze


def aktualne_zamowienie(zamowienie):
    print("--------------------------")
    print("|        RACHUNEK        |")
    print("--------------------------")
    print("|  Produkt  |Ilość| Cena |")
    print("--------------------------")
    for powtorz in range(0, len(zamowienie)):
        print("|%10s" % zamowienie[powtorz][0], "|%4s" % zamowienie[powtorz][1], "|%5.2f" % zamowienie[powtorz][2], "|")
    print("--------------------------")


def twoj_wybor():
    print("Zatem wybierz proszę przedmiot ktory cie interesuje podając numer ID oraz ilość która chcesz kupic")
    pokaz_liste()
    try:
        i_d = int(input("Wybierz przedmiot z listy podając numer ID: "))
        ilosc = int(input("Wybierz ile chcesz kupić produktów typu %s " % sklep[i_d][0]))
        zamowiona_ilosc = sprawdzenie_ilosci_produktu(i_d, ilosc)
        [nazwa_produktu, zamowiona_ilosc, cena_calkowita] = cena_produktu(i_d, zamowiona_ilosc)
        zamowienie = dodaj_do_zamowienia(nazwa_produktu, zamowiona_ilosc, cena_calkowita)
        aktualne_zamowienie(zamowienie)
    except KeyError:
        print("Nie ma takiej liczby w menu zaprezentowanym")
    except ValueError:
        print("Należało podać liczbę a inny znak")
    finally:
        while True:
            decyzja2 = input("Czy chcesz dodatkowo cos kupic? (t/n)")
            if decyzja2 == "t":
                twoj_wybor()
            elif decyzja2 == "n":
                try:
                    pieniadze = rachunek(zamowienie)
                    print("W sumie musisz zaplacic za wszystkie produkty %6.2f" % pieniadze, "PLN")
                except UnboundLocalError:
                    print("Prawdopodobnie nic nie kupiles dlatego tez")
                exit_function()
            else:
                print("Proszę wpisać literę \"t\" lub \"n\" ")


def pokaz_liste():
    print("------------------")
    print("|ID |", "   Produkt |")
    print("------------------")
    for lista_w_sklepie in sklep:
        print("|", lista_w_sklepie, "|", "%10s" % sklep[lista_w_sklepie][0], "|")
    print("------------------")


def main():
    print("Witaj w sklepie!\n" + "Oto lista dostepnych produktow w sklepie:")
    pokaz_liste()
    while True:
        decyzja = input("Czy chcesz cos kupic? (t/n): ")
        if decyzja == "t":
            twoj_wybor()
        elif decyzja == "n":
            return exit_function()
        else:
            print("Zła litera, Proszę wpisać literę \"t\" lub \"n\" ")


main()
