function lf = Lf(func, xn)
    pkg load symbolic;
    syms x;
    t_func = strcat('@(x)', func);
    f = str2func(t_func);
    fp = matlabFunction(diff(f, x));
    fp2 = matlabFunction(diff(fp, x));
    lf = (f(xn)*fp2(xn))/((fp(xn))**2);
endfunction