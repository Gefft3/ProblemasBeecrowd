valor = input().split()

a, b, c = valor
pi = 3.14159

AT = (float(a) * float(c))/2
AC = pi * (float(c)* float(c))
ATR = float(c) *(float(a) + float(b))/2
AQ = float(b) * float(b)
AR = float(a) * float(b)
print(f"TRIANGULO: {AT:.3f}")
print(f"CIRCULO: {AC:.3f}")
print(f"TRAPEZIO: {ATR:.3f}")
print(f"QUADRADO: {AQ:.3f}")
print(f"RETANGULO: {AR:.3f}")