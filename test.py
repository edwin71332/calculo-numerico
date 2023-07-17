import unittest
from biseccion import *
from Newton_Raphson import*
from  integracion_numerica import*
from metodo_euler import*

class MyTest(unittest.TestCase):
    def test_algoritmo_biseccion(self):
        a = 0
        b = 1
        es = 0.01
        ni = 10
        resultado_esperado = 0.58984375

        resultado_obtenido = algoritmo_biseccion(a, b, es, ni)

        self.assertAlmostEqual(resultado_obtenido, resultado_esperado, places=8)
    
    def test_newton_raphson(self):
        x0 = 0.5
        tol = 0.02
        max_iter = 10
        
        raiz_esperada = 0.5885294126263548
        
        # Llamada a la función newton_raphson
        raiz = newton_raphson(f, df, x0, tol, max_iter)
        
        # Verificar si la raíz encontrada es igual a la raíz esperada
        self.assertAlmostEqual(raiz, raiz_esperada, places=10)        
    
    def test_suma_riemann(self):
        a = 0
        b = 1
        n = 5
        resultado_esperado = 0.43146135109221634
        
        # Llamada a la función suma_riemann
        resultado = suma_riemann(f, a, b, n)
        
        # Verificar si el resultado obtenido es igual al resultado esperado
        self.assertAlmostEqual(resultado, resultado_esperado, places=6)
    
    def test_trapecio(self):
        a = -1
        b = 1
        n = 5
        resultado_esperado = 1.156066874258427
        
        # Llamada a la función trapecio
        resultado = trapecio(f2, a, b, n)
        
        # Verificar si el resultado obtenido es igual al resultado esperado
        self.assertAlmostEqual(resultado, resultado_esperado, places=6)

 
     def test_metodo_euler(self):
     	pass

if __name__ == '__main__':
    unittest.main()