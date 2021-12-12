lista1=[-14,30,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]
count = 0
for num in lista1:
    if num > 0:
        count = count + 1
    else:
        count = count + 1
print(count, " eleme van a listának")

a = len(lista1)
ker = a>0
i= 0
while i < a and lista1[i] != ker:
    i = i+1
if i < a:
     print(ker)
else:
     print(ker)

count1 = 0
for num1 in lista1:
    if num1 % 2 == 0:
        count1 = count1 + 1
print(count1,"páros szám van a listában")

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
ker1 = n%29 == 0

i = 0
while i < n and lista1[i] != ker1:
    i = i + 1
print(ker1)

c = len(lista1)
ker2 = n%2 == 1

i = 0
while i < n and lista1[i] != ker2:
    i = i + 1
print(ker2)

osszeg = 0
for num in lista1:
    osszeg = osszeg + num

print("A számok átlaga:", osszeg/count)
