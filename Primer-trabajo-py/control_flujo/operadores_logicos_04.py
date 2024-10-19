"""And, or, not"""

ESPADA = True
ESCUDO = False

if ESPADA and ESCUDO:
    print("Puedes ver al gran arbol deku.")
elif ESPADA or ESCUDO:
    print("Ya tienes uno, consigue el otro.")
else:
    print("Sin una espada y un escudo no te dejare pasar.")
