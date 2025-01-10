#!/usr/bin/env python
# coding: utf-8

# #for
# while

# In[2]:


x=5
while x<10:
    print('data',x)
    x+=1


# In[4]:


y=[40,20,80,50,30,60,90,]
y


# In[6]:


3*85


# In[7]:


y*2


# In[8]:


for t in y:
    print(t)


# In[9]:


print(t*85)


# In[13]:


for t in y:
    print(t*85)


# In[18]:


z=[]
for t in y:
    z.append(t*5+10)


# In[19]:


z


# In[29]:


num=[81,45,66,33,90,78,67,87,89,93,25,59,9,81]
num


# In[31]:


num=[81,45,66,33,90,78,67,87,89,93,25,59,9,81]
num


# In[32]:


j=[]
k=[]
for i in num:
    if i%2==0:
        j.append(i)
    else:
        k.append(i)


# In[33]:


j


# In[34]:


k


# In[35]:


num


# In[38]:


t=str(78)
t


# In[39]:


t.replace('8','5')


# In[40]:


h=[]
for i in num:
    a=str(i)
    b=a.replace('8','5')
    c=int(b)
    h.append(c)


# In[41]:


h


# In[ ]:




