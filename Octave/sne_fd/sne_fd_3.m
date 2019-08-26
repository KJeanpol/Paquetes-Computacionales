%%   Version del metodo iterativo de Traub
%%   Recuperado del documento "Low-complexity root-finding iteration functions with no
%%   derivatives of any order of convergence" creado por "Alicia Cordero, Juan R. Torregrosa" 
%%   Intenta lograr valores de conversion mediante la ecuacion (2) del documento.
%%   Parametros: 
%%    1) funcion: Funcion en formato string en terminos de x la cual require la aproximacion
%%    2) x0: Valor inicial de la funcion necesario para las siguientes aproximaciones
%%    3) tol: Tolerancia al error maxima para el cÃ¡lculo de la aproximacion
%%    4) graf: Bandera para realizar o no el grafico de iteraciones vs aproximacion.
%%   Probado con x^3-4*x^2-10 usando x0 =1
function [xAprox, itera, err] = sne_fd_3(funcion, x0, tol, graf)
    t_func = strcat('@(x)', funcion);
    try
        f = str2func(t_func);
    catch
        xAprox = 0;
        itera = 0;
        err = 'La Syntaxis de la funcion es incorrecta';
    end_try_catch
    xk=getXk(funcion,x0);
    k=1;  %%Corresponde a la iteración en que se encuentra
    listaX=[];
    listaY=[];
    xi=x0;
    listaX=[listaX 0];
    listaY=[listaY xi];
    listaX=[listaX 1];  
    listaY=[listaY xk];
    while (abs(error(funcion,xk))>=tol)  
        xk=getXk(funcion,xk);      
        xk1=getXk(funcion,xk);
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

function fzx = getFZX(funcion,zk,xk)
    numerador= evaluar(funcion,zk) - evaluar(funcion,xk);
    denominador = zk - xk;
    fzx=numerador/denominador ;
endfunction

function zk =getzk(funcion,xk);
    fxk=evaluar(funcion,xk);
    zk= xk -fxk;
endfunction

function yk = getyk(funcion,xk)
    zk=getzk(funcion,xk);
    fxk=evaluar(funcion,xk);
    fzx=getFZX(funcion,zk,xk);
    yk= xk - (fxk/fzx);
endfunction

function xk = getXk(funcion,xk)
    zk= getzk(funcion,xk);
    yk= getyk(funcion,xk);
    numerador=  evaluar(funcion,yk);
    denominador = getFZX(funcion,zk,xk);
    xk= yk - (numerador/denominador);
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
