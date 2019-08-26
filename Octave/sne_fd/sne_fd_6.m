%%  Evalua una funcion dependiente de X para asi encontrar una aproximacion
%%  de una de sus raices.
    
%%  Recuperado de "Dynamical Techniques for Analyzing Iterative
%%  Schemes with Memory"
%%  Ecuacion 4
%%  Autores "Neha Choubey,A. Cordero, J. P. Jaiswal, and J. R. Torregrosa"
    
%%  Retorna una lista donde sus elementos son el x aproximado y la cantidad de
%%  iteraciones necesarias para cumplir con la tolerancia dada.
    
%%  Parámetros:
%%  fstr: funcion dependdiente de x a la cual se le quiere encontrar sus ceros
%%  xn: valor inicial para empezar a calcular las iteraciones
%%  alpha1: constante necesario para calcular x
%%  alpha2: constante necesario para calcular x
%%  tol: tolerancia aceptable para finalizar el metodo
%%  graf: parametro para indicar si se quiere generar la grafica

%%  PRUEBA sne_fd_6('x**2', 2, 1, 2, 0.0001, 1)


disp('')
function [xAprox, iter,err] = sne_fd_6(func, xn, alpha1, alpha2, tol, graf)
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
 
  retorno = metodo_recursivo6(f, xn, alpha1, alpha2, tol, listax, listay, 0, graf);
  xAprox = retorno(1);
  iter = retorno(2);
  err = 'Se terminó correctamente';

endfunction

%{
  Evalua una funcion dependiente de X para asi encontrar una aproximacion
  de una de sus raices.
    
  Recuperado de "Dynamical Techniques for Analyzing Iterative
  Schemes with Memory"
  Ecuacion 4
  Autores "Neha Choubey,A. Cordero, J. P. Jaiswal, and J. R. Torregrosa"
    
  Retorna una lista donde sus elementos son el x aproximado y la cantidad de
  iteraciones necesarias para cumplir con la tolerancia dada.
    
  Parámetros:
  fstr: funcion dependdiente de x a la cual se le quiere encontrar sus ceros
  xn: valor inicial para empezar a calcular las iteraciones
  alpha1: valor necesario para encontrar el x aproximado
  alpha2: valor necesario para encontrar el x aproximado
  tol: tolerancia aceptable para finalizar el metodo
  arreglo: es un arreglo de arreglos donde se almacena los valores de
  las iteracciones y los valores de la función evaluada en xnueva
  iteracion: cantida de veces que se ha tratado de aproximar x
  graf: parametro para indicar si se quiere generar la grafica
%}
function retorno = metodo_recursivo6(fun_sim, xn, alpha1, alpha2, tol, arreglox, arregloy, iteracion, graf)
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
    yn = xn - (subs(fun_sim, x,xn)/subs(derivada,x,xn));
    zn = yn-(-subs(derivada,x,xn)+2*((subs(fun_sim, x,yn)-subs(fun_sim, x,xn))/(yn-xn)));
    xnueva = subs(fun_sim,x,zn)/((alpha1*((subs(fun_sim,x,yn)-subs(fun_sim,x,xn))/(yn-xn)))+
                        (alpha2*(subs(fun_sim,x,zn)-subs(fun_sim,x,yn))/(zn-yn))+(1-alpha1-alpha2)*
                        ((subs(fun_sim,x,zn)-subs(fun_sim,x,xn))/(zn-xn)));
    iteracion = iteracion + 1;
    a=subs(fun_sim, x,xn);
    x=double(a);
    arreglo_totalx = [arreglo_totalx x];
    arreglo_totaly = [arreglo_totaly iteracion];
    metodo_recursivo6(fun_sim, xnueva, alpha1, alpha2, tol, arreglo_totalx, arreglo_totaly, iteracion, graf)
  endif
endfunction
        
