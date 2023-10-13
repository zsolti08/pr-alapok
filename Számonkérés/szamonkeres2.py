#Vécsei Zsolt 10.C számonkérés 2023. 10. 13.

jegy = int(input( f"Kérek egy jegyet 1-5-ig: " ))

if jegy == 1:
    print( f"A jegyed {jegy}-es, elégtelen!" )
elif jegy == 2:
    print( f"A jegyed {jegy}-es, elégséges!" )
elif jegy == 3:
    print( f"A jegyed {jegy}-as, közepes!" )
elif jegy == 4:
    print( f"A jegyed {jegy}-es, jó!" )
elif jegy == 5:
    print( f"A jegyed {jegy}-ös, jeles!" )
else:
    print( f"A jegyed {jegy}, ami nem megfelelő!" )