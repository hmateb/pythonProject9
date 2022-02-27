titkositas = 0
eltolas = 0
def cezar():
    a = input("Kérem adjon meg egy szót: ")
    global titkositas
    global eltolas
    eltolas = int(input("Kérem adja meg az eltolás mértékét: "))
    for i in a:
        if ord(i) + eltolas > 122 and 97 <= ord(i) <= 122:
            titkositas += 96 + (ord(i) + eltolas - 122)
        elif ord(i) + eltolas > 90 and 65 <= ord(i) <= 90:
            titkositas += 64 + (ord(i) + eltolas - 90)
        else:
            titkositas += ord(i) + eltolas
    print(chr(titkositas))
cezar()