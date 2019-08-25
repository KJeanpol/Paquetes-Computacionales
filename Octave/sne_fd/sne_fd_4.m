%{
    Evalua una funcion dependiente de X para asi encontrar una aproximacion
    de una de sus raices.
    
    Recuperado de "Steffensen type methods for solving nonlinear equations"
    ecuacion 4
    
    Autores "Alicia Cordero, Jos� L. Hueso, Eulalia Mart�nez, Juan R. Torregrosa"
    
    Retorna una lista donde sus elementos son el x aproximado y la cantidad de
    iteraciones necesarias para cumplir con la tolerancia dada
    parametros:
    fstr: funcion dependdiente de x a la cual se le quiere encontrar sus ceros
    x0: valor inicial para empezar a calcular las iteraciones
    tol: tolerancia aceptable para finalizar el metodo
    graf: parametro para indicar si se quiere generar la grafica
%}

function [xAprox, itera, err] = sne_fd_4(funcion, x0, tol, graf)
    xk=getxk(funcion,x0);
    k=1;  #Corresponde a la iteraci�n en que se encuentra
    listaX=[];
    listaY=[];
    listaX=[listaX 0];
    listaY=[listaX x0];
    listaY=[listaY xk];
    listaX=[listaX 1];
    while (abs(error(funcion,xk))>=tol)  
        xk=getxk(funcion,xk)        
        xk1=getxk(funcion,xk)   
        listaY=[listaY xk]
        listaY=[listaY xk1]
        k+=2
        listaX=[listaX (k-1)]
        listaX=[listaX k]
    endwhile 
    listaX=[listaX (k+1)]
    if (graf)
        plot(listaX, listaY)
    else
        disp('Metodo finalizado')
    endif
endfunction

function resultado = evaluar(funcion,varx)
##    Eval�a una funci�n dependiente de X, dado un valor.
##
##    Devuelve el valor de la funci�n correspondiente, al susituir
##    su variable independiente X, por un valor 
##
##    Par�metros:
##    funcion   -- Funcion dependiente de X, a encontrar su valor
##    varx      -- Valor de la variable X, a sustituir en la funci�n dada
##        
    func=inline(funcion);
    resultado= func(varx);
endfunction   

function err= error(funcion,x)
##    Form�la que da el error en el m�todo de Bisecci�n
##
##    Devuelve el valor del error en una iteraci�n espec�fica del
##    m�todo de la Falsa Posicion
##
##    Par�metros:
##    a     -- Primer valor del intervalo dado
##    b     -- Segundo valor del intervalo dado
##    k     -- Valor la iteraci�n en la que se encuentra
    func=inline(funcion);
    err= func(x);
endfunction


function yk= getyk(funcion,xk)   
    zk=getzk(funcion,xk);
    numerador= (evaluar(funcion,xk))**2;
    denominador=evaluar(funcion,zk)-evaluar(funcion,xk);
    yk= abs(xk- (numerador/(denominador)));
endfunction

function zk = getzk(funcion,xk)
    zk=xk + evaluar(funcion,xk);
endfunction

function xk = getxk(funcion,x)
    a=1;
    b=1;
    c=1;
    d=0;
    yk=getyk(funcion,x);
    zk=getzk(funcion,x);
    operando1= (a*evaluar(funcion,yk)-b*evaluar(funcion,zk))/abs(yk-zk);
    operando2= (c*evaluar(funcion,yk)-(d*evaluar(funcion,x)))/abs(yk-x);
    numerador=evaluar(funcion,yk);
    denominador=operando1+operando2;
    xk=yk-(numerador/abs(denominador));
endfunction