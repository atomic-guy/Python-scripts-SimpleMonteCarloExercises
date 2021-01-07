import random, math, numpy
import matplotlib.pyplot as plt

d = int(input('Podaj liczbe wymiarow: ')) 
liczbaSymulacji = 20
liczbaPunktow = 100000

def ObjetoscNKuli(d, liczbaSymulacji):
    wynikiObjetosc = []
    wynikBlad = []
    wymiary = []
    for w in range(d):
        wymiar = w + 1
        wynikiObjetoscJedenWymiar = []
        for symulacje in range(liczbaSymulacji):
            punkty_w_kuli = 0
            for iteracje in range(liczbaPunktow):
                punkt = numpy.random.uniform(-1.0, 1.0, wymiar)
                odleglosc = numpy.linalg.norm(punkt)
                if odleglosc < 1.0:
                    punkty_w_kuli += 1
            objetosc = numpy.power(2.0, wymiar) * (punkty_w_kuli / liczbaPunktow)
            wynikiObjetoscJedenWymiar.append(objetosc)
        objetoscAverrage = numpy.average(wynikiObjetoscJedenWymiar)
        objetoscBlad = numpy.std(wynikiObjetoscJedenWymiar)
        wymiary.append(wymiar)
        wynikiObjetosc.append(objetoscAverrage)
        wynikBlad.append(objetoscBlad)           
    return wymiary, wynikiObjetosc, wynikBlad

def ObjetoscNKuliDokladna(d):
    wynikiObjetoscDokladna = []
    for w in range(d):
        wymiar = w + 1
        objetosc = math.pi**(wymiar/2)/math.gamma(wymiar/2 + 1)
        wynikiObjetoscDokladna.append(objetosc)
    return wynikiObjetoscDokladna

wymiary, wynikiObjetosc, wynikBlad = ObjetoscNKuli(d, liczbaSymulacji)
wynikiObjetoscDokladna = ObjetoscNKuliDokladna(d)

print(wynikiObjetosc)
print(wynikiObjetoscDokladna)

plt.errorbar(wymiary, wynikiObjetosc, yerr=wynikBlad, fmt='o')
plt.plot(wymiary, wynikiObjetoscDokladna, '-')
plt.xlabel('Liczba wymiarow n')
plt.ylabel('Objetosc n-wymiarowej kuli')
plt.show()


