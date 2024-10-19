"""Ejercicio de prueba conndicional if"""

EDAD = int(input("ingrese  su edad "))
if EDAD < 16:
    print("No puedes ver la pelicula")

elif EDAD > 55:
    print("Viene con descuento del 5%")
else:
    print("Puedes ver la pelicula")
print("")
print("Tenga un buen dia")
