%%   Version del metodo iterativo Ostrowski–Chun, con un valor de alfa = alfa1 = beta1= beta =1
%%   Recuperado del documento "Solving nonlinear problems by Ostrowski–Chun type
%%   parametric families" creado por 
%%   Alicia Cordero, Javier G. Maimó Juan R. Torregrosa · María P. Vassileva. 
%%   Intenta lograr valores de conversion mediante la ecuacion (5) del documento.
%%   Parametros: 
%%    1) funcion: Funcion en formato string en terminos de x la cual require la aproximacion
%%    2) x0: Valor inicial de la funcion necesario para las siguientes aproximaciones
%%    3) tol: Tolerancia al error maxima para el cÃ¡lculo de la aproximacion
%%    4) graf: Bandera para realizar o no el grafico de iteraciones vs aproximacion.
%%   Probado con x^3-4*x^2-10 usando x0 =1
function [xk, k, err] = sne_ud_2(funcion, x0, tol, graf)
    t_func = strcat('@(x)', funcion);
    try
        f = str2func(t_func);
    catch
        xk = 0;
        k = 0;
        err = 'La Syntaxis de la funcion es incorrecta';
    end_try_catch
    
    xk=getxk(funcion,x0)

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
     
    func=inline(funcion);
    resultado= func(varx);
 endfunction   

 
function derivada = calDerivada(funcion,varx)
       
    syms x;
    f=inline(funcion);
    derivada=char(diff(funcion,x));
 endfunction   
 
function err= error(funcion,x)


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
