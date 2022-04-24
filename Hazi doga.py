forras=open('./parduc_2.feladat.txt','r',encoding='utf-8')
for num in forras
    osszeg = osszeg + num
count = 0
for num in forras:
    if num < 0 or num > 0:
        count = count + 1
#3 feladat
with open('./programnyelv_1feladat.txt','r',encoding='utf-8')as forras:
    with open('./masolat.txt', 'w', encoding='utf-8') as cel:
        for sor in forras:
            print(sor,file=cel)















