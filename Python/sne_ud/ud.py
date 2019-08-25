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
    Version Original del metodo iterativo Chebyshev-Halley, con un valor de alfa = 1
    Recuperado del documento "A stable class of improved second-derivative free
    Chebyshev-Halley type methods with optimal eighth order convergence" creado por 
    Alicia Cordero, Munish Kansal, Vinay Kanwar y Juan R. Torregrosa.
    Para efectos de probar el método, se utilizó la función x^3+4*(x^2)-10 con un valor incial de 1.
    Parametros: 
            1) func: Funcion en formato string en terminos de x la cual require la aproximacion
            2) x0: Valor inicial de la funcion necesario para las siguientes aproximaciones
            3) tol: Tolerancia al error maxima para el cálculo de la aproximacion
            4) graf: Bandera para realizar o no el grafico de iteraciones vs aproximacion.
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
            temp = aprox - (1 + 0.5 * (lF/1-lF))*functionAprox/firstDerivateAprox
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


def sne_ud_3(func, x0, tol, graf):
    """
    Version optimizada del metodo iterativo Chebyshev-Halley, con un valor de alfa = 1
    Recuperado del documento "A stable class of improved second-derivative free
    Chebyshev-Halley type methods with optimal eighth order convergence" creado por 
    Alicia Cordero, Munish Kansal, Vinay Kanwar y Juan R. Torregrosa. Esta versión intenta 
    lograr valores de conversión en el orden de 8 comparado a el quinto logrado con el original, ecuación 2.1 del documento.
    Para efectos de probar el método, se utilizó la función x^3+4*(x^2)-10 con un valor incial de 1.
    Parametros: 
    	1) func: Funcion en formato string en terminos de x la cual require la aproximacion
        2) x0: Valor inicial de la funcion necesario para las siguientes aproximaciones
        3) tol: Tolerancia al error maxima para el cálculo de la aproximacion
        4) graf: Bandera para realizar o no el grafico de iteraciones vs aproximacion.
    """
    x = Symbol("x")
    f = sympify(func)
    firstDerivate = diff(func, x)
    secondDerivate = diff(firstDerivate, x)
    xAxis = []
    yAxis = []
    aprox = x0
    iteration = 1
    while (abs(f.subs(x,aprox)) >= tol):
        functionAprox = f.subs(x,aprox)
        firstDerivateAprox = firstDerivate.subs(x,aprox)
        lF = Lf(f, firstDerivate, secondDerivate, aprox)
        zn = aprox - (1 + 0.5 * (lF/1-lF)) *functionAprox/firstDerivateAprox
        temp = zn - f.subs(x,zn)/firstDerivate.subs(x,zn)
        aprox = temp
        xAxis += [iteration]
        yAxis += [f(aprox)]
        iteration += 1 
    if (graf == 1):
        plt.plot(xAxis, yAxis)
        plt.title('Iteration vs aproximation graph using a tol value of: ' + str(tol))
        plt.xlabel("iterations")
        plt.ylabel("Aproximation")
        plt.show()
        return [aprox, iteration]
    else: 
        return  "Iteration numeber:"+ str(iteration) + " Aproximation value: " + str(aprox)


