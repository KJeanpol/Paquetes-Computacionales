import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt

def sne_ud_6(fstr, x0, m, tol, graf):
    """Evalua una funcion dependiente de X para asi encontrar una aproximacion
    de una de sus raices.
    
    Recuperado de "Multiplicity anomalies of an optimal fourth-order class of
    iterative methods for solving nonlinear equations"
    Ecuacion 1
    Autores "Ramandeep Behl, Alicia Cordero, Sandile S. Motsa, Juan R. Torregrosa"
    Retorna una lista donde sus elementos son el x aproximado y la cantidad de
    iteraciones necesarias para cumplir con la tolerancia dada

    Parametros:
    fstr: funcion dependdiente de x a la cual se le quiere encontrar sus ceros
    x0: valor inicial para empezar a calcular las iteraciones
    m: constante necesario para calcular x
    tol: tolerancia aceptable para finalizar el metodo
    graf: parametro para indicar si se quiere generar la grafica

    PRUEBA sne_fd_6('x**2', 2, 1, 0.0001, 1)
    """

    lista=[]
    retorno = metodo_iterativo6(fstr, x0, m, tol, 0, lista, graf)
    return retorno

def metodo_iterativo6(fstr, xn, m, tol, iteracion, arreglo, graf):
    """Evalua una funcion dependiente de X para asi encontrar una aproximacion
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
            
    if (abs(fun_sim.subs(x,xn)) <= tol):
        if (graf == 1):
            plt.plot(arreglo[0],arreglo[1])
            plt.show()
            return [xn, iteracion]
        else:
            return [xn, iteracion]
    else:
        derivada = sp.diff(fun_sim, x)
        yn = xn -((2*m/(m+2)) * (fun_sim.subs(x,xn)/derivada.subs(x,xn)))
        xnueva = xn - (fun_sim.subs(x,xn)/(2*derivada.subs(x,xn))*
                (((m*(m-2))*((m/(m+2))**(-m))*derivada.subs(x,yn)-(m**2)*derivada.subs(x,xn))/(derivada.subs(x,xn)-((m/(m+2))**(-m))*derivada.subs(x,xn))))
        iteracion = iteracion + 1
        arreglo_x.append(xn)
        x=fun_sim.subs(x,xn)
        arreglo_y.append(iteracion)
        arreglo_total.append(arreglo_x)
        arreglo_total.append(arreglo_y)
           
        metodo_iterativo6(fstr, xnueva, m, tol, iteracion, arreglo_total, graf)
            
