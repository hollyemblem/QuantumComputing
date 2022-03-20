###Superdense Coding Example - Matrix Multiplication and Tensor (Kronecker) Products

'''
Creating an entangled Bell pair: https://qiskit.org/textbook/ch-algorithms/superdense-coding.html
--------

PART ONE
This code creates generates a tensor product of |0>|1>
Then, a hadamard gate is applied to the first qubit |0>.
We then apply this back to the second qubit |1> which creates superposition.
From here, we then apply a CNOT gate to both qubits, which generates an entangled state of
(|01> + |10>)*1/sqrt(2)
We check our output matches what we expected. Formally, we have created B01.
'''

import numpy as np

##PART ONE - CREATING A BELL PAIR STATE
zero = np.array([[1],[0]])
one = np.array([[0], [1]])

#This is |01>
zero_one = (np.kron(zero,one))
hadamard = np.array([[1,1], [1,-1]]) * 1/np.sqrt(2)
q0 = zero  #Separate out the first qubit., so |0>
#Apply the hadamard matrix to the first qubit.
hadamard_q0 = ((np.matmul(hadamard,q0)))

##Applying absolute value as "it does not matter whether it is positive or negative for the result of this circuit (global phase factors have no significance)."
print(hadamard_q0)

##We now want to apply the outcome of this first qubit onto the second one with a kroenecker product...
##The second qubit was [0,1] as we simply started with a tensor product of these two qubits, so bring that back in.
superposition = (np.kron(hadamard_q0,one))
print(superposition)

##Create a CNOT gate to put the qubits into an entangled state
cnot = np.array([[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]]) 
cnot_output = (np.matmul(cnot,superposition))

##Output from the CNOT gate should equal an entangled state of (|01> + |10>)*1/sqrt(2)
print(cnot_output)

##In matrix terms this would be 
check_output = np.array([[0],[1],[1],[0]])*1/np.sqrt(2)

print(np.array_equiv(cnot_output, check_output))
