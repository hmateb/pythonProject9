listam= [32, 12, 8, 2, 5, 3, 75, 15]
listaparos= []
listaparatlan= []
for i in listam:
    if i%2==0:
        listaparos.append(i)
    else:
        listaparatlan.append(i)
print (listaparatlan)
print (listaparos)