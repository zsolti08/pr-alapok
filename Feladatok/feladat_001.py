# feladat_001

"""
Kérjük be a billyentyűzetről a nevünket, és írassuk ki a képernyőre!
A billentyűzetről mindig szöveget (string-et) olvasunk be!
type(változó)
"""

"""
nev = input("Kérek egy nevet: ")
print(f"A megadott név a következő: {nev}")
"""

vnev = input( f"Kérek egy vezetéknevet: " )
knev = input( f"Kérek egy keresztnevet: " )
print(f"Szia {vnev} {knev}!")
print(f"A vezetéknév változó típusa: {type(vnev)}")
print(f"A keresztnév változó típusa: {type(knev)}")