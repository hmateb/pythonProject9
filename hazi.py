orszag=[{'nev':'Ausztria',
        'fovaros':"Bécs",
        'csatlakozas':1995},
        {'nev':"Belgium",
        'fovaros':"Brüsszel",
        'csatlakozas':1952},
        {'nev':"Bulgária",
        'fovaros':"Szófia",
        'csatlakozas':2007},
        {'nev':"Horváthország",
        'fovaros':"Zágráb",
        'csatlakozas':2013},
        {'nev':"Ciprus",
        'fovaros':"Nicosia",
        'csatlakozas':2004},
        {'nev':"Csehország",
        'fovaros':"Prága",
        'csatlakozas':2004},
        {'nev':"Dánia",
        'fovaros':"Koppenhága",
        'csatlakozas':1973},
        {'nev':"Észtország",
        'fovaros':"Tallinn",
        'csatlakozas':2004},
        {'nev':"Finnország",
        'fovaros':"Helsinki",
        'csatlakozas':1995},
        {'nev':"Franciaország",
        'fovaros':"Párizs",
        'csatlakozas':1952},
        {'nev':"Németország",
        'fovaros':"Berlin",
        'csatlakozas':1952},
        {'nev':"Görögország",
        'fovaros':"Athén",
        'csatlakozas':1981},
        {'nev':"Magyarország",
        'fovaros':"Budapest",
        'csatlakozas':2004},
        {'nev':"írország",
        'fovaros':"Dublin",
        'csatlakozas':1973},
        {'nev':"Olaszország",
        'fovaros':"Róma",
        'csatlakozas':1952},
        {'nev':"Lettország",
        'fovaros':"Riga",
        'csatlakozas':2004},
        {'nev':"Litvánia",
        'fovaros':"Vilnius",
        'csatlakozas':2004},
        {'nev':"Luxemburg",
        'fovaros':"Luxemburg",
        'csatlakozas':1952},
        {'nev':"Málta",
        'fovaros':"La Valetta",
        'csatlakozas':2004},
        {'nev':"Hollandia",
        'fovaros':"Hága",
        'csatlakozas':1952},
        {'nev':"Lengyelország",
        'fovaros':"Varsó",
        'csatlakozas':2004},
        {'nev':"Portugália",
        'fovaros':"Lisszabon",
        'csatlakozas':1986},
        {'nev':"Románia",
        'fovaros':"Bukarest",
        'csatlakozas':2007},
        {'nev':"Szlovákia",
        'fovaros':"Pozsony",
        'csatlakozas':2004},
        {'nev':"Szlovénia",
        'fovaros':"Ljubljana",
        'csatlakozas':2004},
        {'nev':"Spanyolország",
        'fovaros':"Madrid",
        'csatlakozas':1986},
        {'nev':"Svédország",
        'fovaros':"Stockholm",
        'csatlakozas':1995}]

def csatl_ev(elem):
        return elem["csatlakozas"]
ev_rendezett=sorted(orszag,key=csatl_ev)
elso=ev_rendezett[0]["csatlakozas"]
i=0
while ev_rendezett[i]["csatlakozas"]==elso:
        i+=1
print("Az alapítótagok száma:", i)
print(" A leghosszabb a neve:")
min=orszag[i]["nev"]
for i in range(len(orszag)):
        if len(orszag[i]["nev"])<len(min):
                min=orszag[i]["nev"]
print(min)
while len(ev_rendezett[i]["nev"])==len(min):
        print("-",ev_rendezett[i]["nev"])
i+=1
print("Négy betűs a fővárosa:")
for i in range(len(orszag)):
  if len(orszag[i]["fovaros"])==4:
        print(orszag[i]["nev"], "-", orszag[i]["fovaros"])
