import matplotlib.pyplot as plt
from sympy import Symbol, sympify, diff, Subs

def Lf(f, fp, fp2, xn):
    x = Symbol("x")
    fn = f.subs(x, xn)
    fpn = fp.subs(x, xn)**2
    fp2n = fp2.subs(x, xn)
    return (fn*fp2n)/fpn

def sne_ud_1(fstr, x0, tol, graf): # super-Halley
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
            Lfxn = Lf(f, fp, fp2, xAprox)
        except ValueError:
            break
        fxn = f.subs(x, xAprox)
        fpxn = fp.subs(x, xAprox)
        xAprox = xAprox - (1+0.5*(Lfxn/(1-Lfxn)))*(fxn/fpxn)
        itera += 1
    if (graf):
        plt.plot(xAx, yAx)
        plt.title('Comportamiento del metodo de Newton-Raphson para ' + fstr) 
        plt.xlabel('iteraciones')
        plt.ylabel('|f(Xaprox)|')
        plt.grid(True)
        plt.show()
        return [xAprox, itera]
    else:
        return [xAprox, itera]