%%   Version del metodo iterativo de Steffensen con a=b=c=1 y d =0
%%   Recuperado del documento "A class of Steffensen type methods with optimal order of convergence" 
%%   creado por "Alicia Cordero, Juan R. Torregrosa" 
%%   Intenta lograr valores de conversion mediante la ecuacion (6) del documento.
%%   Parametros: 
%%    1) funcion: Funcion en formato string en terminos de x la cual require la aproximacion
%%    2) x0: Valor inicial de la funcion necesario para las siguientes aproximaciones
%%    3) tol: Tolerancia al error maxima para el cÃ¡lculo de la aproximacion
%%    4) graf: Bandera para realizar o no el grafico de iteraciones vs aproximacion.
%%   Probado con x^3-4*x^2-10 usando x0 =1
function [xAprox, itera, err] = sne_fd_4(funcion, x0, tol, graf)
    xk=getxk(funcion,x0);
    k=1;  %%Corresponde a la iteración en que se encuentra
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
%%    Evalúa una función dependiente de X, dado un valor.
%%
%%    Devuelve el valor de la función correspondiente, al susituir
%%    su variable independiente X, por un valor 
%%
%%    Parámetros:
%%    funcion   -- Funcion dependiente de X, a encontrar su valor
%%    varx      -- Valor de la variable X, a sustituir en la función dada
%%        
    func=inline(funcion);
    resultado= func(varx);
endfunction   

function err= error(funcion,x)
%%    Formúla que da el error en el método de Bisección
%%
%%    Devuelve el valor del error en una iteración específica del
%%    método de la Falsa Posicion
%%
%%    Parámetros:
%%    a     -- Primer valor del intervalo dado
%%    b     -- Segundo valor del intervalo dado
%%    k     -- Valor la iteración en la que se encuentra
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