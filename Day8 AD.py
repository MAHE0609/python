#!/usr/bin/env python
# coding: utf-8

# In[1]:


stud_2nd=[18,19,20,19,19,20,20,20,18,18,20,19]


# In[2]:


import numpy as np
np.random.randint(18,21,(200))


# In[4]:


import numpy as np
tenth_std=np.random.randint(15,18,(1000))
tenth_std


# In[7]:


np.random.seed(234)
arr=np.random.randint(20,99,(6,7))


# In[8]:


arr


# In[9]:


arr.size


# In[10]:


m=[5,20,10,6,8]
m


# In[11]:


h=[x**2 for x in m]
h


# In[15]:


for i in range(len(m)):
    m[i]=m[i]**2
    print(m)


# In[16]:


b=(3,6,7,8,9)
b


# In[18]:


h=[x+5 for x in b]
h


# In[19]:


k=[55,25,85,75,35,45,95]
k


# In[20]:


d=[]
for i in k:
    if i<50:
        d.append(i)


# In[21]:


d


# In[22]:


np.random.seed(5)
arr=np.random.randint(20,90,10)


# In[23]:


arr


# In[24]:


arr+5


# In[25]:


arr**2


# In[27]:


arr-20


# In[ ]:




