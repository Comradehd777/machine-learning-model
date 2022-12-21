#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
A = pd.read_csv(r"D:\lib\Cars93.csv")
A


# In[2]:


from warnings import filterwarnings
filterwarnings("ignore")


# In[3]:


from hdlib import Missingvalue
Missingvalue(A)


# In[4]:


A.isna().sum()


# In[5]:


from hdlib import outliers
out = outliers(A)


# In[8]:


A = A.drop(index=out,axis=0)
A.index = range(0,87)


# In[7]:





# In[9]:


A.shape


# In[ ]:


Y = A[['Weight']]
X = A.drop(labels=['Weight','id','Make','Model'],axis=1)
from hdlib import catcon
catg,cont = catcon()

