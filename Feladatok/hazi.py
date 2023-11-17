print()
a=int(input( "Adj meg egy páros számot: " ))
szam_fele = int(a / 2)

darab_karakter = 1
sor = 1
while sor <= a:
    oszlop = 1
    while oszlop <= darab_karakter:
        print( "O ", end='' )
        oszlop += 1
    print('')
    darab_karakter += 1
    sor += 1
darab_karakter = a
sor = 1
while sor <= a:
    oszlop = 1
    while oszlop <= darab_karakter:
        print( "O ", end='' )
        oszlop += 1
    print('')
    darab_karakter -= 1
    sor += 1
print()
