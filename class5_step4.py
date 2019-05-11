import numpy as np
import random

mymatrix_zeros = np.zeros((2,2))
mymatrix_ones = np.ones((2,2))
mymatir_eye = np.eye(2,2)
mymatrix_rand = np.random.rand(3,3)

#making an array of 7s
array_of_sevens = np.ones(20)*7
print(array_of_sevens)
#reshaping the array into a matrix with 4 rows, 5 columns
reshape_of_sevens = array_of_sevens.reshape(4,5)
print(reshape_of_sevens)

#printing the third row
print(reshape_of_sevens[3])
