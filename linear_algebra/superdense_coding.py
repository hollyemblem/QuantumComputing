###Superdense Coding Example - Matrix Multiplication and Tensor (Kronecker) Products

'''
Creating an entangled Bell pair: https://qiskit.org/textbook/ch-algorithms/superdense-coding.html
--------

PART ONE
This code creates generates a tensor product of |0>|0> which is [1,0,0,0]
Then, a hadamard gate is applied to the first qubit, which returns |+> or 1/sqrt(2)*(|0>+|1>)
We then apply this back to the second qubit which creates superposition.
From here, we then apply a CNOT gate to both qubits, which generates an entangled state of
(|00> + |11>)*1/sqrt(2)
We check our output matches what we expected. Formally, we have created B00.

PART TWO
We now move into superdense coding using our entangled states.
We split the qubits we have created with our friend Alice, who wants to use them to send a message to us.
Alice takes the first qubits which are |0> and |1> from B00.
Alice decides she wants to send us a message of |00>, so to do so she simply applies the identity matrix to us.
Next, we pretend Alice transmits this to us with classical computing channels.
As Bob, we pick up Alice's message and begin to decode it.
We apply a CNOT gate which allows us to factor out the second qubit, and manipulate the first one.
We put the first qubit through a Hadamard gate, and then we take the tensor product of this output and the second qubit, the second qubit was |0>.
Taking this product (kronecker officially) gives us Alice's secret message, which is |00>.
'''

import numpy as np

##PART ONE - CREATING A BELL PAIR STATE
zero = [[1],[0]]
zero_zero = (np.kron(zero,zero))
hadamard = np.array([[1,1], [1,-1]]) * 1/np.sqrt(2)
q0 = (zero)  #Separate out the first qubit.
#Apply the hadamard matrix to the first qubit.
hadamard_q0 = ((np.matmul(hadamard,q0))) 


##We now want to apply the outcome of this first qubit onto the second one with a kroenecker product...
##The second qubit was [1,0] as we simply started with a tensor product of these two qubits, so bring that back in.
superposition = (np.kron(hadamard_q0,zero))
print(superposition)

##Create a CNOT gate to put the qubits into an entangled state
cnot = np.array([[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]]) 
cnot_output = (np.matmul(cnot,superposition))

##Output from the CNOT gate should equal an entangled state of (|00> + |11>)*1/sqrt(2)
print(cnot_output)

##In matrix terms this would be 
check_output = np.array([[1],[0],[0],[1]])*1/np.sqrt(2)

print(np.array_equiv(cnot_output, check_output))

'''Srinjoy Ganguly and Thomas Cambier in Quantum Computing with Silq Programming have verification methods for if a quantum state is entangled (Chapter 3)'''

##PART TWO - CREATING A BELL PAIR STATE
'''
We now want to give a qubit to our friend Alice, this will allow Alice to communicate back to us (Bob) with her new qubit.
We're going to give Alice our first qubit.
In our example, Alice wants to give us |00> so will apply an identity matrix to her qubit in order to do so.
Alice is going to take the first qubit, so |0> and |1> from (|00> + |11>)*1/sqrt(2)
'''

pauli_identity_matrix = np.array([[1,0], [0,1]])
##For ease we're going to create Alice's qubits here.
alice_qubit_0 = [[1],[0]] 
alice_qubit_1 = [[0],[1]] 

alice_qubit_0 = np.matmul(pauli_identity_matrix,alice_qubit_0  )
alice_qubit_1 = np.matmul(pauli_identity_matrix,alice_qubit_1  )

#Some manipulation to recreate our entangled state earlier....
alice_qubit_0 = (np.kron(alice_qubit_0,alice_qubit_0))
alice_qubit_1 = (np.kron(alice_qubit_1,alice_qubit_1))

alice_output = (alice_qubit_0+alice_qubit_1)*1/np.sqrt(2)

##Checking Alice's output still matches
print(np.array_equiv(alice_output, check_output))

##We will pretend Alice is now handing over her information back to us and we (Bob) are going to get to the output state she wanted, which is |00>

##We are going to apply a CNOT gate again...
decrypt_cnot_output = (np.matmul(cnot,alice_output))
print(decrypt_cnot_output)

##CNOT and hadamard gates: https://qiskit.org/textbook/ch-algorithms/superdense-coding.html
##This is equivalent to 1/sqrt(2)*(a|0> + b|1>)|0>. We can prove this by creating these values
# Factoring out this second qubit is helpful as it allows us to manipulate the first one.

one_one = [[1],[1]] * 1/np.sqrt(2)
verifying_output = (np.kron(one_one,zero)) 
print(f'This is the output we expected \n {verifying_output} this should also match \n {decrypt_cnot_output}')

##We can exploit the fact that this is equivalent to apply a hadamard gate to the first qubit.
##For ease, we have used one_one as our first qubit, as we have proved it is equivalent to our cnot output.

hadamard_gate_output = (np.round(np.matmul(hadamard,one_one)).astype(int))
#This should return |0> or [[1],[0]]
print(hadamard_gate_output)

#Now we have |0> in place of 1/sqrt(2)*(a|0> + b|1>). 
#As we can see the hadamard gate transformed this output. 
#Our final step is to replace this into the equation 1/sqrt(2)*(a|0> + b|1>)|0> = |0>|0> which again is a kroneker product:
alices_message_to_bob = (np.kron(hadamard_gate_output,zero)) 

'''Casting our mind back, we remember Alice's secret message to us was  |00>.
We need to verify the output from all of our calculations as Bob matches her secret message. 
We actually used |00> right at the top to create our entangled state, so we can verify our output
against what we reached previously ^ '''


print(np.array_equiv(zero_zero, alices_message_to_bob))
