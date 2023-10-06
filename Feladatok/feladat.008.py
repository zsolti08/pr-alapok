#feladat_008

jegy = int(input( "Kérek egy jegyet 1-től 5-ig: " ))
if jegy == 5:
    print( f"A jegyed {jegy}-ös, gratulálok!" )
elif jegy == 4:
    print( f"A jegyed {jegy}-es, lehetne jobb is." )
elif jegy == 3:
    print( f"A jegyed {jegy}-as, elmegy." )
elif jegy == 2 or jegy == 1:
    print( f"A jegyed {jegy}-es, menj tanulni!" )
else:
    print( f"Olyan nem is létezik!" )