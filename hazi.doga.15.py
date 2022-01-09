lista1 = [ -14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]
#1
print(" 1. Van-e a sorozatban pozitív szám? ")
count=0
for i in lista1:
    if i>0:
        count=count+1
if count>0:
    print("Van pozitív szám a listában")
#2
print(" 2. Hány eleme van a sorozatnak? ")
count = 0
for num in lista1:
    if num < 0 or num > 0:
        count = count + 1
print(count)

#3
print(" 3. Mennyi a sorozatban található legkisebb szám? ")
minElem = lista1[0]
for elem in lista1:
    if elem < minElem:
        maxElem = elem
print(minElem)
#4
print(" 4. Írjuk ki az első 33-mal osztható szám indexét! ")
szamold = True
szam = lista1 [0]
elem = 0
for i in range(len(lista1)):
    if lista1[i] % 33 == 0:
        szam = elem
        hely = i
        szamold = False
print( "33-al osztható számok helye:", hely)
#5
print(" 5. Mennyi a sorozatban található számok átlagának a fele? ")
osszeg = 0
for num in lista1:
    osszeg = osszeg + num
count = 0
for num in lista1:
    if num < 0 or num > 0:
        count = count + 1

print(osszeg%count/2)
#6
print(" 6. Igaz-e, hogy minden szám pozitív?" )
paros = True
for i in range(len(lista1)):
    if lista1[i] % 2 != 0:
        paros = False
        print("Nem minden szám páros.")
    else:
        print("Minden szám páros.")
#7
print(" 7. Hány páratlan szám található a sorozatban? ")
count = 0
for num in lista1:
    if num < 0:
        count = count + 1
print(count)
#8
print(" 8.  Van-e a sorozatban olyan negatív szám, amelyet újabb negatív követ? ")
#9
print(" 9. Írjuk ki az utolsó 19-cel osztható szám indexét! ")
szamold = True
szam = lista1 [0]
elem = 0
lista1.reverse()
for i in range(len(lista1)):
    if lista1[i] % 17 == 0:
        szam = elem
        hely = i
        szamold = False
print( "19-tel osztható utolsó szám helye:", hely)
#10
print(" 10. Írjuk ki a sorozatban található 5-tel osztható számokat! ")
a = []
for elem in lista1:
    if elem%5==0:
        a.append(elem)
print(a)