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

print(f'5. feladat: Napi kölcsönzések száma: {len(lista)}')

nevinput = input('6. feladat: Kérek egy nevet: ')

talalhato = False
for n in lista:
        if nevinput == n.nev:
            talalhato = True

if talalhato == False:
    print('\tNem volt ilyen  nevű kölcsönző!')
else:
    print('\t', nevinput, 'kölcsönzései:')
    for n in lista:
        if nevinput == n.nev:
            if len(n.eora) == 1:
                eora = ['0', n.eora]
                n.eora = ''.join(eora)
            if len(n.eperc) == 1:
                eperc = ['0', n.eperc]
                n.eperc = ''.join(eperc)
            if len(n.vora) == 1:
                vora = ['0', n.vora]
                n.vora = ''.join(vora)
            if len(n.vperc) == 1:
                vperc = ['0', n.vperc]
                n.vperc = ''.join(vperc)

            print(f'\t{n.eora}:{n.eperc}-{n.vora}:{n.vperc}')

