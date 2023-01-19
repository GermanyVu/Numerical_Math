from NumericIntegration import Integration
import PolynomialMaker as poly

class Simpson(Integration):
    ''' integral = h*(S+2T)'''
    def simpson_method(self, f):
        s_1 = self.first_iter_s(f)
        t_1 = self.t(f)
        first_integ = self.h*(s_1 +2*t_1)
        s_prev = s_1
        t_prev = t_1
        prev_integ = first_integ

        while(True):
            self.double_it() #double the number of step
            s_i = s_prev + t_prev
            t_i = self.t(f)
            integ_i = self.h * (s_i +2*t_i)

            error = self.error_calc(integ_i, prev_integ)
            if (error <= self.error):
                break
            else:
                prev_integ = integ_i
                s_prev = s_i
                t_prev = t_i

        return integ_i

    def t(self,func):
        sum = 0
        for k in range(1, self.number_slices):
            if k%2 != 0: #odd
                sum += func(self.initial_limit+ k*self.h)
        return 2.0/3.0 *sum

    def first_iter_s(self,func):
        sum = func(self.initial_limit) + func(self.final_limit)
        for k in range(1, self.number_slices):
            if k%2 == 0:  #even
                sum += 2*func(self.initial_limit+ k*self.h)
        return 1.0/3.0*sum


    def error_calc(self,cur_iter, prev_iter):
        error = (1.0/15.0) * abs(cur_iter - prev_iter)
        return error
