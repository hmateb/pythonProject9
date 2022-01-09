
lista1=[-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]
hossz=len(lista1)
valtozo=None
for i in range(0, hossz-1):
    min=i
    for j in range(i+1, hossz):
        if lista1[min]>lista1[j]:
         min=j
        valtozo=lista1[i]
    lista1[i]=lista1[min]
    lista1[min]= valtozo
print(lista1)
