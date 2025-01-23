#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[5]:


df=pd.read_csv(r"C:\Users\ramak\OneDrive\Desktop\customers-100.csv")
df


# In[19]:


df=sns.load_dataset('taxis')
df


# In[20]:


sns.barplot(x='payment',y='total',data=df,color='red',estimator='mean')
plt.show()
plt.tight_layout()


# In[21]:


sns.histplot(x=df['fare'],color='blue')


# In[22]:


sns.histplot(x=df['fare'],palette=['blue','red'],hue=df['payment'])
plt.show


# In[23]:


sns.boxplot(x=df['fare'],color='skyblue')


# In[24]:


iris_data=sns.load_dataset('iris')
iris_data


# In[25]:


sns.boxplot(x=iris_data['sepal_length'],color='lightgreen')
plt.show()


# lower_bound= q1-1.5(q3-q1)
# 
# upper_bound= q3+1.5(q3-q1)

# In[26]:


sns.distplot(x=df['fare'],hist=True,kde=True)
plt.show()


# In[ ]:




