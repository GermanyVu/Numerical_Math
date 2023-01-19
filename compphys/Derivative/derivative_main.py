import derivative_classes as dc

generic_func = lambda x: x**2

first_der = dc.ForwardDifference(.01, .0001)
second_der_obj = dc.HigherDerivative(.01, .000001)
print(first_der.differentiate(generic_func,2))
print(second_der_obj.second_derivative(generic_func, 2))

