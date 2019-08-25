%{
    Evalua una funcion dependiente de X para asi encontrar una aproximacion
    de una de sus raices.
    Recuperado de "Steffensen type methods for solving nonlinear equations"
    ecuacion 4
    Autores "Alicia Cordero, José L. Hueso, Eulalia Martínez, Juan R. Torregrosa"
    Retorna una lista donde sus elementos son el x aproximado y la cantidad de
    iteraciones necesarias para cumplir con la tolerancia dada
    parametros:
    fstr: funcion dependdiente de x a la cual se le quiere encontrar sus ceros
    x0: valor inicial para empezar a calcular las iteraciones
    tol: tolerancia aceptable para finalizar el metodo
    graf: parametro para indicar si se quiere generar la grafica
%}

function [xAprox, itera, err] = sne_fd_4(fstr, x0, tol, graf)
    t_func = strcat('@(x)', fstr);
    try
        f = str2func(t_func);
    catch
        xAprox = 0;
        itera = 0;
        err = 'La Syntaxis de la funcion es incorrecta';
    end_try_catch
    
    xk=getxk(funcion,x0)
    k=1  #Corresponde a la iteración en que se encuentra
    listaX=[0];
    listaY=[x0];
    listaY=[listaY xk];
    listaX=[listaX 1];
    while (error(funcion,xk)>=tol) 
        xk=getxk(funcion,xk);
        xk1=getxk(funcion,xk); 
        listaY=[listaY xk];
        listaY=[listaY xk1];
        k+=2;
        listaX=[listaX k-1];
        listaX=[listaX k];
    endwhile
     
    if (graf)
        plot(listaX, listaY)
    else
        disp('Metodo finalizado')
    end
endfunction


function resultado = evaluar(funcion,varx)
##    Evalúa una función dependiente de X, dado un valor.
##
##    Devuelve el valor de la función correspondiente, al susituir
##    su variable independiente X, por un valor 
##
##    Parámetros:
##    funcion   -- Funcion dependiente de X, a encontrar su valor
##    varx      -- Valor de la variable X, a sustituir en la función dada
##        
    func=inline(funcion);
    resultado= func(varx);
 endfunction   

 
function derivada = calDerivada(funcion,varx)
##    Evalúa una función dependiente de X, dado un valor.
##
##    Devuelve el valor de la función correspondiente, al susituir
##    su variable independiente X, por un valor 
##
##    Parámetros:
##    funcion   -- Funcion dependiente de X, a encontrar su valor
##    varx      -- Valor de la variable X, a sustituir en la función dada
##        
    syms x;
    f=inline(funcion);
    derivada=char(diff(funcion,x));
 endfunction   
 
function err= error(funcion,x)
##    Formúla que da el error en el método de Bisección
##
##    Devuelve el valor del error en una iteración específica del
##    método de la Falsa Posicion
##
##    Parámetros:
##    a     -- Primer valor del intervalo dado
##    b     -- Segundo valor del intervalo dado
##    k     -- Valor la iteración en la que se encuentra
    func=inline(funcion);
    err= func(varx);
endfunction



function yk = getyk(funcion,xk,a)
    numerador= evaluar(funcion,xk);
    denominador=evaluar(calDerivada(funcion),xk);
    yk= xk - a*(numerador/abs(denominador));
endfunction

function xk = getxk(funcion,x)
    a=1;
    a1=1;
    a2=1;
    b1=1;
    b2=1  ;
    yk=getyk(funcion,x,a);
    fx=evaluar(funcion,x);
    fy=valuar(funcion,yk);
    fdx=evaluar(calDerivada(funcion),x);
    operando1=fx/abs((a1*fx)+(a2*fy));
    operando2=((b1*fx)+(b2*fy))/abs(fx);
    xk=yk-(operando1+operando2)*(fy/abs(fdx));
endfunction
