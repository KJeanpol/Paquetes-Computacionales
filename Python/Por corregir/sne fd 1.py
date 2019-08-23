import numpy as np
import matplotlib.pyplot as plt
import sympy
import general as g
import math

def sne_fd_1(funcion,x0,x1,tol):
    
    """Resuelve una ecuación no lineal mediante el método de la Muller-Biseccion.

    Devuelve el valor de la raíz más aproximada según la tolerancia dada
    en un intervalo [x0,x1]

    Parámetros:
    funcion -- Funcion dependiente de X, a cálcular su raíz
    x0      -- Primer valor del intervalo a resolver
    x1      -- Segundo valor del intervalo a resolver
    tol     -- Tolerancia miníma aceptada para encontrar la raíz
   
    """    
    xr=x0
    a=x0
    b=x1
    k=1
    if (balzano (funcion, x0, x1) <0 ):
        while (error(a,b,k)>=tol):  
            xr=(x0+x1)/2
            if (evaluar(funcion,x0)*evaluar(funcion,xr)<0):
                x1=xr
            else:
                x0=xr
            k+=1
        return (x0+x1)/2
    else:
        return "No existe raíz"

def getCValue(ak,bk):
    c = ak + (bk-ak)/2
    return c
    
def balzano (funcion, x0, x1):
    return g.evaluar(funcion,x0) * g.evaluar(funcion,x1)

def getCkValue(A,B,C,x2):
    
    raiz  math.sqrt(pow(B,2)-(4*A*C))
    ck= x2- (-2*C)/(B+raiz)  #Como hago el mas menos B ?
    return ck

def getA(x0,x1,x2):
    numerador = (x1-x2)*(g.evaluar(x0)-g.evaluar(x2)) - (x0-x2)*(g.evaluar(x1)-g.evaluar(x2))
    denominador= (x0-x2)*(x1-x2)*(x0-x1)
    return numerador/denominador
    
def getB(x0,x1,x2):
    numerador = pow((x0-x2),2)*(g.evaluar(x1)-g.evaluar(x2)) - pow((x1-x2),2)*(g.evaluar(x1)-g.evaluar(x2))
    denominador= (x0-x2)*(x1-x2)*(x0-x1)
    return numerador/denominador

def getC(x2):
    return g.evaluar(x2)