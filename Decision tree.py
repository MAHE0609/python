#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install streamlit')


# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix


# In[2]:


data=pd.read_csv("Heart_Disease_Dataset.csv")


# In[3]:


data.head()


# In[4]:


data.shape


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


data.isnull().sum()


# In[8]:


data.duplicated()


# In[9]:


len(data[data.duplicated()])


# In[10]:


for column in data.columns:
    print(data[column].value_counts())


# In[12]:


data['Diabetic'].value_counts()


# In[14]:


data=pd.get_dummies(data,columns=['Diabetic'],drop_first=True)
data.head()


# In[15]:


binary_columns=["Smoking","AlcoholDrinking","Stroke","DiffWalking",'PhysicalActivity',"Asthma",'KidneyDisease', 'SkinCancer']
for col in binary_columns:
    data[col]=data[col].map({'Yes':1,"No":0})


# In[16]:


data


# In[17]:


data=pd.get_dummies(data,columns=['Sex','AgeCategory','Race','GenHealth'],drop_first=True)
data.head()


# In[18]:


data.isnull().sum()


# In[19]:


x=data.drop(columns=['HeartDisease'],axis=1)
y=data['HeartDisease'].map({'Yes':1,'No':0})


# In[20]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)


# In[23]:


clf=DecisionTreeClassifier(max_depth=5,criterion='gini',random_state=42)
clf.fit(x_train,y_train)


# In[24]:


y_pred=clf.predict(x_test)


# In[25]:


accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)
f1=f1_score(y_test,y_pred)
roc_auc=roc_auc_score(y_test,y_pred)


# In[ ]:




