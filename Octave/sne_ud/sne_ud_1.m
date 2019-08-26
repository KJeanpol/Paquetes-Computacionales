%%    Evalua una funcion dependiente de X para asi encontrar una aproximacion
%%    de una de sus raices.
%%
%%    Recuperado de "Geometric constructions of iterative functions to solve
%%        nonlinear equations"    
%%    Autores "S.Amat, S.Busquier, J.M. Guti"
%%
%%    Retorna una lista donde sus elementos son el x aproximado y la cantidad de
%%    iteraciones necesarias para cumplir con la tolerancia dada
%%
%%    parametros:
%%    fstr: funcion dependdiente de x a la cual se le quiere encontrar sus ceros
%%    x0: valor inicial para empezar a calcular las iteraciones
%%    tol: tolerancia aceptable para finalizar el metodo
%%    graf: parametro para indicar si se quiere generar la grafica
%%
%%    sne_ud_1('x**2-4*x+4', 5, 0.00001, 1)

function [xAprox, iter, err] = sne_ud_1(func, x0, tol, graf)
    pkg load symbolic;
    syms x;
    t_func = strcat('@(x)', func);
    try
        f = str2func(t_func);
    catch
        xAprox = 0;
        itera = 0;
        err = 'La Syntaxis de la funcion es incorrecta';
    end_try_catch
    fp = matlabFunction(diff(f, x));
    itera = 0;
    xAprox = 0;
    xAprox = x0;
    xAx = [];
    yAx = [];
    while (abs(f(xAprox)) >= tol)
        xAx = [xAx itera];
        yAx = [yAx f(xAprox)];
        try
            fpxn = 1/f(xAprox);
            fpxn = fpxn**(-1);
        catch
            break
        end_try_catch
        fxn = f(xAprox);
        Lfxn = Lf(func, xAprox);
        xAprox = xAprox - (1+0.5*(Lfxn/(1-Lfxn)))*(fxn/fpxn);
        itera = itera + 1;
    end
    if (graf)
        plot(xAx, yAx);
        err = 'terminado con exito';
    else
        err = 'terminado con exito';
    end
endfunction