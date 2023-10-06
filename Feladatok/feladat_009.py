#feladat_009

'''
Kérjünk be két egész számot (szám1 , szám2).
Hasonlítsuk össze a két számot és irassuk ki,
hogy a szám1 vagy a szám2 a nagyobb/kisebb vagy pedig egyenlők.
'''

szam1 = int(input( "Add meg az első számot: " ))
szam2 = int(input( "Add meg a második számot: " ))

if szam1 > szam2:
    print( "Az első szám a nagyobb." )
elif szam1 < szam2:
    print( "A második szám a nagyobb." )
elif szam1 == szam2:
    print( "A két szám egyenlő." )