#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df=sns.load_dataset('titanic')
df


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.sample()


# In[6]:


df.info()


# In[7]:


df['alive'].unique()


# In[8]:


df['alive'].value_counts()


# In[9]:


df.duplicated()


# In[10]:


df.duplicated().sum()


# In[11]:


df[df.duplicated()]


# In[12]:


df.drop_duplicates(inplace=True)


# In[13]:


df


# In[14]:


df.reset_index(drop=True)


# In[15]:


df.reset_index(drop=True,inplace=True)


# In[16]:


df


# In[17]:


df.isnull().sum()


# In[18]:


sns.heatmap(df.isnull())
plt.show


# In[19]:


df.dropna()


# In[20]:


df.drop('deck',axis=1,inplace=True)


# In[21]:


df


# In[22]:


df.columns


# In[23]:


df.isnull().sum()


# In[24]:


df.dtypes


# In[25]:


df['embark_town'].unique()


# In[26]:


df['embark_town']


# In[27]:


df['embark_town'].mode()[0]


# In[28]:


df['embark_town'].fillna(df['embark_town'].mode()[0])


# In[29]:


df['embark_town'].fillna(df['embark_town'].mode()[0],inplace=True)


# In[30]:


df['embark_town'].isnull().sum()


# In[31]:


df['age'].isnull().sum()


# In[32]:


df['age'].median()


# In[33]:


df['age'].fillna(df['age'].median(),inplace=True)


# In[34]:


df['age'].isnull().sum()


# In[35]:


df['embarked'].isnull().sum()


# In[36]:


df['embarked'].fillna(df['embarked'].mode()[0],inplace=True)


# In[37]:


df['embarked'].isnull().sum()


# In[38]:


df.describe()


# In[39]:


df.describe(include='O')


# In[40]:


df['embarked'].unique()


# In[41]:


s=0
c=1
q=2


# In[50]:


df['embarked'].replace({'S':1,'C':2,'Q':3},inplace=True)


# In[51]:


df['embarked']


# In[52]:


df['embarked'].unique()


# In[62]:


df['embarked'].replace({'1':s,'2':c,'3':q},inplace=True)


# In[63]:


df['embarked']


# In[64]:


df['embarked'].unique()


# In[66]:





# In[68]:


df.describe(include='O')


# In[69]:


df['embarked'].unique()


# In[73]:


df['embarked'].replace({1:'S',2:'C',3:'Q'},inplace=True)


# In[74]:


df['embarked'].unique()


# In[78]:


from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
lb.fit_transform(df['embarked'])


# In[80]:


df['embarked'].unique()


# In[81]:


df.info


# In[82]:


df['sex'].unique()


# In[83]:


df['alive'].unique()


# In[ ]:


print('Before', df['embark_town'].unique())
df['embark_town']=lb.fit_transform

