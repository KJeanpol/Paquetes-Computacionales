import general as g

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
    
def Ostrowski(funcion,x0,tol,graf):
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
    