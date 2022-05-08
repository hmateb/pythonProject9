szam1=int(input("Elso szam"))
szam2=int(input("Második szám"))
if (szam1>0 and szam2>0):
    if (szam1>szam2):
        nagyobb=szam1
        kisebb=szam2
    else:
        nagyobb=szam2
        kisebb=szam1
    kell=1
    szam=kisebb
    while (kell==1):
        if (kisebb % szam==0 and nagyobb % szam==0):
            lko=szam
            kell=0
        szam=szam-1
    szoveg="A ket szam("+ str(szam1) + "," + str(szam2) + ") legnagyobb kozos oszto: "+str(lko)
    print(szoveg)