#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[14]:


cars = pd.read_csv("Cars.csv")
cars.head()


# In[15]:


cars.describe()


# In[16]:


cars.shape


# In[17]:


cars.info()


# In[18]:


cars.isnull()


# In[19]:


cars.isna().sum()


# In[20]:


sns.distplot(cars['MPG'])


# In[21]:


sns.distplot(cars['HP'])


# In[22]:


sns.distplot(cars['VOL'])


# In[23]:


sns.distplot(cars['SP'])


# In[24]:


sns.distplot(cars['WT'])


# In[25]:


sns.boxplot(cars['MPG'])


# In[27]:


sns.boxplot(cars['HP'])


# In[28]:


sns.boxplot(cars['VOL'])


# In[30]:


sns.boxplot(cars['SP'])


# In[31]:


sns.boxplot(cars['WT'])


# In[40]:


x=cars['HP']
y=cars['WT']
scatterplotplot=(x=='feature',y=='target')
plt.scatter(x,y)
plt.show()


# In[41]:


scatterplotplot=(x=='HP',y=='MPG')
plt.show()
plt.scatter(x,y)


# In[42]:


scatterplotplot=(x=='WT',y=='MPG')
plt.show()
plt.scatter(x,y)


# In[43]:


scatterplotplot=(x=='SP',y=='MPG')
plt.show()
plt.scatter(x,y)


# In[44]:


scatterplotplot=(x=='HP',y=='SP')
plt.show()
plt.scatter(x,y)


# In[45]:


cars.corr()


# In[46]:


sns.heatmap(cars.corr(),annot=True)


# In[49]:





# In[ ]:




