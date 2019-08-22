import general as g

def getyk(funcion,xk,a):
    numerador= g.evaluar(xk)
    denominador=g.evaluar(g.calDerivada(xk))
    yk= xk - a*(numerador/denominador)
    return yk

def getxk(funcion,x):
    a=1
    a1=1
    a2=1
    b1=1
    b2=1  
    yk=getyk(funcion,x,a)
    fx=g.evaluar(x)
    fy=g.evaluar(yk)
    fdx=g.evaluar(g.calDerivada(x))
    operando1=fx/((a1*fx)+(a2*fy))
    operando2=((b1*fx)+(b2*fy))/fx
    xk=yk-(operando1+operando2)*(fy/fdx)
    return xk
    

def Ostrowski(funcion,x0,tol):
    """Resuelve una ecuación no lineal mediante el método de Ostrowski.

    a = b = c = 1 and d = 0; this is compared 
    with the classical Steffensen’s method
    
    Devuelve el valor de la raíz más aproximada según la tolerancia dada
    uno valor inicial x

    Parámetros:
    funcion -- Funcion dependiente de X, a cálcular su raíz
    x0      -- Valor inicial dado
    tol     -- Tolerancia miníma aceptada para encontrar la raíz
   
    """ 
    xk=getxk(funcion,x0)
    xk1=getxk(funcion,xk)
    k=0   #Corresponde a la iteración en que se encuentra
    while (g.error(xk1,xk)>=tol):  
        xk=getxk(funcion,xk)
        xk1=getxk(funcion,xk) 
        k+=2
    return k
    