
%%Evalua una funcion dependiente de X para asi encontrar una aproximacion
%%de una de sus raices.
    
%%Recuperado de "Multiplicity anomalies of an optimal fourth-order class of
%%iterative methods for solving nonlinear equations"
%%Ecuacion 1
%%Autores "Ramandeep Behl, Alicia Cordero, Sandile S. Motsa, Juan R. Torregrosa"
%%Retorna una lista donde sus elementos son el x aproximado y la cantidad de
%%iteraciones necesarias para cumplir con la tolerancia dada

%%Parametros:
%%fstr: funcion dependdiente de x a la cual se le quiere encontrar sus ceros
%%x0: valor inicial para empezar a calcular las iteraciones
%%m: constante necesario para calcular x
%%tol: tolerancia aceptable para finalizar el metodo
%%graf: parametro para indicar si se quiere generar la grafica

%%PRUEBA sne_ud_6('x**2', 2, 1, 0.0001, 1)

disp('')
function [xAprox, iter, err] = sne_ud_6(func, x0, m, tol, graf)
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
  retorno = metodo_iterativo6(func, x0, m, tol, 0, listax, listay, graf)
  xAprox = retorno(1);
  iter = retorno(2);
  err = 'Se terminó correctamente';
endfunction

%{
Evalua una funcion dependiente de X para asi encontrar una aproximacion
de una de sus raices.
    
Recuperado de "Multiplicity anomalies of an optimal fourth-order class of
iterative methods for solving nonlinear equations"
Ecuacion 1
Autores "Ramandeep Behl, Alicia Cordero, Sandile S. Motsa, Juan R. Torregrosa"
Retorna una lista donde sus elementos son el x aproximado y la cantidad de
iteraciones necesarias para cumplir con la tolerancia dada

Parametros:
fstr: funcion dependdiente de x a la cual se le quiere encontrar sus ceros
xn: valor inicial para empezar a calcular las iteraciones
m: constante necesario para calcular x
tol: tolerancia aceptable para finalizar el metodo
iteracion: cantida de veces que se ha tratado de aproximar x
arreglo: es un arreglo de arreglos donde se almacena los valores de
las iteracciones y los valores de la función evaluada en xnueva
graf: parametro para indicar si se quiere generar la grafica
%}
function [xn, iteracion, err] = metodo_iterativo6(fun_sim, xn, m, tol, iteracion, arreglox, arregloy, graf)
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
    derivada = diff(fun_sim, x);
    yn = xn -((2*m/(m+2)) * (subs(fun_sim,x,xn)/subs(derivada,x,xn)));
    xnueva = xn - (subs(fun_sim,x,xn)/(2*subs(derivada,x,xn))*
              (((m*(m-2))*((m/(m+2))**(-m))*subs(derivada,x,yn)-(m**2)*subs(derivada,x,xn))
              /(subs(derivada,x,xn)-((m/(m+2))**(-m))*subs(derivada,x,xn))));
    iteracion = iteracion + 1;
    a=subs(fun_sim, x,xn);
    x=double(a);
    arreglo_totalx = [arreglo_totalx x];
    arreglo_totaly = [arreglo_totaly iteracion];
    metodo_iterativo6(fun_sim, xnueva, m, tol, iteracion, arreglo_totalx, arreglo_totaly, graf)
  endif
endfunction        
