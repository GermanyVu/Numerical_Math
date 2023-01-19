from derivative import NumericalDerivative

class ForwardDifference(NumericalDerivative):

    def differentiate(self, func,x):

        dfx =  (func(x + self.h) - func(x))/self.h
        return dfx

class CentralDifference(NumericalDerivative):

    def differentiate(self,func,x):
        dfx = (func(x + self.h/2) + func(x - self.h/2))/self.h
        return dfx

class HigherDerivative(NumericalDerivative):
    
    def second_derivative(self, func,x):
        ddfx = (func(x + self.h) + func(x - self.h))/self.h**2 \
                                            - 2*func(x)/self.h**2
        return ddfx
    

