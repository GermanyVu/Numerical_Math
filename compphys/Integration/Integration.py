import numpy as np

def Quadraticf(A,B,C,x ):
    return A*x**2 +B*x + C

def Analyticf(A,B,C,init,final ):
    return (A*(1/3)*final**3 +B*(1/2)*final**2 + C*final -  A*(1/3)*init**3 -B*(1/2)*init**2 - C*init)

def TrapezoidRule(A,B,C,number_trapezoid,init,final):
    h =(final-init)/number_trapezoid
    s = 0.5*(Quadraticf(A,B,C,init) + Quadraticf(A,B,C,final))
    for k in range(1,number_trapezoid):
        s += Quadraticf(A,B,C,init+k*h)
    return h*s

def SimpsonRule(A,B,C,number_slices, init, final):
    h =(final-init)/number_slices
    s = (Quadraticf(A,B,C,init) + Quadraticf(A,B,C,final))
    for k in range(1,number_slices):
        if(k%2 == 0):
            s += 2*Quadraticf(A,B,C,init + k*h)
        else:
            s += 4*Quadraticf(A,B,C,init + k*h)
    return (1/3)*h * s

def SimpsonRule_eps(A,B,C,number_slices,eps, init, final):
    h =(final-init)/number_slices
    s = Quadraticf(A,B,C,init) + Quadraticf(A,B,C,final)
    t1 = 0
    t2 = 0
    switch = True

    for k in range(1,number_slices):
        if(k%2 == 0):
            s += 2*Quadraticf(A,B,C,init + k*h)
        else:
            t1 += (2/3)*Quadraticf(A,B,C,init + k*h)
    intg1 = h *(s+2*t1)
    """ double the number slices"""
    while ( switch == True):

        h  = (1/2) * h
        number_slices = 2 *number_slices
        for  k in range(1, number_slices):
            if k%2 != 0 :
                t2 += (2/3)*Quadraticf(A,B,C,init + k*h)
        s = s + t1
        intg2 = h*(s +2*t2)
        if error(intg1,intg2) <= eps:
            switch = False
        else:
            intg1 = intg2


    return intg1, number_slices

def error(Intg1,Intg2):
    return (1/15)* abs(Intg1 - Intg2)


#main
A= 2
B =1
C =1
number_slices = 10
init = 1
final = 6
eps = 10e-2
print (SimpsonRule_eps(A,B,C,number_slices,eps, init, final))
print ("simpson rule" , SimpsonRule(A,B,C,number_slices, init, final))
print("trapezoid" , TrapezoidRule(A,B,C,number_slices,init,final))
print ("actual:" , Analyticf(A,B,C,init,final ) )
