import general as g

def getyk(funcion,xk):
    
    zk=getzk(funcion,xk)
    numerador= pow(g.evaluar(xk),2)
    denominador=g.evaluar(zk)-g.evaluar(xk)
    yk=xk- (numerador/denominador)
    return yk

def getzk(funcion,xk):
    zk=xk + g.evaluar(xk)
    return zk

def getxk(funcion,x):
    a=1
    b=1
    c=1
    d=1
    yk=getyk(funcion,x)
    zk=getzk(funcion,x)
    operando1= (a*g.evaluar(yk)-b*g.evaluar(zk))/(yk-zk)
    operando2= (c*g.evaluar(yk)-d*g.evaluar(x))/(yk-x)
    numerador=g.evaluar(yk)
    denominador=operando1+operando2
    xk=numerador/denominador
    return xk
    

def Steffensen(funcion,x0,tol):
    """Resuelve una ecuación no lineal mediante el método de Steffensen–Newton.

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
    