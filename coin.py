import random
import numpy as np
import matplotlib.pyplot as plt

liczbaRzutow = int(input('Podaj liczbe rzutow: ')) 
liczbaSymulacji = 10

def RzutMoneta(liczbaRzutow, liczbaSymulacji):
    MalgosiaWygranaAll = []
    MalgosiaWygranaStdAll = []
    LiczbaRzutow = []
    for NRzut in range(liczbaRzutow):
        MalgosiaWygranaRzut = []
        for symulacje in range(liczbaSymulacji):
            MalgosiaWygrana = 0
            for rzut in range(NRzut+1):
                moneta = random.randint(0,1)
                if moneta==1: 
                    MalgosiaWygrana += 1
                else: 
                    MalgosiaWygrana -= 1
            MalgosiaWygranaRzut.append(MalgosiaWygrana)
        print(MalgosiaWygranaRzut)
        OczekiwanaWygranaRzut = np.average(MalgosiaWygranaRzut)
        OczekiwanaWygranaStdRzut = np.std(MalgosiaWygranaRzut)
        MalgosiaWygranaAll.append(OczekiwanaWygranaRzut)
        MalgosiaWygranaStdAll.append(OczekiwanaWygranaStdRzut)
        LiczbaRzutow.append(int(NRzut+1))
    return MalgosiaWygranaAll, MalgosiaWygranaStdAll, LiczbaRzutow

MalgosiaWygranaAll, MalgosiaWygranaStdAll, LiczbaRzutow = RzutMoneta(liczbaRzutow, liczbaSymulacji)

plt.errorbar(LiczbaRzutow, MalgosiaWygranaAll, MalgosiaWygranaStdAll,  fmt='o')
plt.xlabel('Liczba rzutow')
plt.ylabel('Oczekiwana wygrana Malgosi')
plt.show()
