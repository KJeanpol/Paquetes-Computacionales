import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt

def sne_fd_5(fstr, x0, p0, tol, graf):
    """Evalua una funcion dependiente de X para asi encontrar una aproximacion
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
    """
    lista=[]
    retorno = metodo_interactivo5(fstr, x0, 0, p0, tol, 0, lista, graf)
    return retorno
    

def metodo_interactivo5(fstr, xn, xv, pn, tol, iteracion, arreglo, graf):
    """Evalua una funcion dependiente de X para asi encontrar una aproximacion
    de una de sus raices.

    Recuperado de "A general class of four parametric with- and without
    memory iterative methods for nonlinear equations"
    Ecuacion: la primera ecuación que aparece 
    Autores "Fiza Zafar1, Alicia Cordero, Juan R. Torregrosa"
    Retorna una lista donde sus elementos son el x aproximado y la cantidad de
    iteraciones necesarias para cumplir con la tolerancia dada

    Parametros:
    fstr: funcion dependdiente de x a la cual se le quiere encontrar sus ceros
    xn: valor inicial para empezar a calcular las iteraciones
    xv: valor anterior de x
    pn: valor inicial para emperzar a calcular las iteraciones
    tol: tolerancia aceptable para finalizar el metodo
    iteracion: numero de veces que se ha tratado de encontrar x
    arreglo: es un arreglo de arreglos donde se almacena los valores de
    las iteracciones y los valores de la función evaluada en xnueva
    graf: parametro para indicar si se quiere generar la grafica
    """
    x = sp.symbols('x')
    try:
        fun_sim = parse_expr(fstr)
    except:
        print ('Error de sintaxis')
    arreglo_x=[]
    arreglo_y=[]
    arreglo_total=[]
    if( len(arreglo)>0):
        arreglo_total= arreglo
        arreglo_x=arreglo[0]
        arreglo_y=arreglo[1]
        arreglo_total=[]


    if (pn != 0):
        if (abs(fun_sim.subs(x,xn)) <= tol):
            if (graf == 1):
                plt.plot(arreglo[0],arreglo[1])
                plt.show()
                return [xn, iteracion]
            else:
                return [xn, iteracion]
        else:
            wn = xn + pn*(fun_sim.subs(x,xn))
            xnueva = xn - (fun_sim.subs(x,xn)/((fun_sim.subs(x,xn)-fun_sim.subs(x,wn))/(xn-wn)))
            N = fun_sim.subs(x,xv) + (x - xnueva) * ((fun_sim.subs(x,xnueva)-fun_sim.subs(x,xn))/(xnueva-xn))
            derivada = sp.diff(N, x)
            pnueva = -1/derivada
            iteracion = iteracion + 1
            arreglo_x.append(xn)
            x=fun_sim.subs(x,xn)
            arreglo_y.append(iteracion)
            arreglo_total.append(arreglo_x)
            arreglo_total.append(arreglo_y)

            metodo_interactivo5(fstr, xnueva, xn, pnueva, tol, iteracion,arreglo_total, graf)
        
    
