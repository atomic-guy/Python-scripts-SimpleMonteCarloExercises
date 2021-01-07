import random
import numpy as np
import matplotlib.pyplot as plt

def dzieci(N):
    # plec: 0 - chlopiec, 1 - dziewczynka
    licznikDzieci = []
    dziewczynki = 0
    chlopcy = 0
    prawdopodobienstwo = 0    
    for i in range(N):
        plec = random.randint(0,1)
        if plec==0: 
            chlopcy += 1
        else: 
            dziewczynki += 1
            break
    if dziewczynki != 0:
        prawdopodobienstwo = 0.5 ** (chlopcy + 1) 
    Wyniki.append([dziewczynki, chlopcy, prawdopodobienstwo])

    return

N = int(input('Podaj maksymalna liczbe dzieci: ')) 
Wyniki = []

for n in range(1000):
    dzieci(N)

WynikiArr = np.unique(np.asarray(Wyniki), axis=0)
print(Wyniki)
print(WynikiArr)

x = np.arange(N+1)
xticks = WynikiArr[:, 2]
y1Dz = WynikiArr[:, 0]
y2Ch = WynikiArr[:, 1]

width = 0.1
p1 = plt.bar(x, y2Ch, width)
p2 = plt.bar(x, y1Dz, width, bottom=y2Ch)
plt.legend((p1[0], p2[0]), ('Chlopcy', 'Dziewczynki'))
plt.xticks(x, xticks)
plt.xlabel('Prawdopodobienstwo urodzenia dziewczynki')
plt.show()