#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.cluster import DBSCAN
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv("Wholesale customers data.csv")
df.head()


# In[4]:


df.describe()


# In[5]:


df.isnull()


# In[6]:


df.info()


# In[7]:


df.duplicated()


# In[13]:


df.shape


# In[14]:


df.sum()


# In[15]:


df.duplicated()


# In[16]:


import seaborn as sns


# In[17]:


sns.countplot(x=df['Region'])
plt.show()


# In[18]:


sns.countplot(x=df['Channel'])
plt.show()


# In[19]:


sns.countplot(x=df['Fresh'])
plt.show()


# In[25]:


import warnings
warnings.filterwarnings('ignore')


# In[26]:


sns.distplot(df['Grocery'])
plt.show()


# In[27]:


sns.distplot(df['Frozen'])
plt.show()


# In[28]:


sns.distplot(df['Milk'])
plt.show()


# In[29]:


sns.distplot(df['Detergents_Paper'])
plt.show()


# In[30]:


sns.distplot(df['Delicassen'])
plt.show()


# In[31]:


import sklearn.preprocessing as standardScaler
sns.scaler


# In[ ]:




