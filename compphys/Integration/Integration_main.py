from  TrapezoidRule import Trapezoid
from SimpsonRule import Simpson
from MidPointRule import MidPoint
from RombergRule import Romberg
import SymbolicIntegral as symb
from infinity_integral import  IntegrateInfLimit
import numpy as np
import sys

def string_to_float(string_list):
    float_list =[ float(i)  for i in string_list ]
    return float_list
def f(x):
    return np.sin(2*x)

number_slices = int(sys.argv[1])
initial_limit = float(sys.argv[2])
final_limit = float(sys.argv[3])
accepted_error = float(sys.argv[4])


# trapezoid_obj = Trapezoid(initial_limit, final_limit,number_slices, \
#     accepted_error)
# simpson_obj = Simpson(initial_limit, final_limit,number_slices, \
#     accepted_error)
# midpoint_obj = MidPoint(initial_limit, final_limit,number_slices, \
#     accepted_error)
# romberg_obj = Romberg(initial_limit, final_limit,number_slices, \
#     accepted_error)
inf_integral_obj = IntegrateInfLimit(initial_limit,final_limit,number_slices, \
    accepted_error)





''' defined function'''
general_function = lambda x: 1/x**2

symb.symbolic_integral(initial_limit,final_limit, \
     '1/x**2' )

print('the integral of your function is',  \
    inf_integral_obj.integrate_simpson(general_function))
print(inf_integral_obj)

# print('the integral of you function using the trapezoid method is',  \
#     trapezoid_obj.trapezoid_method(general_function))
# print(trapezoid_obj)
# print('the integral of you function using the simpson\'s method is',  \
#     simpson_obj.simpson_method(general_function))
# print(simpson_obj)
# print('the integral of you function using the midpoint\'s method is',  \
#     midpoint_obj.midpoint_method(general_function))
# print(midpoint_obj)
# print('the integral of you function using the romberg\'s method is',  \
#     romberg_obj.romberg_trapezoid_method(general_function))
# print(romberg_obj)
