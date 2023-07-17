#Edwin Rodríguez
#CI: 29668894
from math import *
def f(x):
    return x *cos(x)

def suma_riemann(f, a, b, n):
    h = (b - a) / n
    acum = 0
    for i in range(n+1):
        x = a + i * h
        acum += h * f(x)
    return acum

a = 0  # límite inferior del intervalo
b = 1  # límite superior del intervalo
n = 5  # número de subintervalos

resultado = suma_riemann(f, a, b, n)

print(f"La suma de Riemann de la función f(x) = x*cos(x) en el intervalo [{a}, {b}] con {n} subintervalos es {resultado}")

def f2(x):
    return sqrt(x + 1)

def trapecio(f2, a, b, n):
    h = (b - a) / n
    suma = (f2(a) + f2(b)) / 2
    for i in range(1, n):
        x = a + i * h
        suma += f2(x)
    return h * suma

a = -1  # límite inferior del intervalo
b =  1  # límite superior del intervalo
n = 5  # número de subintervalos

resultado = trapecio(f2, a, b, n)

print(f"La integral de la función f(x) sqrt(x+1) en el intervalo [{a}, {b}] con el método del trapecio y {n} subintervalos es {resultado}")