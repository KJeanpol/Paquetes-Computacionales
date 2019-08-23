import general as g

def getyk(funcion,xk):
    
    zk=getzk(funcion,xk)
    numerador= pow(g.evaluar(funcion,xk),2)
    denominador=g.evaluar(funcion,zk)-g.evaluar(funcion,xk)
    yk= xk- (numerador/(denominador))
    return abs(yk)

def getzk(funcion,xk):
    zk=xk + g.evaluar(funcion,xk)
    return zk

def getxk(funcion,x):
    a=1
    b=1
    c=1
    d=0
    try:
        yk=getyk(funcion,x)
        zk=getzk(funcion,x)
        operando1= (a*g.evaluar(funcion,yk)-b*g.evaluar(funcion,zk))/abs(yk-zk)
        operando2= (c*g.evaluar(funcion,yk)-(d*g.evaluar(funcion,x)))/abs(yk-x)
        numerador=g.evaluar(funcion,yk)
        denominador=operando1+operando2
        xk=yk-(numerador/abs(denominador))
        return xk
    except:
        return True

def Steffensen(funcion,x0,tol,graf):
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
    k=1  #Corresponde a la iteración en que se encuentra
    listaX=[0]
    listaY=[x0]
    listaY.append(xk)
    listaX.append(1)
    while (g.error(funcion,xk)>=tol):  
        print("Entre")
        xk=getxk(funcion,xk)        
        xk1=getxk(funcion,xk) 
        if (xk1==True):
            break
        else:     
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