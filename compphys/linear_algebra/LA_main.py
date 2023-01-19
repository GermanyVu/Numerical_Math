from linear_algebra import GaussianElimination
import numpy as np
import random
A = np.random.rand(3,3)
v = [random.randrange(1, 50, 1) for i in range(3)]  

matrix1 = np.array([[0,1,4,1],[3,4,-1,-1],[1,-4,1,5], [2,-2,1,3]],dtype=float)
v1 = np.array([-4,3,9,7], dtype=float )

gauss_elim_obj = GaussianElimination(matrix1, v1)
gauss_elim_obj.gaussian_elimination()
print(gauss_elim_obj.answer)
