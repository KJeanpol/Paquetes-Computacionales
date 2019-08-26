import matplotlib.pyplot as plt
from sympy import Symbol, sympify, diff, Subs

def Lf(f, fp, fp2, xn):
    x = Symbol("x")
    fn = f.subs(x, xn)
    fpn = fp.subs(x, xn)**2
    fp2n = fp2.subs(x, xn)
    return (fn*fp2n)/fpn

def sne_ud_4(func, x0, tol, graf):
    """
    Método de Halley con convergencia cúbica.
    Recuperado del documento "Geometric constructions of iterative functions to solve
    nonlinear equations" creado por S.Amata, S.Busquiera, J.M. Gutierrez
    Parametros: 
        1) func: Funcion en formato string en terminos de x la cual require la aproximacion
        2) x0: Valor inicial de la funcion necesario para las siguientes aproximaciones
        3) tol: Tolerancia al error maxima para el cรกlculo de la aproximacion
        4) graf: Bandera para realizar o no el grafico de iteraciones vs aproximacion.
    Probado con la funcion x^3 -4*x^2-10 con x_0 = 1
    """
    x = Symbol("x")
    try:
        f = sympify(func)
        firstDerivate = diff(f, x)
        secondDerivate = diff(firstDerivate, x)
    except: 
        print("Syntax Error")
        return 
    xAxis = []
    yAxis = []
    aprox = x0
    iteration = 1
    while (abs(f.subs(x,aprox)) >= tol):
        functionAprox = f.subs(x,aprox)
        firstDerivateAprox = firstDerivate.subs(x,aprox)
        try:
            lF = Lf(f, firstDerivate, secondDerivate, aprox)
            temp = aprox - (2/2-lF)*functionAprox/firstDerivateAprox
        except:
            break
        aprox = temp
        xAxis += [iteration]
        yAxis += [f.subs(x,aprox)]
        iteration += 1

    if (graf == 1):
        plt.plot(xAxis, yAxis)
        plt.title('Iteration vs aproximation graph using a tol value of: ' + str(tol))
        plt.xlabel("iterations")
        plt.ylabel("Aproximation")
        plt.show()
        return [aprox, iteration]
    else:
        textResult ="Iteration numeber:" + str(iteration) +  " Aproximation value: " + str(aprox)
        return textResult


