%{
    Evalua una funcion dependiente de X para asi encontrar una aproximacion
    de una de sus raices.
<<<<<<< HEAD
    Recuperado de "Solving nonlinear problems by Ostrowski�Chun type
    parametric families"
   
    Autores "Alicia Cordero, Jos� L. Hueso, Eulalia Mart�nez, Juan R. Torregrosa"
    
=======
    Recuperado de "Steffensen type methods for solving nonlinear equations"
    ecuacion 4
    Autores "Alicia Cordero, José L. Hueso, Eulalia Martínez, Juan R. Torregrosa"
>>>>>>> 0fa3b44d14b8a3862dddd915a0c86f400c0cda11
    Retorna una lista donde sus elementos son el x aproximado y la cantidad de
    kciones necesarias para cumplir con la tolerancia dada
    parametros:
    funcion: funcion dependdiente de x a la cual se le quiere encontrar sus ceros
    x0: valor inicial para empezar a calcular las kciones
    tol: tolerancia aceptable para finalizar el metodo
    graf: parametro para indicar si se quiere generar la grafica
%}

function [xk, k, err] = sne_ud_2(funcion, x0, tol, graf)
    pkg load symbolic;
    t_func = strcat('@(x)', funcion);
    try
        f = str2func(t_func);
    catch
        xk = 0;
        k = 0;
        err = 'La Syntaxis de la funcion es incorrecta';
    end_try_catch
    
    xk=getxk(funcion,x0)
<<<<<<< HEAD
    k=1  #Corresponde a la kci�n en que se encuentra
=======
    k=1  #Corresponde a la iteración en que se encuentra
>>>>>>> 0fa3b44d14b8a3862dddd915a0c86f400c0cda11
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
<<<<<<< HEAD
##    Devuelve el valor del error en una kci�n espec�fica del
##    m�todo de la Falsa Posicion
=======
##    Devuelve el valor del error en una iteración específica del
##    método de la Falsa Posicion
>>>>>>> 0fa3b44d14b8a3862dddd915a0c86f400c0cda11
##
##    Parámetros:
##    a     -- Primer valor del intervalo dado
##    b     -- Segundo valor del intervalo dado
<<<<<<< HEAD
##    k     -- Valor la kci�n en la que se encuentra
=======
##    k     -- Valor la iteración en la que se encuentra
>>>>>>> 0fa3b44d14b8a3862dddd915a0c86f400c0cda11
    func=inline(funcion);
    err= func(x);
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
    fy=evaluar(funcion,yk);
    fdx=evaluar(calDerivada(funcion),x);
    operando1=fx/abs((a1*fx)+(a2*fy));
    operando2=((b1*fx)+(b2*fy))/abs(fx);
    xk=yk-(operando1+operando2)*(fy/abs(fdx));
endfunction
