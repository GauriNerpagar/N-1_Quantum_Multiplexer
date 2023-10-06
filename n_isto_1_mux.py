import qiskit
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library.standard_gates import SwapGate
import matplotlib

n = int(input("Enter number of lines to be multiplexed : (Please add number 2 or greater)"))
N = n-1
c=(bin(N)[2:])
c=str(c)
c=len(c)  # Number of control qubits
lines = n+c

QR = QuantumRegister(lines)
Qmux = QuantumCircuit(QR)

# Create control state array
SA = list(range(1, n))
mux_start = c
mux_end = c+1

for p in SA:
    
    
    S=(bin(p)[2:]) #Control state
    
    if len(S)<c: #Converting S to c-bit binary by zero filling
        S = S.zfill(c)
    
    #Creating Multicontrol Custom Swap Gate
    BSwap= SwapGate().control(c,"C2swap",S)
    
    #Circuit ordering
    Control = list(range(0,c))
    Swap_Order = [mux_start, mux_end]
    Mux_Order = Control + Swap_Order
    Qmux.append(BSwap, Mux_Order)
    mux_end = mux_end+1
    
Qmux.draw('mpl')
