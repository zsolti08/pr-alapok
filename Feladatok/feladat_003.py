# feladat_003
# dk9 95 old.

print( "Szevasz!" )
évek_száma = int(input( "Hány éves vagy? " ))
if évek_száma == 0:
    print( f"Még meg se születtél" )
elif évek_száma < 6:
    print( f"{évek_száma} éves vagy, még nem jársz általános iskolába" )
elif évek_száma >= 6 and évek_száma <= 14:
    print( f"{évek_száma} éves vagy, általános iskolába jársz" )
elif évek_száma > 14 and évek_száma < 65:
    print( f"{évek_száma} éves vagy, még tanulsz vagy már dolgozol" )
else:
    print( f"{évek_száma} éves vagy, már nyugdíjas vagy" )