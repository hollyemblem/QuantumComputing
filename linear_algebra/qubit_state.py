''''Computational qubit state example'''
import numpy as np

qubit_0 = np.array((1,0))
qubit_1 = np.array((0,1))

print(qubit_0)
print(qubit_1)


# Compute the tensor product
state_0_1 = np.kron(qubit_0,qubit_1)
print(state_0_1)