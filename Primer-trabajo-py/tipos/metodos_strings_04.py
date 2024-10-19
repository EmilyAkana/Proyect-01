"""Modelos Strings"""

VARIABLE01 = "  pepe El mago  "
print(VARIABLE01.strip().capitalize())
print(VARIABLE01.lower())
print(VARIABLE01.upper())
print(VARIABLE01.title())
print(VARIABLE01.find("ma"))
print(VARIABLE01.replace("go", "il"))
print("ma" in VARIABLE01)
print("ma" not in VARIABLE01)

# no solo existe el tag strip, tambien existe lstrip y rstrip.
# R equivalente a right, osea derecha, y L representando left, osea izquierda
