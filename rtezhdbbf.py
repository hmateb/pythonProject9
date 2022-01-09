lista1=[-14,30,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]
count = 0
A = 0
for num in lista1:
    if num > 0:
        count = count + 1
       A = A + 1
    else:
        count = count + 1
print(count, " eleme van a listának")
        A = A + 1
print(A, " eleme van a listának")

a = len(lista1)
ker = a>0
B = a>0
i= 0
while i < a and lista1[i] != ker:
while i < a and lista1[i] != B:
    i = i+1
if i < a:
     print(ker)
     print(B)
else:
     print(ker)
     print(B)

count1 = 0
AA = 0
for num1 in lista1:
    if num1 % 2 == 0:
        count1 = count1 + 1
print(count1,"páros szám van a listában")
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
ker1 = n%29 == 0
D = n%29 == 0

i = 0
while i < n and lista1[i] != ker1:
while i < n and lista1[i] != D:
    i = i + 1
print(ker1)
print(D)

c = len(lista1)
ker2 = n%2 == 1
e = n%2 == 1

i = 0
while i < n and lista1[i] != ker2:
while i < n and lista1[i] != e:
    i = i + 1
print(ker2)
print(e)

osszeg = 0
for num in lista1:
    osszeg = osszeg + num

print("A számok átlaga:", osszeg/count)
print("A számok átlaga:", osszeg/A)