#----------WYŚWIETLACZ LICZB NIEPARZYSTYCH!-----------#
def zadanie(liczba):
    for x in range(1, liczba+1):
        if x % 2 != 0  and x != liczba-1:
            if x == liczba:
                print(x,  end=".")
                exit()
            else:
                print(x,  end=", ")
        elif x % 2 == 0 and x == liczba:
            if x == liczba:
                print("%i." % (liczba-1))
                exit()

def main():
    while True:
        try:
            liczba = int(input("Podaj liczbe: "))
            if liczba > 0:
                zadanie(liczba)
            else:
                print("Liczba nie jest liczbą dodatnią, spórbuj jeszcze raz!")
        except ValueError:
            print("Podano liczbe nie całkowitą lub inny znak")

main()
