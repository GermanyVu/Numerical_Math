from  TrapezoidRule import Trapezoid
import PolynomialMaker as poly

class Romberg(Trapezoid):
    def romberg_trapezoid_method(self, f):

        r_i_prev = []
        r_i = []
        r_i_prev.append(self.first_iter_trapezoid(f))
        print('number of slices: ', self.number_slices,' Ri-1',r_i_prev )
        k = 1
        while(True):

            self.double_it()

            r_i.append(self.n_iter_trapezoid( f,r_i_prev[0]))
            for i in range(k):
                r = r_i[i] + 1/(4**(i+1)-1)  * ( r_i[i] - r_i_prev[i])
                r_i.append(r)
        #    print('k', k)
            print('number of slices: ', self.number_slices,' Ri',r_i )
            #print('Ri_1',r_i_prev[-1])
            error = self.error_calc( r_i, r_i_prev, k)
            if (error <= self.error):
                break
            else:
                r_i_prev = r_i
                k += 1
                r_i =[]

        return r_i[-1]



    def error_calc(self, r_i, r_i_prev, k):
        #print('k in error', k)
        error = abs(1/(4**(k)-1)  * ( r_i[-2] - r_i_prev[-1]))

        return error
