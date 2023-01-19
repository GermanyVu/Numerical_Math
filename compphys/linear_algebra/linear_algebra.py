import numpy as np 
 
class GaussianElimination:
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.vector = vector
        self.answer= []

    def gaussian_elimination(self):
        self._divide_diagonal()


    def _divide_diagonal(self):
        diagonal_length = len(self.vector)
        for index in range(diagonal_length):
            self._partial_probing(index,diagonal_length)
             #divide by the diagonal element
            diagonal_element= self.matrix[index,index]            
            self.matrix[index,:] /= diagonal_element
            self.vector[index] /= diagonal_element
            self._subtract_rows(index,diagonal_length)
        self._backsub(index,diagonal_length)


    def _subtract_rows(self, index,diagonal_length):
        for row in range(index+1, diagonal_length):
            coefficient = self.matrix[row,index]
           # print(coefficient)
            self.matrix[row,:] -=coefficient*self.matrix[index,:]
           # print(self.matrix[row,:])
            self.vector[row]  -= coefficient*self.vector[index]
            print(self.matrix)

    def _backsub(self,index, diagonal_length):
        x = np.zeros(diagonal_length,float)
        for index in range(diagonal_length-1,-1,-1): # range(start, end,step)
           x[index] = self.vector[index]
           for col in range(index+1,diagonal_length):
               x[index] -= self.matrix[index,col]*x[col]
        self.answer = x

    def _partial_probing(self,index,diagonal_length):
        coeff_dict ={}
        for row in range (index, diagonal_length):
            coeff_dict.update({row:self.matrix[row,index]})
        max_key = max(coeff_dict,key= lambda k: abs(coeff_dict[k]))
        print(max_key)
        self._switch(max_key, index )

    def _switch(self,key, index):
        print(index,key)
        if index != key: 
            self.matrix[[index,key]] = self.matrix[[key,index]]
      #      print(self.matrix)

            a = self.vector[index]
            b = self.vector[key]
            self.vector[index] = b 
            self.vector[key] = a
       #     print(self.vector)


