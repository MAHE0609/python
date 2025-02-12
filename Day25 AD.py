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


# In[21]:


df


# In[22]:


from sklearn.preprocessing import StandardScaler
stscaler = StandardScaler()
X=stscaler.fit_transform(df)


# In[23]:


X


# In[24]:


import scipy.cluster.hierarchy as sch


# In[25]:


plt.figure(figsize=(20,6))
dendo = sch.dendrogram(sch.linkage(X,method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customer data')
plt.ylabel('Eucl Distance')
plt.show()


# In[26]:


len(set(dendo['color_list']))


# In[27]:


len(set(dendo['color_list']))-1


# In[28]:


from sklearn.cluster import AgglomerativeClustering


# In[29]:


model = AgglomerativeClustering(n_clusters=3)
cluster=model.fit_predict(X)


# In[30]:


cluster


# In[31]:


df


# In[32]:


group_num=pd.DataFrame(cluster,columns=['Group'])
group_num


# In[33]:


cust_group_data=pd.concat([df,group_num],axis=1)
cust_group_data


# In[34]:


from sklearn.metrics import silhouette_score
silhouette_score(X,cluster)


# #kmeans

# In[35]:


X


# In[36]:


from sklearn.cluster import KMeans
wcss=[]
for i in range (2,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)


# In[37]:


wcss


# In[38]:


plt.plot(range(2,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# In[48]:


model = KMeans(n_clusters = 5, random_state = 309)
groups = model.fit_predict(X)
print(groups)


# In[49]:


groups


# In[50]:


groups.shape


# In[51]:


group_num=pd.DataFrame(groups,columns=['Group'])
group_num


# In[52]:


cust_kmeans_data=pd.concat([df,group_num],axis=1)
cust_kmeans_data


# In[53]:


silhouette_score(X,groups)


# In[ ]:





# In[ ]:




