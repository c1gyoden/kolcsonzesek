class Kolcsonzes:
    def __init__(self, nev, jazon, eora, eperc, vora, vperc):
        self.nev = nev
        self.jazon = jazon
        self.eora = eora
        self.eperc = eperc
        self.vora = vora
        self.vperc = vperc

    def __str__(self):
        return f'Név: {self.nev}\nAzonosító: {self.jazon}\n'
    
lista = []

fajl = open('kolcsonzesek.txt', 'rt', encoding='utf-8')
fajl.readline()

for sor in fajl:
    sor = sor.strip().split(';')
    lista.append(Kolcsonzes(sor[0], sor[1], sor[2], sor[3], sor[4], sor[5]))

