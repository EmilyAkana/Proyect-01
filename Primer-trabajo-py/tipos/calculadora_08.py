"""calculadora"""

N1 = input("Ingresa primer nummero ")
N2 = input("ingresa segundo numero ")

N1 = int(N1)
N2 = int(N2)
print(N1 + N2)

SUMA = N1 + N2
RESTA = N1 - N2
MULT = N1 * N2
DIV = N1 / N2

MENSAJE = f"""
Para los numeros {N1} y {N2},
El resultado de la suma  es {SUMA}
EL resultado de la  resta es {RESTA}
El resultado de la multiplicación es {MULT}
El resultado de la division es {DIV}
"""
print(MENSAJE)
