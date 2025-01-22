#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[10]:


k=[4,2,9,87.9999,40]
k


# In[11]:


pd.Series(k)


# In[79]:


a=np.random.randint(20,50,15)
a


# In[80]:


a.ndim


# In[82]:


s=pd.Series(a)
s


# In[83]:


s[0]


# In[84]:


s[4:10]


# In[89]:


np.random.seed(34)
b=np.random.randint(100,200,(6,5))


# In[90]:


b.ndim


# In[91]:


b.shape


# In[92]:


b


# In[95]:


df=pd.DataFrame(b,columns=['Roll','name','age','addr','country'])
df


# In[99]:


df.iloc[[0,5]]


# In[102]:


df


# In[103]:


df['age']


# In[ ]:


df[[]]

