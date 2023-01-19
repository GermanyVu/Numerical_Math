from NumericIntegration import Integration
import PolynomialMaker as poly

class MidPoint(Integration):
    def midpoint_method(self, f):

        prev_iter = self.n_iter_midpoint(f)

        while(True):
            self.double_it() #double the number of step, halves h
            cur_iter = self.n_iter_midpoint(f)
            error = self.error_calc(cur_iter, prev_iter)
            if (error <= self.error):
                break
            else:
                prev_iter = cur_iter
        return cur_iter


    def n_iter_midpoint(self, func):
        sum = 0
        for k in range(0, self.number_slices ):
            sum  += self.h*func(self.initial_limit+ k*self.h + self.h/2.0)
            #print('k',k,str(self.initial_limit+ k*self.h + self.h/2.0))

        return sum


    def error_calc(self,cur_iter, prev_iter):
        error = (1.0/3.0) * abs(cur_iter - prev_iter)
        return error
