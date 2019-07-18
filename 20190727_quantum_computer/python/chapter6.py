# -*- coding: utf-8 -*-
"""chapter6.ipynb
# 第6章のソースコード

## リスト6.1: 量子回路の作成
"""

from qiskit import QuantumCircuit
from qiskit import ClassicalRegister, QuantumRegister

# 量子回路の初期化
qr = QuantumRegister(2, 'q') # 量子レジスタを作成
cr = ClassicalRegister(2, 'c') # 古典レジスタを作成
circuit = QuantumCircuit(qr, cr) # レジスタを使い量子回路を初期化

# 量子回路の組み立て
circuit.h(qr[0]) # アダマール行列を適用
circuit.cx(qr[0], qr[1]) # CNOTを適用

# 測定
circuit.measure(qr, cr)

"""## リスト6.2: 実行と結果取得(実行する毎に結果は変化します)"""

from qiskit import Aer, execute

# 実行と結果取得
backend = Aer.get_backend('qasm_simulator') # デバイス指定 
job = execute(circuit, backend) # 量子プログラムを実行
result = job.result() # 結果を取得
print(result.get_counts(circuit)) # 結果をテキスト表示

"""## リスト6.4: ヒストグラム表示(実行する毎に結果は変化します)"""

from qiskit.visualization import plot_histogram

# ヒストグラム表示
plot_histogram(job.result().get_counts(circuit))

"""## リスト6.5: 量子回路を描画"""

# 量子回路を描画
circuit.draw(output='mpl')