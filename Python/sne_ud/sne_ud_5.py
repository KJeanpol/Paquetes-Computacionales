def sne_ud_5(func, x0, tol, graf):
    """    
    Método de Liu-Wang, utilizando alfa_1 = 5 y alfa_2 = -7, así como la función sin(x)^2-x^2+1 con x_0 = 1.5
    Recuperado del documento "A stable class of improved second-derivative free
    Chebyshev-Halley type methods with optimal eighth order convergence" creado por 
    Alicia Cordero, Munish Kansal, Vinay Kanwar y Juan R. Torregrosa.
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
    except:
        print("Syntax Error")
        return
    xAxis = []
    yAxis = []
    aprox = x0
    iteration = 1
    while (abs(f.subs(x,aprox))>=tol):
        functionAprox = f.subs(x,aprox)
        firstDerivateAprox = firstDerivate.subs(x,aprox)

        yn = aprox - functionAprox/firstDerivateAprox
        functionOnYn = f.subs(x,yn)
        divisor = N(functionAprox/functionAprox-2*functionOnYn)
        
        zn = yn - N((divisor)*functionOnYn/firstDerivateAprox)
        functionOnZn = f.subs(x,zn)
        temp = N(zn - ((functionAprox-functionOnYn/functionAprox-2*functionOnYn)**2 + (functionOnZn/functionOnYn-5*functionOnZn) + (4*functionOnZn/functionAprox+-7*functionOnZn))*N(functionOnZn/firstDerivateAprox))
        aprox = temp
        xAxis += [iteration]
        yAxis += [f.subs(x,aprox)]
        iteration +=1

    if (graf == 1):
       plt.plot(xAxis, yAxis)
       plt.title('Iteration vs aproximation graph using a tol value of: ' + str(tol))
       plt.xlabel("iterations")
       plt.ylabel("Aproximation")
       plt.show()
       return [aprox, iteration]
    else:
        return "Iteration numeber:" + str(iteration) + " Aproximation value: " + str(aprox)
