%{
Evalua una funcion dependiente de X para asi encontrar una aproximacion
de una de sus raices.

Recuperado de "A general class of four parametric with- and without
memory iterative methods for nonlinear equations"
Ecuacion: la primera ecuación que aparece 
Autores "Fiza Zafar1, Alicia Cordero, Juan R. Torregrosa"
Retorna una lista donde sus elementos son el x aproximado y la cantidad de
iteraciones necesarias para cumplir con la tolerancia dada

Parametros:
fstr: funcion dependdiente de x a la cual se le quiere encontrar sus ceros
x0: valor inicial para empezar a calcular las iteraciones
p0: valor inicial para emperzar a calcular las iteraciones
tol: tolerancia aceptable para finalizar el metodo
graf: parametro para indicar si se quiere generar la grafica

PRUEBA sne_fd_5('x**2', 2, 1, 0.0001, 1)
%}
disp('')
function [xAprox, iter, err] = sne_fd_5(func, x0, p0, tol, graf)
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
    
  listax=[1000 1000];
  listay=[1000 1000];  
 
  retorno = metodo_interactivo5(f, x0, 0, p0, tol, 0, listax, listay, graf)
  xAprox = retorno(1);
  iter = retorno(2);
  err = 'Se terminó correctamente'
endfunction
    
%{
Evalua una funcion dependiente de X para asi encontrar una aproximacion
de una de sus raices.

Recuperado de "A general class of four parametric with- and without
memory iterative methods for nonlinear equations"
Ecuacion: la primera ecuación que aparece 
Autores "Fiza Zafar1, Alicia Cordero, Juan R. Torregrosa"
Retorna una lista donde sus elementos son el x aproximado y la cantidad de
iteraciones necesarias para cumplir con la tolerancia dada

Parametros:
fstr: funcion dependdiente de x a la cual se le quiere encontrar sus ceros
x0: valor inicial para empezar a calcular las iteraciones
p0: valor inicial para emperzar a calcular las iteraciones
tol: tolerancia aceptable para finalizar el metodo
graf: parametro para indicar si se quiere generar la grafica

PRUEBA sne_fd_5('x**2', 2, 1, 0.0001,1)
%}
function [xn, iteracion, err] = metodo_interactivo5(fun_sim, xn, xv, pn, tol, iteracion, arreglox, arregloy, graf)
  syms x;
  arreglo_x=[];
  arreglo_y=[];
  arreglo_totalx=[];
  arreglo_totaly=[];
  if( arreglox(1) ~= 1000)
    arreglo_totalx= arreglox;
    arreglo_totaly= arregloy;
  endif

  if (abs(subs(fun_sim, x, xn)) <= tol)
    if (graf ==1)
      retorno = [xn iteracion];
      plot(arreglox,arregloy);
      xlabel ("Eje X - Error");
      ylabel ("Eje Iteracción");
    else
      retorno = [xn iteracion];
    endif
  else
    wn = xn + pn*(subs(fun_sim,x,xn));
    xnueva = xn - (subs(fun_sim,x,xn)/((subs(fun_sim,x,xn)-subs(fun_sim,x,wn))/(xn-wn)));
    N = subs(fun_sim,x,xv) + (x - xnueva) * ((subs(fun_sim,x,xnueva)-subs(fun_sim,x,xn))/(xnueva-xn));
    derivada = diff(N, x);
    pnueva = -1/derivada;
    iteracion = iteracion + 1;
    a=subs(fun_sim, x,xn);
    x=double(a);
    arreglo_totalx = [arreglo_totalx x];
    arreglo_totaly = [arreglo_totaly iteracion];
    metodo_interactivo5(fun_sim, xnueva, xn, pnueva, tol, iteracion, arreglo_totalx, arreglo_totaly, graf)
  endif
endfunction