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

def sne_fd_3(funcion,x0,tol,graf):
    """ Version del metodo iterativo de Traub con a=b=c=1 y d =0
        Recuperado del documento "A class of Steffensen type methods with optimal order of convergence" 
        creado por "Alicia Cordero, Juan R. Torregrosa" 
   Intenta lograr valores de conversion mediante la ecuacion (6) del documento.
   Parametros: 
    1) funcion: Funcion en formato string en terminos de x la cual require la aproximacion
    2) x0: Valor inicial de la funcion necesario para las siguientes aproximaciones
    3) tol: Tolerancia al error maxima para el cÃ¡lculo de la aproximacion
    4) graf: Bandera para realizar o no el grafico de iteraciones vs aproximacion.
   Probado con x^3-4*x^2-10 usando x0 =1   
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
        return g.graficar(listaX,listaY,"Steffensen")