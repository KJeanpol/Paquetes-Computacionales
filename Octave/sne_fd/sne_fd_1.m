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


function [xAprox, itera, err] = sne_fd_1(fstr, x0, tol, graf)
    t_func = strcat('@(x)', fstr);
    try
        f = str2func(t_func);
    catch
        xAprox = 0;
        itera = 0;
        err = 'La Syntaxis de la funcion es incorrecta';
    end_try_catch
    yn = x0 - ((2*f(x0)**2)/((f(x0+f(x0)))-(f(x0-f(x0)))));
    xn = x0 - ((2*f(x0)**2)/((f(x0+f(x0)))-(f(x0-f(x0)))))*((f(yn)-f(x0))/(2*f(yn)-f(x0)));
    itera = 0;
    xAx = [];
    yAx = [];
    while (abs(f(xn)) >= tol)
        xAx = [xAx itera];
        yAx = [yAx abs(f(xAprox))]; % revisar
        try
            denominador1 = 1/(f(xn+f(xn)) - f(xn-f(xn)))
            denominador1 = denominador1**(-1)
        catch
            break
        end_try_catch
        yn = xn - ((2*f(xn)**2)/denominador1)
        try
            denominador2 = 1/(2*f(yn)-f(xn))
            denominador2 = denominador2**(-1)
        catch
            break
        end_try_catch
        xn = xn - ((2*f(xn)**2)/denominador1)*((f(yn)-f(xn))/denominador2)
        itera = itera + 1
    end
    if (graf)
        plot(xAx, yAx)
    else
        disp('Metodo finalizado')
    end
endfunction
