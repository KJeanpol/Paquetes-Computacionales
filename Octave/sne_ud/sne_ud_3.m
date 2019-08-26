%%   Version optimizada del metodo iterativo Chebyshev-Halley, con un valor de alfa = 1
%%   Recuperado del documento "A stable class of improved second-derivative free
%%   Chebyshev-Halley type methods with optimal eighth order convergence" creado por 
%%   Alicia Cordero, Munish Kansal, Vinay Kanwar y Juan R. Torregrosa. Esta version intenta 
%%   lograr valores de conversion en el orden de 8 comparado a el quinto logrado con el original, ecuacion 2.1 del documento.
%%   Parametros: 
%%    1) func: Funcion en formato string en terminos de x la cual require la aproximacion
%%    2) x0: Valor inicial de la funcion necesario para las siguientes aproximaciones
%%    3) tol: Tolerancia al error maxima para el cálculo de la aproximacion
%%    4) graf: Bandera para realizar o no el grafico de iteraciones vs aproximacion.
%%   Probado con x^3-4*x^2-10 usando x0 =1
function sne_ud_3(func, x0, tol, graf)
    pkg load symbolic;
    syms x;
    tFunc = strcat('@(x)', func);
    try
        f = str2func(tFunc);
        firstDerivate = matlabFunction(diff(func,x));
        secondDerivate = matlabFunction(diff(firstDerivate,x));
    catch 
        err = "Syntax error"
    end_try_catch
    xAxis = [];
    yAxis = [];
    aprox = x0;
    iteration = 1;
    while (abs(f(aprox))>=tol)
        functionAprox = f(aprox);
        firstDerivateAprox = firstDerivate(aprox);
        try 
            lF =computeLf(f,firstDerivate,secondDerivate,aprox);
            zn = aprox - double((1+ 0.5 * (lF/1-lF))*functionAprox/firstDerivateAprox);
            temp = zn - f(zn)/firstDerivate(zn)
        catch   
            break
        end_try_catch
        aprox = temp;
        xAxis = [xAxis iteration];
        yAxis = [yAxis f(aprox)];
        iteration ++
    endwhile

    if (graf == 1)
        plot (xAxis, yAxis)
        titleText = strcat("Iteration vs aproximation graph using a tol value of: ", num2str(tol))
        title(titleText)
        xlabel("iterations")
        ylabel("Aproximation")
    else
        textResult = strcat("Iteration numeber:", num2str(iteration) ," Aproximation value: ", num2str(aprox))  
        disp(textResult)
    end
endfunction

function [lfValue] = computeLf(func,firstDerivate, secondDerivate, aprox)
        secondDerivateAprox = secondDerivate(aprox);
        functionAprox = func(aprox);
        firstDerivateAprox = firstDerivate(aprox);
        lfValue = secondDerivateAprox*functionAprox/firstDerivateAprox^2;
endfunction
