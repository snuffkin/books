# -*- coding: utf-8 -*-
"""install_circuit.ipynb
# インストール
"""

!pip install qiskit==0.10.5

"""# 1量子ビットの量子回路"""

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.visualization import plot_histogram

qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.h(qr[0])

circuit.draw(output='mpl')

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.visualization import plot_histogram

qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.x(qr[0])

circuit.draw(output='mpl')

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.visualization import plot_histogram

qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.z(qr[0])

circuit.draw(output='mpl')

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.visualization import plot_histogram

qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.iden(qr[0])

circuit.draw(output='mpl')

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.visualization import plot_histogram

qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.measure(qr, cr)

circuit.draw(output='mpl')

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.visualization import plot_histogram

qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.x(qr[0])
circuit.h(qr[0])

circuit.measure(qr, cr)

circuit.draw(output='mpl')

"""# 2量子ビットの量子回路"""

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.visualization import plot_histogram

qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.h(qr[0])
circuit.cx(qr[0], qr[1])

circuit.measure(qr, cr)

circuit.draw(output='mpl')

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.visualization import plot_histogram

qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.cx(qr[0], qr[1])

circuit.draw(output='mpl')

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.visualization import plot_histogram

qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.cx(qr[1], qr[0])

circuit.draw(output='mpl')

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.visualization import plot_histogram

qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.swap(qr[0], qr[1])

circuit.draw(output='mpl')

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.visualization import plot_histogram

qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qr, cr)

circuit.measure(qr, cr)

circuit.draw(output='mpl')