import sympy

'''
class version of polynomial creator
'''
class Polynomial:

    def __init__(self, *coefficients):
        self.coefficients = coefficients[::-1]

    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x** index
        return res

'''
>>> a[::-1]
[8, 7, 6, 5, 4, 3, 2, 1]

Okay. And that -1 I snuck in at the end? It means to increment the index every
time by -1, meaning it will traverse the list by going backwards. If you wanted
 the even indexes going backwards, you could skip every second element and set
 the iteration to -2. Simple.

'''
def polynomial_creator(coefficients):
    """ coefficients are in the form a_n, ... a_1, a_0
    """
    def polynomial(x):
        res = 0
        # print('coefficient' ,coefficients[::-1])
        for index, coeff in enumerate(coefficients[::-1]):
            # print('coeff', coeff)
            # print('index', index)
            res += coeff * x** index
        return res
    return polynomial

#-------------------------------------------------------------------
def polynomial_rep(initial_limit,final_limit ,string_list):
    expression =''
    for index, coeff in enumerate(string_list[::-1]):
        if(index !=0):
            expression += '+'+str(coeff)+'*'+'x'+'^'+str(index)
        else:
            expression += str(coeff)
    print('expression',expression)
    return expression

#p1 = polynomial_creator(4)
#p2 = polynomial_creator(2, 4)
# p3 = polynomial_creator(1, 8, -1, 3, 2)
#p4  = polynomial_creator(-1, 2, 1)
