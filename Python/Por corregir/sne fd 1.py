import general as g

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
    
def Trub(funcion,x0,tol,graf):
    """Resuelve una ecuación no lineal mediante el método de Ostrowski.

    a = b = c = 1 and d = 0; this is compared 
    with the classical Steffensen’s method
    
    Devuelve el valor de la raíz más aproximada según la tolerancia dado
    un valor inicial x

    Parámetros:
    funcion -- Funcion dependiente de X, a cálcular su raíz
    x0      -- Valor inicial dado
    tol     -- Tolerancia miníma aceptada para encontrar la raíz
   
    """ 
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
        return g.graficar(listaX,listaY,"Low-complexity root-finding iteration")