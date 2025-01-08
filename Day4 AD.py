#!/usr/bin/env python
# coding: utf-8

# In[1]:


d={101: 4,102: 7,103:2}
d


# In[2]:


l=[5,9,3,4]
l


# In[3]:


l[1]


# In[4]:


d[103]


# In[5]:


d[101]=40


# In[6]:


d


# In[7]:


d.update({102:69})


# In[8]:


d


# In[9]:


d[104]=70     #dictionaries does not find room


# In[10]:


d


# In[11]:


d.update({101:'India'})
d


# In[12]:


d.update({105:'Hyderabad'})


# In[13]:


d


# In[15]:


d.get(105)
d


# In[16]:


d.values()


# In[17]:


d.keys()


# In[19]:


d.items()


# In[22]:


d[104]=[1000,2000,3000,4000]


# In[23]:


d


# In[24]:


type(d)


# In[25]:


type(d[101])


# In[26]:


type(d[102])


# In[27]:


type(d[104])


# In[28]:


d.update({103:(30,40,50,60)})


# In[29]:


d


# In[31]:


type(d[105])


# In[39]:


d[105]={'a':{30,50,60},'b':(1000,4000,5000,9000),'c':['K',{'L':[11,22],'M':(77,88)},'N']}


# In[40]:


d


# In[41]:


d[101]={50:[7,8,9,10],'apple':(20,10,70,[90,180,270])}


# In[42]:


d


# In[46]:


d[101]


# In[48]:


d[101]['apple']


# In[51]:


d[101]['apple'][3][1]


# In[ ]:




