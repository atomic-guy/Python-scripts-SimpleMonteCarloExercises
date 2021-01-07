import random

def rzut_kostka():
    pozostale = 1
    szostka = 6
    return random.randint(pozostale, szostka)

def cztery_rzuty():
    for _ in range(4):
        if rzut_kostka() == 6:
            return True
    return False

def dwadziescia_cztery_rzuty():
    for _ in range(24):
        if rzut_kostka() + rzut_kostka() == 12:
            return True
    return False

def problem1():
    liczba_szostek = 0
    liczba_powotrzen = 1000000
    for i in range(liczba_powotrzen):
        if cztery_rzuty() == True:
            liczba_szostek = liczba_szostek + 1
    prawdopod_symulacja = liczba_szostek / liczba_powotrzen
    prawdopod_obliczone = 1 - (5/6)**4
    print("Otrzymanie przynajmniej jednej szostki w czterech rzutach kostka:")
    print("   Prawdopodobienstwo z symulacji = ", prawdopod_symulacja)
    print("   Prawdopodobienstwo obliczone = ", prawdopod_obliczone)
    return

def problem2():
    liczba_podwojnych_szostek = 0
    liczba_powotrzen = 1000000
    for i in range(liczba_powotrzen):
        if dwadziescia_cztery_rzuty() == True:
            liczba_podwojnych_szostek = liczba_podwojnych_szostek + 1
    prawdopod_symulacja = liczba_podwojnych_szostek / liczba_powotrzen
    prawdopod_obliczone = 1 - (35/36)**24
    print("Otrzymanie przynajmniej jednej podwojnej szostki w dwudziestu czterech rzutach dwiema kostkami:")
    print("   Prawdopodobienstwo z symulacji = ", prawdopod_symulacja)
    print("   Prawdopodobienstwo obliczone = ", prawdopod_obliczone)

problem1()
print()
problem2()