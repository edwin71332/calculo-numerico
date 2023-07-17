#Edwin Rodríguez
#CI: 29668894
from math import *
def f(x):
    return sin(x) - e**(-x);
def df(x):
    return cos(x) + e**(-x);

def newton_raphson(f, x0, tol, max_iter):
    
     
    
    xi = x0  
    iteraciones = 0
    raiz = 0
    error = 100
    
    while (iteraciones < max_iter and error > tol ):
        xi1 = xi - f(xi)/df(xi)
        error = abs((xi1 - xi)/xi1)
        if error < tol:          
            raiz = xi1      
        xi = xi1          
        iteraciones += 1
    print(f"La raíz encontrada es:",raiz)
    print("el error es:",error)

x0 = float(input("Ingrese la aproximación inicial xi:"))      
tol = float(input("Ingrese la tolerancia deseada: "))        
max_iter = int(input("Ingrese el número máximo de iteraciones permitidas: "))

newton_raphson(f, x0, tol, max_iter)
   
