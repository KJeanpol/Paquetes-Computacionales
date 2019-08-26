import matplotlib.pyplot as plt
from sympy import Symbol, sympify, diff, Subs

def Lf(f, fp, fp2, xn):
    x = Symbol("x")
    fn = f.subs(x, xn)
    fpn = fp.subs(x, xn)**2
    fp2n = fp2.subs(x, xn)
    return (fn*fp2n)/fpn

def sne_ud_1(fstr, x0, tol, graf): # super-Halley

    """
    Evalua una funcion dependiente de X para asi encontrar una aproximacion
    de una de sus raices.

    Recuperado de "Geometric constructions of iterative functions to solve
        nonlinear equations"    
    Autores "S.Amat, S.Busquier, J.M. Guti"

    Retorna una lista donde sus elementos son el x aproximado y la cantidad de
    iteraciones necesarias para cumplir con la tolerancia dada

    parametros:
    fstr: funcion dependdiente de x a la cual se le quiere encontrar sus ceros
    x0: valor inicial para empezar a calcular las iteraciones
    tol: tolerancia aceptable para finalizar el metodo
    graf: parametro para indicar si se quiere generar la grafica

    Ejemplo sne_ud_1('x**2-4*x+4', 5, 0.00001, 1)
    
    """

    x = Symbol("x")
    try:
        f = sympify(fstr)
    except ValueError:
        return 'Syntaxis de la funcion incorrecta'
    fp = diff(f,x)
    fp2 = diff(fp, x)
    itera = 0
    xAprox = x0
    xAx = []
    yAx = []
    while (abs(f.subs(x, xAprox)) >= tol):
        xAx += [itera]
        yAx += [abs(f.subs(x, xAprox))]
        try:
            fpxn = 1/(fp.subs(x, xAprox))
            fpxn = fpxn**(-1)
        except ValueError:
            break
        fxn = f.subs(x, xAprox)
        Lfxn = Lf(f, fp, fp2, xAprox)
        xAprox = xAprox - (1+0.5*(Lfxn/(1-Lfxn)))*(fxn/fpxn)
        itera += 1
    if (graf):
        plt.plot(xAx, yAx)
        plt.title('Comportamiento del metodo de Super-Halley para ' + fstr) 
        plt.xlabel('iteraciones')
        plt.ylabel('|f(Xaprox)|')
        plt.grid(True)
        plt.show()
        return [xAprox, itera]
    else:
        return [xAprox, itera]
