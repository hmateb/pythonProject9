allat={}
run = True
while run:
    a=input("adja meg az állat nevét:")
    if a !="":
        b=int(input("adja meg a születési évét az állatnak:"))
        c=input("adja meg az állat fajtáját:")
        allat['név']=a
        allat['év'] = 2022-b
        allat['fajta'] = c
    else:
        run=False
print("1.állat")
for key in allat.keys():
     print(key, "-->", allat[key])

#2feladat

orszag = {}
l2 = []

run1 = True
while run1:

    d = input("adja meg az ország nevét:")
    if d != "":
       e = input("Adja meg az ország fővárosát")
       f = input("Adja meg hogy ez az ország mikor csatlakozott az EU-hoz (év):")
       orszag['ország neve'] = d
       orszag['ország fővárosa'] = e
       orszag['EU-hoz csatlakozás'] = f
       y = orszag.copy()
       l2.append(y)

    else:
          run1=False

print(l2)