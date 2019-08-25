from Equation import Expression
import matplotlib.pyplot as plt

def sne_fd_1(fstr, x0, tol, graf):
    """Evalua una funcion dependiente de X para asi encontrar una aproximacion
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

    ejemplo: sne_fd_1('sin(x)**2-x**2+1', 5, 0.00000000001, 1)

    """
    try:
        f = Expression(fstr, ["x"])
    except ValueError:
        return 'Syntaxis de la funcion incorrecta'
    yn = x0 - ((2*f(x0)**2)/((f(x0+f(x0)))-(f(x0-f(x0)))))
    xn = x0 - ((2*f(x0)**2)/((f(x0+f(x0)))-(f(x0-f(x0)))))*((f(yn)-f(x0))/(2*f(yn)-f(x0)))
    itera = 0
    xAx = []
    yAx = []
    while (abs(f(xn)) >= tol):
        xAx += [itera]
        yAx += [abs(f(xn))]
        try:
            denominador1 = 1/(f(xn+f(xn)) - f(xn-f(xn)))
            denominador1 = denominador1**(-1)
        except ValueError:
            break
        yn = xn - ((2*f(xn)**2)/denominador1)
        try:
            denominador2 = 1/(2*f(yn)-f(xn))
            denominador2 = denominador2**(-1)
        except ValueError:
            break
        xn = xn - ((2*f(xn)**2)/denominador1)*((f(yn)-f(xn))/denominador2)
        itera += 1
    if (graf):
        plt.plot(xAx, yAx)
        plt.title('Comportamiento del metodo de Newton-Raphson para ' + fstr) 
        plt.xlabel('iteraciones')
        plt.ylabel('|f(Xaprox)|')
        plt.grid(True)
        plt.show()
        return [xn, itera]
    else:
        return [xn, itera]


def sne_fd_2(fstr, x0, tol, graf):
    """Evalua una funcion dependiente de X para asi encontrar una aproximacion
    de una de sus raices.

    Recuperado de "Steffensen type methods for solving nonlinear equations"
    ecuacion 5
    Autores "Alicia Cordero, José L. Hueso, Eulalia Martínez, Juan R. Torregrosa"

    Retorna una lista donde sus elementos son el x aproximado y la cantidad de
    iteraciones necesarias para cumplir con la tolerancia dada

    parametros:
    fstr: funcion dependdiente de x a la cual se le quiere encontrar sus ceros
    x0: valor inicial para empezar a calcular las iteraciones
    tol: tolerancia aceptable para finalizar el metodo
    graf: parametro para indicar si se quiere generar la grafica

    ejemplo: sne_fd_2('sin(x)**2-x**2+1', 5, 0.00000000001, 1)

    """
    try:
        f = Expression(fstr, ["x"])
    except ValueError:
        return 'Syntaxis de la funcion incorrecta'
    yn = x0 - ((2*f(x0)**2)/((f(x0+f(x0)))-(f(x0-f(x0)))))
    zn = yn - ((yn-x0)/(2*f(yn)-f(x0)))*(f(yn))
    xn = zn - ((yn-x0)/(2*f(yn)-f(x0)))*(f(zn))
    itera = 0
    xAx = []
    yAx = []
    while (abs(f(xn)) >= tol):
        xAx = [itera]
        yAx = [abs(f(xn))]
        try:
            denominador1 = 1/(f(xn+f(xn)) - f(xn-f(xn)))
            denominador1 = denominador1**(-1)
        except ValueError:
            break
        yn = xn - ((2*f(xn)**2)/denominador1)
        try:
            denominador2 = 1/(2*f(yn)-f(xn))
            denominador2 = denominador2**(-1)
        except ValueError:
            break
        zn = yn - ((yn-xn)/denominador2)*(f(yn))
        xn = zn - ((yn-xn)/denominador1)*(f(zn))
        itera += 1
    if (graf):
        plt.plot(xAx, yAx)
        plt.title('Comportamiento del metodo de Newton-Raphson para ' + fstr) 
        plt.xlabel('iteraciones')
        plt.ylabel('|f(Xaprox)|')
        plt.grid(True)
        plt.show()
        return [xn, itera]
    else:
        return [xn, itera]
