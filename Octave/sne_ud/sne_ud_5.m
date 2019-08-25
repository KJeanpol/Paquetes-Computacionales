function [lfValue] = computeLf(func,firstDerivate, secondDerivate, aprox)
        secondDerivateAprox = secondDerivate(aprox);
        functionAprox = func(aprox);
        firstDerivateAprox = firstDerivate(aprox);
        lfValue = secondDerivateAprox*functionAprox/firstDerivateAprox^2;
endfunction

#   Método de Liu-Wang, utilizando alfa_1 = 5 y alfa_2 = -7, así como la función sin(x)^2-x^2+1 con x_0 = 1.5
#   Recuperado del documento "A stable class of improved second-derivative free
#   Chebyshev-Halley type methods with optimal eighth order convergence" creado por 
#   Alicia Cordero, Munish Kansal, Vinay Kanwar y Juan R. Torregrosa.
#   Parametros: 
#    1) func: Funcion en formato string en terminos de x la cual require la aproximacion
#    2) x0: Valor inicial de la funcion necesario para las siguientes aproximaciones
#    3) tol: Tolerancia al error maxima para el cálculo de la aproximacion
#    4) graf: Bandera para realizar o no el grafico de iteraciones vs aproximacion.

function [iteration, aprox] = sne_ud_5(func, x0, tol, graf)
    pkg load symbolic;
    syms x;
    tFunc = strcat('@(x)', func);
    try
        f = str2func(tFunc);
        firstDerivate = matlabFunction(diff(func,x));
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
            yn = aprox - functionAprox/firstDerivateAprox
            functionOnYn = f(yn)
            divisor = functionAprox/functionAprox-2*functionOnYn
            zn = yn - (divisor)*functionOnYn/firstDerivateAprox
            functionOnZn = f(zn)
            temp = zn - [(functionAprox-functionOnYn/functionAprox-2*functionOnYn)^2 + (functionOnZn/functionOnYn-5*functionOnZn) + (4*functionOnZn/functionAprox+-7*functionOnZn)]*(functionOnZn/firstDerivateAprox)
        catch   
            break
        end_try_catch
        aprox = temp
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
