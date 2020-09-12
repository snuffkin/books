#!/usr/bin/env python
# coding: utf-8

# # 第6章のソースコード

# ## リスト6.1: 量子回路の作成

# In[1]:


from braket.circuits import Circuit

# 量子回路の組み立て
circuit = Circuit().h(0).cnot(0, 1)


# ## リスト6.2: 実行と結果取得(実行する毎に結果は変化します)

# In[2]:


from braket.devices import LocalSimulator

# デバイス指定
device = LocalSimulator()

# 実行と結果取得
task = device.run(circuit, shots=1000) # 量子プログラムを実行
result = task.result() # 結果を取得
counts = result.measurement_counts # 各測定値を得た回数を取得
print(counts) # 結果をテキスト表示


# ## リスト6.4: ヒストグラム表示(実行する毎に結果は変化します)

# In[3]:


import matplotlib.pyplot as plt

# ヒストグラム表示
plt.bar(counts.keys(), counts.values())
plt.xlabel('bitstrings')
plt.ylabel('counts')


# ## リスト6.5: 量子回路を描画

# In[4]:


# 量子回路を描画
print(circuit)

