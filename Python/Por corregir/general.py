import numpy as np
import matplotlib.pyplot as plt
import sympy


def evaluar(funcion,varx):
    """Evalúa una función dependiente de X, dado un valor.

    Devuelve el valor de la función correspondiente, al susituir
    su variable independiente X, por un valor 

    Parámetros:
    funcion   -- Funcion dependiente de X, a encontrar su valor
    varx      -- Valor de la variable X, a sustituir en la función dada
   
    """    
    x,y,z = sympy.symbols ('x y z') #Define x,y,z como variables de una funcion
    y=sympy.sympify(funcion).subs(x,varx) #Evalua la funcion, indicado su variable y valor respectivo
    return float(y)



def calDerivada(funcion):
    """Determina la derivada de una función dependiente de X.

    Devuelve el valor de la función derivada respecto a X

    Parámetros:
    funcion   -- Funcion dependiente de X, a derivar
   
    """  
    x,y,z = sympy.symbols ('x y z')  #Define x,y,z como variables de una funcion
    y=sympy.sympify(funcion) #Convierte el string funcion, a tipo Fucnion
    return y.diff(x)   #diff= utilizado para derivar la funcion, respecto a X

def error(funcion,xk):
    """Formúla que da el error en el método de la Falsa Posicion

    Devuelve el valor del error en una iteración específica del
    método de la Falsa Posicion

    Parámetros:
    x1     -- Valor anterior de la iteración
    x      -- Valor siguiente de la iteración
   
    """   
    return evaluar(funcion,xk)

def imprimirResultado(iteraciones,valorAprox):
    print ("Numero de iteraciones que se utilizaron para aproximar el cero : " + str(iteraciones+1))
    print ("Aproximacion a la solucion de la ecuacion : " + str (valorAprox))

def graficar(listaX,listaY,nombre):
    """Gráfica de una ecuación no lineal mediante el método de Newton-Raphson.

    Parámetros:
    funcion -- Funcion dependiente de X, a cálcular su raíz
    listaX      -- Valor inicial dado
    listaY     -- Tolerancia miníma aceptada para encontrar la raíz
   
    """
    plt.plot(listaX, listaY)
    plt.title('Comportamiento del metodo de '+ nombre) 
    plt.xlabel('iteraciones')
    plt.ylabel('|f(Xaprox)|')
    plt.grid(True)
    plt.show()