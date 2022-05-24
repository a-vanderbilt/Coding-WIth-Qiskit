import qiskit
from qiskit.visualization import plot_histogram

# This Qiskit program demonstrates how quantum entanglement is achieved.
# Intuitively speaking, qubit 0 is placed in superposition using a Hadamard gate.
# Then, a CNOT gate is applied to qubit 0 and 1. The state of qubit one is dependent
# on the result of the CNOT gate, but until we measure it, we do not know what that is.
# Implemented correctly, we should see a 50/50 distribution with both qubits having the same value.

# Create a new quantum circuit with two classical and two quantum bits.
quantum_circuit = qiskit.QuantumCircuit(2,2)

# Apply a Hadamard gate to the 0 qubit.
# This puts the qubit in superposition.
quantum_circuit.h(0)

# Apply a CNOT gate to qubit 1, using qubit 0 as the control qubit.
# Since qubit 0 is in superposition, qubit 1 will also enter superposition.
quantum_circuit.cx(0,1)

# Measure the values of the qubits and store them in the classical bits.
quantum_circuit.measure_all()

# Draw out the circuit diagram.
quantum_circuit.draw()

# Simulate the circuit using the Aer backend.
simulator = qiskit.Aer.get_backend('qasm_simulator')
results = qiskit.execute(quantum_circuit, backend=simulator).result()
qiskit.visualization.plot_histogram(results.get_counts(quantum_circuit))
