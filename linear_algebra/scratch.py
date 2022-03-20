#Create a new tensor product, this time with pauli x and i operators
import numpy as np
zero = np.array([[1],[0]])

one = np.array([[0],[1]])


#hadamard gate and identity tensor product
hadamard = np.array([[1,1], [1,-1]]) * 1/np.sqrt(2)
print(hadamard)
pauli_i = np.array([[1,0], [0,1]])
print(pauli_i)
combined = (np.kron(hadamard, pauli_i))
zero_one = np.array([[1],[0],[0],[1]])  

ab = np.array([[1/np.sqrt(2)],[1/np.sqrt(2)]]) 

print(np.round(np.matmul(hadamard,ab)))


cnot = np.array([[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]])
cnot_output = (np.matmul(cnot,zero_one))

#print(cnot_output)

