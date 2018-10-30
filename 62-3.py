#------------------------WARCABY----------------------#
def poziome():
    for x in range(20):
        print("-", end="")
    print("")


def biale(x):
    if x % 2 != 0:
        for x in range(4):
            print("0 W ", end="")
    elif x % 2 == 0:
        for x in range(4):
            print("W 0 ", end="")


def czarne(x):
    if x % 2 != 0:
        for x in range(4):
            print("0 B ", end="")
    elif x % 2 == 0:
        for x in range(4):
            print("B 0 ", end="")


def srodek(x):
    if x % 2 == 0:
        for x in range(4):
            print("1 0 ", end="")
    elif x % 2 != 0:
        for x in range(4):
            print("0 1 ", end="")


def main():
    for x in range(1, 9):
        print(str(x)+ "|", end="")
        if x <= 3:
            biale(x)
        elif x >=6:
            czarne(x)
        else:
            srodek(x)
        print("|"+str(x))

def wykonaj_v1():
    poziome()
    main()
    poziome()


def poziome2():
    for x in range(23):
        print("-", end="")
    print("")


def main2():
    for x in range(1, 9):
        print(str(x)+ " | ", end="")
        if x <= 3:
            biale(x)
        elif x >=6:
            czarne(x)
        else:
            srodek(x)
        print("| "+str(x))


def wykonaj_v2():
    poziome2()
    main2()
    poziome2()


# realizacja zadania
wykonaj_v1()  # wersja w 100% zgodna z treścią zadania
wykonaj_v2()  # druga wersja - bardziej symetryczna wg mnie ;)