import random
import numpy as np
import matplotlib.pyplot as plt

N = int(input('Podaj liczbe punktow: '))

def Szescian(N):
    Npunktow = []
    odlegosciAverageList = []
    odleglosciAverageStdList = []
    for Npkt in range(N):
        punkty = []
        for i in range(Npkt+1):
            p = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
            punkty.append(p)
        print(punkty)
        punktyArr = np.asarray(punkty)
        odleglosci = np.linalg.norm(punktyArr - punktyArr[:,None], axis=-1)
        print(odleglosci)
        odleglosci = odleglosci[odleglosci!=0]
        odleglosci = np.unique(odleglosci)
        odlegosciAverage = np.average(odleglosci)
        odleglosciAverageStd = np.std(odleglosci)
        odlegosciAverageList.append(odlegosciAverage)
        odleglosciAverageStdList.append(odleglosciAverageStd)
        Npunktow.append(Npkt + 1)
    return odlegosciAverageList, odleglosciAverageStdList, Npunktow

odlegosciAverageList, odleglosciAverageStdList, Npunktow = Szescian(N)

plt.errorbar(Npunktow, odlegosciAverageList, yerr=odleglosciAverageStdList, fmt='o')
plt.xlabel('Liczba punktow')
plt.ylabel('Srednia arytmetyczna odleglosci miedzy punktami')
plt.show()