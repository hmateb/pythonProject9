#afeladat:
d = input("Adj meg egy szót: ")
b = []
for i in range(len(d)):
    b.append(ord(d[i])-32)

for i in b:
    print(chr(i), end=" ")
print(" ")
#bfeladat
a = input("Adj meg egy szót: ")
d = []
for i in range(len(a)):
    d.append(ord(a[i])-32)

for i in range(len(d), 0, -1):
    print(chr(d[i-1]), end=" ")
print(" ")
