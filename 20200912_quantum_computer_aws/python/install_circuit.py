#!/usr/bin/env python
# coding: utf-8

# # インストール

# In[1]:


get_ipython().system('pip install amazon-braket-sdk')


# # 1量子ビットの量子回路

# In[2]:


from braket.circuits import Circuit
from braket.devices import LocalSimulator

device = LocalSimulator()

circuit = Circuit().h(0)

print(circuit)


# In[3]:


from braket.circuits import Circuit
from braket.devices import LocalSimulator

device = LocalSimulator()

circuit = Circuit().x(0)

print(circuit)


# In[4]:


from braket.circuits import Circuit
from braket.devices import LocalSimulator

device = LocalSimulator()

circuit = Circuit().z(0)

print(circuit)


# In[5]:


from braket.circuits import Circuit
from braket.devices import LocalSimulator

device = LocalSimulator()

circuit = Circuit().i(0)

print(circuit)


# In[6]:


from braket.circuits import Circuit
from braket.devices import LocalSimulator

device = LocalSimulator()

circuit = Circuit().x(0).h(0)

print(circuit)


# # 2量子ビットの量子回路

# In[7]:


from braket.circuits import Circuit
from braket.devices import LocalSimulator

device = LocalSimulator()

circuit = Circuit().h(0).cnot(0, 1)

print(circuit)


# In[8]:


from braket.circuits import Circuit
from braket.devices import LocalSimulator

device = LocalSimulator()

circuit = Circuit().cnot(0, 1)

print(circuit)


# In[9]:


from braket.circuits import Circuit
from braket.devices import LocalSimulator

device = LocalSimulator()

circuit = Circuit().cnot(1, 0)

print(circuit)


# In[10]:


from braket.circuits import Circuit
from braket.devices import LocalSimulator

device = LocalSimulator()

circuit = Circuit().swap(1, 0)

print(circuit)

