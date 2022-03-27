import numpy as np

#Helper functions
def get_eigenvalues(eigen_array):
    return eigen_array[0]

def get_eigenvectors(eigen_array):
    return eigen_array[1]

##Create our gates

##Pauli I

identity = np.array([[1,0], [0,1]])

##Pauli X
x_gate = np.array([[0,1], [1,0]])

##Pauli Y
y_gate = np.array([[0,-1j], [1j,0]])


##Example matrix
toy = np.array([[1,0], [1,2]])


##Get Eigenvalues and Eigenvectors for Identity Matrix
identity_ee = (np.linalg.eig(identity))
print(f'The eigenvalues for Identity Matrix are {get_eigenvalues(identity_ee)}')
print(f'The normalised eigenvectors for Identity matrix are {get_eigenvectors(identity_ee)}')

##Get Eigenvalues and Eigenvectors for X Gate
x_ee = (np.linalg.eig(x_gate))
print(f'The eigenvalues for X Gate are {get_eigenvalues(x_ee)}')
print(f'The normalised eigenvectors for X Gate are {get_eigenvectors(x_ee)}')

##Get Eigenvalues and eigenvectors for Pauli Y Gate
y_ee = (np.linalg.eig(y_gate))
print(f'The eigenvalues for Y Gate are {get_eigenvalues(y_ee)}')
print(f'The normalised eigenvectors for Y Gate are {get_eigenvectors(y_ee)}')
