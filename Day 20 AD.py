#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
data = pd.read_csv("NewspaperData.csv")
data.head()


# In[7]:


data.info()


# In[8]:


data


# In[9]:


data.sample(10)


# In[10]:


data.drop('Newspaper',axis=1).corr()


# In[11]:


import warnings
warnings.filterwarnings('ignore')


# In[12]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[13]:


sns.distplot(data['daily'])


# In[15]:


sns.distplot(data['sunday'])
plt.show()


# In[17]:


import statsmodels.formula.api as smf
model = smf.ols("sunday~daily",data = data).fit()


# In[18]:


sns.regplot(x="daily", y="sunday", data=data,ci=None);


# In[20]:


data.head()


# In[21]:


model.params


# In[22]:


print(model.tvalues, '\n', model.pvalues)


# In[23]:


(model.rsquared,model.rsquared_adj)


# In[ ]:




