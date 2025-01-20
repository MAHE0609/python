#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd


# In[2]:


a=np.random.randint(30,50,15)


# In[14]:


a


# In[15]:


a[-5:-12:-1]


# In[16]:


a.ndim


# In[17]:


a[12]


# In[19]:


np.random.seed(94)
b=np.random.randint(45,78,(7,8))
b


# In[20]:


b[2]


# In[21]:


b[-1]


# In[22]:


b[:,4]


# In[23]:


b[3,1]


# In[24]:


b[6,4]


# In[25]:


b[1:5]


# In[26]:


b[1:5,1:5]


# In[27]:


b


# In[28]:


b[1:7,1:7]


# In[29]:


np.random.seed(94)
b=np.random.randint(15,50,(7,8))
b


# In[30]:


b[1:7,1:7]


# In[33]:


b[-6:-1,-7:-1]


# In[40]:


b[2,1]


# In[41]:


b[1,0]


# In[42]:


b[0:4,1:7]


# In[ ]:




