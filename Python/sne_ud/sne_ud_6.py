import general as g
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
def getyk(funcion,xk,a):
    numerador= g.evaluar(funcion,xk)
    denominador=g.evaluar(g.calDerivada(funcion),xk)
    yk= xk - a*(numerador/abs(denominador))
    return yk

def getxk(funcion,x):
    a=1
    a1=1
    a2=1
    b1=1
    b2=1  
    yk=getyk(funcion,x,a)
    fx=g.evaluar(funcion,x)
    fy=g.evaluar(funcion,yk)
    fdx=g.evaluar(g.calDerivada(funcion),x)
    operando1=fx/abs((a1*fx)+(a2*fy))
    operando2=((b1*fx)+(b2*fy))/abs(fx)
    xk=yk-(operando1+operando2)*(fy/abs(fdx))
    return xk
    
def sne_ud_6(funcion,x0,tol,graf):
    """ Version del metodo iterativo Ostrowski–Chun, con un valor de alfa = alfa1 = beta1= beta =1
        Recuperado del documento "Solving nonlinear problems by Ostrowski–Chun type
        parametric families" creado por 
   Alicia Cordero, Javier G. Maimó Juan R. Torregrosa · María P. Vassileva. 
   
   Intenta lograr valores de conversion mediante la ecuacion (5) del documento.
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
    xk=getxk(funcion,x0)
    k=1  #Corresponde a la iteración en que se encuentra
    listaX=[0]
    listaY=[x0]
    listaY.append(xk)
    listaX.append(1)
    while (g.error(funcion,xk)>=tol):  
        xk=getxk(funcion,xk)
        xk1=getxk(funcion,xk) 
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
        return g.graficar(listaX,listaY,"Ostrowski")
    