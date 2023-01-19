from NumericIntegration import Integration
import PolynomialMaker as poly


class Trapezoid(Integration):
    def trapezoid_method(self, f):
        prev_iter = self.first_iter_trapezoid(f)

        while(True):

            self.double_it() #double the number of step
            cur_iter = self.n_iter_trapezoid(f,prev_iter)
            error = self.error_calc(cur_iter, prev_iter)
            if (error <= self.error):
                break
            else:
                prev_iter = cur_iter
        return cur_iter


    def first_iter_trapezoid(self, func):
        sum = 0.5*(func(self.initial_limit) + func(self.final_limit))
        for k in range(1, self.number_slices ):
            sum  += func(self.initial_limit+ k* self.h)
        return sum

    def n_iter_trapezoid(self, func,prev_iter):

        sum = 0.5 * prev_iter
        for k in range(1, self.number_slices ):
            if k%2 != 0:
                sum  += self.h * func(self.initial_limit+ k* self.h)
        return sum

    def error_calc(self,cur_iter, prev_iter):
        error = (1.0/3.0) * abs(cur_iter - prev_iter)
        return error
