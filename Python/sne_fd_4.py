import general as g
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
def getFZX(funcion,zk,xk):
    numerador= g.evaluar(funcion,zk) - g.evaluar(funcion,xk)
    denominador = zk - xk
    fzx=numerador/denominador 
    return fzx

def getzk(funcion,xk):
    fxk=g.evaluar(funcion,xk)
    zk= xk -fxk
    return zk

def getyk(funcion,xk):
    zk=getzk(funcion,xk)
    fxk=g.evaluar(funcion,xk)
    fzx=getFZX(funcion,zk,xk)
    yk= xk - (fxk/fzx)
    return yk

def getXk(funcion,xk):
    zk= getzk(funcion,xk)
    yk= getyk(funcion,xk)
    numerador=  g.evaluar(funcion,yk)
    denominador = getFZX(funcion,zk,xk)
    xk= yk - (numerador/denominador)
    return xk
    
def sne_fd_4(funcion,x0,tol,graf):
    """Version del metodo iterativo de Traub con a=b=c=1 y d =0
       Recuperado del documento "Low-complexity root-finding iteration functions with no
       derivatives of any order of convergence" 
       creado por "Alicia Cordero, Juan R. Torregrosa" 
   
   Intenta lograr valores de conversion mediante la ecuacion (6) del documento.
   Parametros: 
    1) funcion: Funcion en formato string en terminos de x la cual require la aproximacion
    2) x0: Valor inicial de la funcion necesario para las siguientes aproximaciones
    3) tol: Tolerancia al error maxima para el cÃ¡lculo de la aproximacion
    4) graf: Bandera para realizar o no el grafico de iteraciones vs aproximacion.
    Probado con x^3-4*x^2-10 usando x0 =1
    """ 
    x = sp.symbols('x')
    try:
        fun_sim = parse_expr(funcion)
    except:
        print ('Error de sintaxis')
    xk=getXk(funcion,x0)
    k=1  #Corresponde a la iteración en que se encuentra
    listaX=[0]
    listaY=[x0]
    listaY.append(xk)
    listaX.append(1)
    while (abs(g.error(funcion,xk))>=tol):  
        xk=getXk(funcion,xk)        
        xk1=getXk(funcion,xk) 
        listaY.append(xk)
        listaY.append(xk1)
        k+=2
        listaX.append(k-1)
        listaX.append(k)    
    if (graf==0):
        return g.imprimirResultado(listaX[-1],listaY[-1])
    else:
        print(listaX,listaY)
        g.imprimirResultado(listaX[-1],listaY[-1])
        return g.graficar(listaX,listaY,"Traub Method")