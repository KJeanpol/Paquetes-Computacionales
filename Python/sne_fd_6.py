import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt

def sne_fd_6(fstr, xn, alpha1, alpha2, tol, graf):
    """Evalua una funcion dependiente de X para asi encontrar una aproximacion
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
    alpha1: constante necesario para calcular x
    alpha2: constante necesario para calcular x
    tol: tolerancia aceptable para finalizar el metodo
    graf: parametro para indicar si se quiere generar la grafica

    PRUEBA sne_fd_6('x**2', 2, 1, 2, 0.0001,1)
    """

    lista=[]
       
    retorno = metodo_recursivo6(fstr, xn, alpha1, alpha2, tol, lista, 0, graf)
    return retorno
    
def metodo_recursivo6(fstr, xn, alpha1, alpha2, tol, arreglo, iteracion, graf):
    """Evalua una funcion dependiente de X para asi encontrar una aproximacion
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
        yn = xn - (fun_sim.subs(x,xn)/derivada.subs(x,xn))
        zn = yn-(-derivada.subs(x,xn)+2*((fun_sim.subs(x,yn)-fun_sim.subs(x,xn))/(yn-xn)))
        xnueva = fun_sim.subs(x,zn)/((alpha1*((fun_sim.subs(x,yn)-fun_sim.subs(x,xn))/(yn-xn)))+
                        (alpha2*(fun_sim.subs(x,zn)-fun_sim.subs(x,yn))/(zn-yn))+(1-alpha1-alpha2)*
                        ((fun_sim.subs(x,zn)-fun_sim.subs(x,xn))/(zn-xn)))
        iteracion = iteracion + 1
        arreglo_x.append(xn)
        x=fun_sim.subs(x,xn)
        arreglo_y.append(iteracion)
        arreglo_total.append(arreglo_x)
        arreglo_total.append(arreglo_y)
 
        metodo_recursivo6(fstr, xnueva, alpha1, alpha2, tol, arreglo_total, iteracion, graf)
        
