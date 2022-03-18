'''The trace function is the sum of its diagonals'''

import numpy as np

'''Show X Y and Z Pauli Operators have 0 trace'''

pauli_x = np.array([[0,1], [1,0]])
pauli_y =  np.array([[0,1j], [-1j,0]])
pauli_z = np.array([[1,0], [0,-1]])

print(np.trace(pauli_x))
print(np.trace(pauli_y))
print(np.trace(pauli_z))

'''If A and B are two linear operators show that tr(AB) = tr(BA) '''


print(np.trace(np.matmul(pauli_x, pauli_z)))
print(np.trace(np.matmul(pauli_z, pauli_x)))

'''Let A and B denote two linear operators and a is ∈ C . Show that 
tr(a.A  + B)  = α.trA()  + trB()
'''

matrix_a = np.array([[3,5], [1,2]])
matrix_b = np.array([[85,34], [7,2]])

a = 4
scalar_multiply = (a * matrix_a)

print(np.trace((scalar_multiply + matrix_b)))
print(np.trace((a * matrix_a)) + np.trace(matrix_b))

