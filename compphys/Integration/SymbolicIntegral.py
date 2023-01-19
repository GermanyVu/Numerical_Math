import sympy
import PolynomialMaker as poly

''' this function calls the string polynomial and rep in integralform'''
def symbolic_integral(initial_limit,final_limit,func ):
    x = sympy.Symbol('x')
    sympy.init_printing()
    sympy.pprint(sympy.pretty(sympy.Integral(func , (x,initial_limit, \
        final_limit  ))))
