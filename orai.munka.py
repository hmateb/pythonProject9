print("1.feladat")
print(30*"*")

n=int(input("Kérem irjon be egy számot"))
m=int(input("Kérje irjon be egy számot"))
if n>m:
    print(n)
else:
    print(m)

print("2.feladat")
a=int(input("Kérje be a kocka egyik oldalának a számát"))
T=(a*a*a)
if T<27:
    print("elég kicsi kocka")
else:
    print("Jó nagy kocka")

print(T)

print("3.feladat")
print(30*"*")

a=int(input("Kérem adjon meg egy életkort"))
if a<18:
    print("Nem szavazhat")
else:
    print("Szavazhat")

print("4.feladat")
print(30*"*")

n=int(input("kérem irjon be egy tetszőleges számot"))
for i in range(1,n):
    if i%2==0:
        print(i)

print("5.feladat")
print(30*"*")
n=int(input("irjon be egy számot"))
m=0
for i in range(0,n):
    for k in range(0,n):
        if m == k:
            print("1",end="")
        else:
            print("0",end="")
    m =m + 1
    print("")

print("6.feladat")
print(30*"*")
a = []
b=0
for i in range(1,3):
    n=int(input("irjon be egy számot"))
    b=b+n
    a.append(n)
print("A számok átlaga",b/len(a))



print("7.feladat")
print(30*"*")
a = []
m=0
for i in range(1,11):
    n=int(input("irjon be egy számot"))
    m=m+n
    a.append(n)
print("A számok átlaga",m/len(a))