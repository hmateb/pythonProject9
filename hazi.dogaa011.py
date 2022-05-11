fajl=open("autok (1).csv","r",encoding="UTF-8")
next(fajl)
indulas=[]
cél=[]
rendszam=[]
telefonszam=[]
ferohely=[]
for sorok in fajl:
    sor=sorok.split(";")
    indulas.append(sor[0])
    cél.append(sor[1])
    rendszam.append(sor[2])
    telefonszam.append(sor[3])
    ferohely.append(int(sor[4]))
def átlagferohely():
    max=0
    maxszam=0
    for i in range(0,len(indulas)):
        if indulas[i]=="Munkács":
            if cél[i]=="Záhony":
                max+=ferohely[i]
                maxszam+=1
    print(max/maxszam)
átlagferohely()
def átlag():
    max=0
    for a in ferohely:
        max+=a
    átlag=(max/len(ferohely))
    átlag=int(átlag*10)/10
    print(átlag)
átlag()
ki=open("budapestrol.dat","w",encoding="UTF-8")
for i in range(len(ferohely)):
    if indulas[i]=="Budapest":
        ki.write(f"{cél[i]} {telefonszam[i]}\n")


print(cél)