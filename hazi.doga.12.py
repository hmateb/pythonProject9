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
