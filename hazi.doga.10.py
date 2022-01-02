lista1=[-14,30,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]
A = 0
for num in lista1:
    if num > 0:
       A = A + 1
    else:
        A = A + 1
print(A, " eleme van a listának")

a = len(lista1)
B = a>0
i= 0
while i < a and lista1[i] != B:
    i = i+1
if i < a:
     print(B)
else:
     print(B)

AA = 0
for num1 in lista1:
    if num1 % 2 == 0:
        AA = AA + 1
print(AA,"páros szám van a listában")

maxElem = lista1[0]
for elem in lista1:
    if elem > maxElem:
        maxElem = elem
print(maxElem, " legnagyobb szám")

count2 = 0
for num2 in lista1:
    if num2 % 10 == 0:
        count2 = count2 + 1
print(count2, "db 10-el osztható szám van a listában")

n = len(lista1)
D = n%29 == 0

i = 0
while i < n and lista1[i] != D:
    i = i + 1
print(D)

c = len(lista1)
e = n%2 == 1

i = 0
while i < n and lista1[i] != e:
    i = i + 1
print(e)

osszeg = 0
for num in lista1:
    osszeg = osszeg + num

print("A számok átlaga:", osszeg/A)
#2
t2=[24, 96, -38, 45, 68, 43, 49, 30, 66, 99, 93, 81, -31, 62, 3, 79, 74, 80, 28, 17, -64, 86, -11, 4, 78, 73, 18, 2, 91, -9]
##Határozd meg az átlaghőmérsékletet!
osszeg=0
for num in t2:
    osszeg = osszeg+num
count=0
for num in t2:
    if num > 0:
        count= count+1
    else:
        count= count+1
print("Átlaghőmérséklet", osszeg/count)
#2 Határozd meg a legkisebb hőmérsékletet!
mine=t2[0]
for elem in t2:
    if elem < mine:
        mine = elem
print(mine)
#Keresd meg a legmelegebb napot, írd ki a hőmérsékletet és azt is, hányadik napon mérték!
maxElem = t2[0]
for i in range(1,len(t2)):
    if t2[i] > maxElem:
        maxElem = elem
        maxhely = i
print(maxElem,maxhely)
#hány napon fagyott?
t3 = []
for elem in t2:
    if elem < 0:
        t3.append(elem)
print(t3,"napon fagyott")