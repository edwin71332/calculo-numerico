#Edwin Rodríguez
#CI: 29668894
from math import *
def f(x):
    return sin(x)-pow(e,-x);

def algoritmo_biseccion(a,b,es,ni):
    ea=100 #error aproximado relativo
    i=0 #contador del numero de iteraciones
    m_actual=0 #punto medio actual
    m_previa=0 #punto medio previo

    if(f(a)*f(b)>0):
        print('no ha habido un cambio de signo');

    while(i<ni and ea>es):
        m_previa = m_actual;
        m_actual = (a+b)/2;
        
        if(f(m_actual)*f(b)<0):
            a=m_actual;
        else:
            b = m_actual;
        
        if(i>1):
            ea = abs((m_actual-m_previa)/m_actual);
        i=i+1;
    
    print("punto medio actual=",m_actual);
    print("error relativo aproximado=",ea);
    print("numero de iteraciones=",i);

a = int(input("ingrese el primer intervalo: "));
b = int(input("ingrese el segundo intervalo: "));
es = float(input("ingrese el error relativo: "));
ni = int(input("ingrese el numero de iteraciones: "));
print("_____________________________________________________");
print("");
algoritmo_biseccion(a,b,es,ni)
