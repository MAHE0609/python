#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[6]:


df=sns.load_dataset('taxis')
df


# In[7]:


df.sample(5)


# In[8]:


df['color']


# In[9]:


df['color'].isnull().sum()


# In[10]:


df.isnull().sum()


# In[11]:


df['payment'].isnull().sum()


# In[12]:


(44/6433)*100


# In[13]:


(26/6433)*100


# In[14]:


(df.isnull().sum()/df.shape[0])*100


# missing data handling
# 1) Imputation (fill in the blanks)
#     1) statistical measures
#     2) parameter
# 2) Delete data
#     1) rows
#     2) columns

# In[15]:


df.drop('pickup_zone',axis=1)


# In[18]:


df.drop(['pickup','color','payment','total'],axis=1,inplace=True)
df


# In[19]:


df


# In[20]:


df.drop([2,3,6430,6432],axis=0,inplace=True)


# In[21]:


df


# In[26]:


a=np.random.randint(10,50,15)


# In[32]:


a


# In[33]:


a[a>40]


# In[34]:


df.iloc[5605]


# In[35]:


df=sns.load_dataset('taxis')


# In[36]:


df


# In[37]:


df[df['color']=='yellow']


# In[38]:


df[df['total']>15]


# In[39]:


df[df['payment']=='cash']


# In[40]:


df['payment']=='cash'


# In[41]:


condition1=df['payment']=='cash'


# In[42]:


df[condition1]


# In[ ]:




