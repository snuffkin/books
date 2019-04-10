# -*- coding: utf-8 -*-
"""install_circuit.ipynb

# インストール
"""

!pip install qiskit==0.8.0

"""# 1量子ビットの量子回路"""

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.tools.visualization import plot_histogram

qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.h(qr[0])

from qiskit.tools.visualization import circuit_drawer
circuit_drawer(circuit)

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.tools.visualization import plot_histogram

qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.x(qr[0])

from qiskit.tools.visualization import circuit_drawer
circuit_drawer(circuit)

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.tools.visualization import plot_histogram

qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.z(qr[0])

from qiskit.tools.visualization import circuit_drawer
circuit_drawer(circuit)

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.tools.visualization import plot_histogram

qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.iden(qr[0])

from qiskit.tools.visualization import circuit_drawer
circuit_drawer(circuit)

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.tools.visualization import plot_histogram

qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.measure(qr, cr)

from qiskit.tools.visualization import circuit_drawer
circuit_drawer(circuit)

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.tools.visualization import plot_histogram

qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.x(qr[0])
circuit.h(qr[0])

circuit.measure(qr, cr)

from qiskit.tools.visualization import circuit_drawer
circuit_drawer(circuit)

"""# 2量子ビットの量子回路"""

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.tools.visualization import plot_histogram

qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.h(qr[0])
circuit.cx(qr[0], qr[1])

circuit.measure(qr, cr)

from qiskit.tools.visualization import circuit_drawer
circuit_drawer(circuit)

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.tools.visualization import plot_histogram

qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.cx(qr[0], qr[1])

from qiskit.tools.visualization import circuit_drawer
circuit_drawer(circuit)

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.tools.visualization import plot_histogram

qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.cx(qr[1], qr[0])

from qiskit.tools.visualization import circuit_drawer
circuit_drawer(circuit)

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.tools.visualization import plot_histogram

qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.swap(qr[0], qr[1])

from qiskit.tools.visualization import circuit_drawer
circuit_drawer(circuit)

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.tools.visualization import plot_histogram

qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.measure(qr, cr)

from qiskit.tools.visualization import circuit_drawer
circuit_drawer(circuit)