lista = []
def paros_e():
    null = False
    while not null:
       a = int(input("Adjon meg egy számot: "))
       if a == 0:
            null = True
       else:
            lista.append(a)
            if a % 2 == 0:
                print("Ez a szám páros!")
            else:
                print("Ez egy páratlan szám!")
    print(lista)

def osszeg_fg():
    b = 0
    for i in lista:
        b += i
    print("A számok összege: ", b)
def atlag():
    b=0
    for i in lista:
        b += i
    print("A számok átlaga:",b/len(lista))


def harommal_oszthatok():
    c = 0
    for i in range(len(lista)):
        if lista[i]%3==0:
            c += 1
    print("3-al osztható számok:",c)
def kisebb():
    min=0
    for i in lista:
        if lista[i]<lista[0]:
            min = lista[i]
    print("legkisebb szám:",min)

paros_e()
osszegfg()
atlag()
harommal