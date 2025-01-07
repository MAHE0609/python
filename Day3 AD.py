#!/usr/bin/env python
# coding: utf-8

# In[8]:


h=(90,70,50,30,20,50,30,10,50,20,20,20,90,80,60,60,60,60)
h


# In[2]:


type(h)


# In[9]:


h.count(60)


# In[12]:


h.index(60)


# In[10]:


h.count(20)


# In[13]:


h[3]


# In[14]:


h[0]


# In[15]:


h[0:3]


# In[16]:


s={80,70,30,80,60,30,10,20}
s


# In[17]:


type(s)


# In[19]:


s.add(90)
s


# In[20]:


s.remove(80)
s


# In[27]:


y={40,30,60,20,90,10}
y


# In[28]:


s.intersection(y)


# In[29]:


s.union(y)


# In[30]:


s.difference(y)


# In[31]:


y.difference(s)


# In[32]:


s.symmetric_difference(y)


# In[33]:


y.symmetric_difference(s)


# In[41]:


y={40,30,60,20,90,10}
y


# In[42]:


tuple(y)


# In[43]:


list(y)


# In[ ]:




