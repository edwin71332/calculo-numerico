#Edwin Rodríguez
#CI: 29668894
import unittest
from math import cos, sqrt
from algoritmo_biseccion import algoritmo_biseccion
from newton_raphson import newton_raphson
from falsa_posicion import falsa_posicion
from integracion_numerica import suma_riemann, trapecio

class TestAlgoritmos(unittest.TestCase):
    
    def test_algoritmo_biseccion(self):
        a = 0
        b = 1
        es = 0.01
        ni = 10
        result = algoritmo_biseccion(a, b, es, ni)
        self.assertAlmostEqual(result[0], 0.703125)
        self.assertAlmostEqual(result[1], 0.417910447761194)
        self.assertEqual(result[2], 5)
        
    def test_newton_raphson(self):
        x = Symbol('x')
        f = sin(x) - e**(-x)
        x0 = 1
        tol = 0.0001
        max_iter = 10
        newton_raphson(f, x0, tol, max_iter)
        raiz_esperada = 0.56714329
        error_esperado = 0.00000000000001
        self.assertAlmostEqual(newton_raphson(f, x0, tol, max_iter)[0], raiz_esperada, places=7)
        self.assertAlmostEqual(newton_raphson(f, x0, tol, max_iter)[1], error_esperado, places=14)
        
   
    def test_suma_riemann(self):
        f = lambda x: x * cos(x)
        a = 0
        b = 1
        n = 5
        resultado = suma_riemann(f, a, b, n)
        self.assertAlmostEqual(resultado, 0.0644980307606)
        
    def test_trapecio(self):
        f2 = lambda x: sqrt(x + 1)
        a = -1
        b = 1
        n = 5
        resultado = trapecio(f2, a, b, n)
        self.assertAlmostEqual(resultado, 1.78179607048)

if __name__ == '__main__':
    unittest.main()