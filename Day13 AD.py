#!/usr/bin/env python
# coding: utf-8

# In[8]:


import seaborn as sns
import matplotlib.pyplot as plt
iris_data=sns.load_dataset('iris')
iris_data


# In[9]:


sns.boxplot(x=iris_data['sepal_width'],color='red')
plt.show()


# In[10]:


sns.boxplot(x=iris_data['sepal_width'],palette=['violet','red','lightgreen'],y=iris_data['species'])
plt.show()


# In[15]:


df=sns.load_dataset('taxis')
df


# In[14]:


sns.scatterplot(x=df['fare'],y=df['total'],palette=['yellow','red'],hue=df['payment'])
plt.show()


# In[16]:


sns.scatterplot(x=df['fare'],y=df['total'])
plt.show()


# In[20]:


sns.stripplot(x=df['fare'],y=df['payment'],palette=['blue','red'],hue=df['color'])


# In[ ]:


sns.lineplot(x=df['total'],y=df['fare'])
plt.show()


# In[ ]:





# In[ ]:


sns.lineplot(x=df['total'],y=df['fare'],hue=df['payment'],palette=['green','orange'])
plt.show()


# In[ ]:


sns.countplot(x=df['payment'])
plt.show()


# In[ ]:




