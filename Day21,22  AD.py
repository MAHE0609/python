#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[2]:


cars = pd.read_csv("Cars.csv")
cars.head()


# In[3]:


cars.describe()


# In[4]:


cars.shape


# In[5]:


cars.info()


# In[6]:


cars.isnull()


# In[7]:


cars.isna().sum()


# In[8]:


sns.distplot(cars['MPG'])


# In[9]:


sns.distplot(cars['HP'])


# In[10]:


sns.distplot(cars['VOL'])


# In[11]:


sns.distplot(cars['SP'])


# In[12]:


sns.distplot(cars['WT'])


# In[13]:


sns.boxplot(cars['MPG'])


# In[14]:


sns.boxplot(cars['HP'])


# In[15]:


sns.boxplot(cars['VOL'])


# In[16]:


sns.boxplot(cars['SP'])


# In[17]:


sns.boxplot(cars['WT'])


# In[18]:


x=cars['HP']
y=cars['WT']
scatterplotplot=(x=='feature',y=='target')
plt.scatter(x,y)
plt.show()


# In[19]:


scatterplotplot=(x=='HP',y=='MPG')
plt.show()
plt.scatter(x,y)


# In[20]:


scatterplotplot=(x=='WT',y=='MPG')
plt.show()
plt.scatter(x,y)


# In[21]:


scatterplotplot=(x=='SP',y=='MPG')
plt.show()
plt.scatter(x,y)


# In[22]:


scatterplotplot=(x=='HP',y=='SP')
plt.show()
plt.scatter(x,y)


# In[23]:


cars.corr()


# In[24]:


sns.heatmap(cars.corr(),annot=True)


# In[25]:


sns.heatmap(cars.corr(),annot=True,cmap='Blues')
plt.show()


# In[26]:


scatterplotplot=(x=='HP',y=='VOL')
plt.show()
plt.scatter(x,y)


# In[27]:


scatterplotplot=(x=='HP',y=='SP')
plt.show()
plt.scatter(x,y)


# In[28]:


scatterplotplot=(x=='HP',y=='WP')
plt.show()
plt.scatter(x,y)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




