''''
Tensor product questions...
Show that the tensor product of two unitary operators is unitary.
@Todo: This is late night code, should be functions.
'''
import numpy as np
#Create a matrix
pauli_i = np.array([[1,0], [0,1]])

# Compute the tensor product
tensor_product = np.kron(pauli_i,pauli_i)


#Is it unitary?
'''Unitary operators have the property that they preserve norm, and are invertible.
Eigenvectors of unitary matrices have a modulus of 1:
Proof: UU^* = I
'''
#Tranpose the tensor product
tensor_product_transpose = np.transpose(tensor_product)

print(np.matmul(tensor_product, tensor_product_transpose))

#Try with a new unitary operator
pauli_x = np.array([[0,1], [1,0]])

#Create a new tensor product, this time with pauli x and i operators
tensor_product_2 = np.kron(pauli_i,pauli_x)

#Create a transpose of the array
tensor_product_transpose_2 = np.transpose(tensor_product_2)

#Multiply the tensor product by its tranpose and check if an identity matrix.
print(np.matmul(tensor_product_transpose_2, tensor_product_2))
