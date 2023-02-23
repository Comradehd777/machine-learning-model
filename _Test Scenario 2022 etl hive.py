#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
from warnings import filterwarnings
filterwarnings("ignore")


# In[4]:




A = pd.read_csv(r"D:\lib\Cars93.csv")
A


# In[13]:


r = pd.set_option("display.max_rows").tail(34)


# In[5]:


A.head(50)


# In[6]:


pd.set_option('display.max_columns',22)
pd.set_option('display.max_rows',68)


# In[23]:


A


# In[24]:


A.groupby('AirBags')[['Weight']].mean()


# In[47]:


A.iloc[52:78:93]


# In[48]:


A.iloc[91:45:33]


# In[125]:


A.iloc[[52,91,46],:]


# In[78]:


A[A.Price<20]['Make'].head(34)


# In[81]:


g = A.Horsepower.max()
g


# In[84]:


A[A.Horsepower == g][['Model']]


# In[90]:


j = A.Price.mean()
A[A.Price > j][['Make']]


# In[93]:


A.sort_values(by='Price').tail(5).Price.sum()


# In[9]:


A.groupby(by='Type')['Price'].mean().plot(kind='hist')


# In[95]:


A.groupby(by='Type')['Price'].mean().plot(kind='bar')


# In[101]:


A.groupby(by='Type')['Price'].mean().plot(kind='hist')


# In[102]:


A[(A['Min.Price']>18)&(A['Min.Price']<30)][['Make','Model']]


# In[104]:


A['hp_new'] = A.Horsepower*1.912


# In[105]:


A.sort_values(by=["hp_new"],ascending=False)


# In[107]:


A.sort_values(by=["hp_new"],ascending=False,inplace=True)


# In[116]:


A.columns.size


# In[118]:


A.index = range(0,93,1)


# In[123]:


A.shape


# In[13]:


A.iloc[50:,1:8]


# In[ ]:




