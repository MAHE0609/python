#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.cluster import DBSCAN
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("Wholesale customers data.csv")
df.head()


# In[3]:


df.describe()


# In[4]:


df.isnull()


# In[5]:


df.info()


# In[6]:


df.duplicated()


# In[7]:


df.shape


# In[8]:


df.sum()


# In[9]:


df.duplicated()


# In[10]:


import seaborn as sns


# In[11]:


sns.countplot(x=df['Region'])
plt.show()


# In[12]:


sns.countplot(x=df['Channel'])
plt.show()


# In[13]:


sns.countplot(x=df['Fresh'])
plt.show()


# In[14]:


import warnings
warnings.filterwarnings('ignore')


# In[15]:


sns.distplot(df['Grocery'])
plt.show()


# In[16]:


sns.distplot(df['Frozen'])
plt.show()


# In[17]:


sns.distplot(df['Milk'])
plt.show()


# In[18]:


sns.distplot(df['Detergents_Paper'])
plt.show()


# In[19]:


sns.distplot(df['Delicassen'])
plt.show()


# In[20]:


df.drop(['Channel','Region'],axis=1,inplace=True)


# In[22]:


df


# In[23]:


from sklearn.preprocessing import StandardScaler
stscaler = StandardScaler()
X=stscaler.fit_transform(df)


# In[24]:


X


# In[25]:


import scipy.cluster.hierarchy as sch


# In[31]:


plt.figure(figsize=(20,6))
dendo = sch.dendrogram(sch.linkage(X,method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customer data')
plt.ylabel('Eucl Distance')
plt.show()


# In[32]:


len(set(dendo['color_list']))


# In[33]:


len(set(dendo['color_list']))-1


# In[34]:


from sklearn.cluster import AgglomerativeClustering


# In[36]:


model = AgglomerativeClustering(n_clusters=3)
cluster=model.fit_predict(X)


# In[37]:


cluster


# In[38]:


df


# In[39]:


group_num=pd.DataFrame(cluster,columns=['Group'])
group_num


# In[41]:


cust_group_data=pd.concat([df,group_num],axis=1)
cust_group_data


# In[43]:


from sklearn.metrics import silhouette_score
silhouette_score(X,cluster)


# #kmeans

# In[45]:


X


# In[50]:


from sklearn.cluster import KMeans
wcss=[]
for i in range (2,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)


# In[51]:


wcss


# In[ ]:




