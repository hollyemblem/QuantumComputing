import numpy as np

#Create cnot matrix
cnot = np.array([[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]]) 

array = np.array([[0],[0],[0],[1]])

print(np.matmul(cnot, array))

#Take adjoint. Not strictly true as not taking conjugate transpose
cnot_adjoint = cnot.transpose()

#Create 4x4 identity matrix
identity_matrix = np.identity(4)

#multiply
cnot_adjoint_cnot = (np.matmul(cnot, cnot_adjoint))

#Check product of cnot adjoint and cnot equals identity matrix (shuold return true)
print(np.array_equiv(cnot_adjoint_cnot, identity_matrix))