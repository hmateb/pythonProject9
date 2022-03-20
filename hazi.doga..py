def sorozat(szoveg):
    num=0
    for szam in szoveg:
        if szam !=".":
            num+= int(szam)
        return str(num)
def honap(szoveg):
    honapok=["január","február","március","április","május","június","július","augusztus","szeptember","október","november","december"]


digitoflife=input("Add meg születési dátumod!")
while len(digitoflife)!=1:
    digitoflife=sorozat(digitoflife)
if honap in digitoflife:
    print("Az élet számod:",digitoflife)