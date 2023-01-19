import numpy as np
from NumericIntegration import Integration
from SimpsonRule import Simpson

class IntegrateInfLimit(Integration):

    def integrate_simpson(self, func):
        print(str(self.final_limit) )
        if self.initial_limit == '-inf'and self.final_limit == 'inf':
            func1, initial_limit1, final_limit1 = self._single_inf_conversion(\
                                            self.initial_limt, 0.0 , func)
            func2, initial_limit2, final_limit2 = self._single_inf_conversion(\
                                            0.0, self.final_limit , func)

            integral_sum =  self._single_integrate(intial_limit1,final_limit1,func1) \
                     +  self._single_integrate(intial_limit2,final_limit2,func2)
            return integral_sum

        elif self.initial_limit == 'inf'and self.final_limit == '-inf':
            func1, initial_limit1, final_limit1 = self._single_inf_conversion(\
                                            0.0,self.initial_limt, func)
            func2, initial_limit2, final_limit2 = self._single_inf_conversion(\
                                             self.final_limit, 0.0 , func)
            integral_sum =  self._single_integrate(intial_limit1,final_limit1,func1) \
                     +  self._single_integrate(intial_limit2,final_limit2,func2)
            return integral_sum

        else:
            trans_func, initial_limit, final_limit = self._single_inf_conversion(\
                                            str(self.initial_limit),str(self.final_limit),func)

            return self._single_integrate(initial_limit, final_limit,trans_func)

    def _single_integrate(self, initial_limit, final_limit, func):

        print('using simpson rule')
        simpson_obj = Simpson(initial_limit,final_limit)
        print(simpson_obj)
        print(func(2))

        return simpson_obj.simpson_method(func)

    def _single_inf_conversion(self,initial_limit, final_limit, func):

        print('I am in single inf conversion')
        if initial_limit == 'inf':
            trans_func = lambda z:( (1/(1-z))**2) *func(z/(1-z) + final_limit)
            initial_limit = 9.99999*10**-1
            final_limit = 1*10**-10
            return trans_func, initial_limit, final_limit
        elif initial_limit == '-inf':
            trans_func = lambda z:( (1/(1-z))**2) *func(z/(1-z) + final_limit)
            initial_limit = -9.99999*10**-1
            final_limit = 1*10**-10
            return trans_func, initial_limit, final_limit
        elif final_limit == 'inf':
            print('I am in single inf conversion1')
            trans_func = lambda z:( (1/(1-z))**2) *func(z/(1-z) + initial_limit)
            initial_limit = 1*10**-10
            final_limit = 9.99999*10**-1

            return trans_func, initial_limit, final_limit
        elif final_limit == '-inf':
            trans_func = lambda z:( (1/(1-z))**2) *func(z/(1-z) + initial_limit)
            initial_limit = 1*10**-10
            final_limit = -9.99999*10**-1
            return trans_func, initial_limit, final_limit
        else:
             print('I am in single inf conversion last')
             return func, initial_limit, final_limit
