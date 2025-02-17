#!/usr/bin/env python
# coding: utf-8

# In[11]:


# !pip install mlxtend


# In[12]:


import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules
import warnings
warnings.filterwarnings('ignore')


# In[13]:


titanic = pd.read_csv("Titanic.csv")
titanic.head()


# In[14]:


titanic['Class']


# In[15]:


titanic['Class'].unique()


# In[16]:


titanic['Gender'].unique()


# In[17]:


titanic['Age'].unique()


# In[18]:


titanic['Survived'].unique()


# In[19]:


df=pd.get_dummies(titanic,dtype='int')
df.head()


# In[21]:


frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)
frequent_itemsets


# In[23]:


rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1,num_itemsets=len(frequent_itemsets))
rules


# In[24]:


rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules


# In[ ]:





# In[ ]:





# In[ ]:




