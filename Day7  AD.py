#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def


# In[ ]:


len


# In[5]:


y='MallA reddy 2025'
y


# In[3]:


len(y)


# In[4]:


y.count('a')


# In[6]:


y


# In[ ]:


def functionname(parameter):
    block of code
    return output


# In[8]:


def calArea(r):
    a=3.14*r*r
    return a
# we use return for find the type of variable


# In[9]:


calArea(r=30)


# In[11]:


w=calArea(r=25)
w


# In[12]:


type(w)


# In[13]:


w+6


# In[16]:


def Aor(l,w):
    area=l*w
    return area

def Aor(l,w):
    area=l*w
    return area
# In[20]:


Aor(l=10,w=5)


# In[27]:


def Area(rad,length,width):
    aoc=3.14*rad*rad
    aor=length*width
    return {'Area of circle':aoc,'Area of rectangle':aor}


# In[28]:


Area(10,20,5)


# In[31]:


t='HyderabAAd 500008 Telangana'
t


# In[30]:


t.count('a')


# In[32]:


def countA(x):
    d=x.lower()
    return d.count('a')


# In[34]:


def count_num_alpha(x):
    c=0
    d=0
    
    for i in x:
        if i.isalpha():
            c+=1
        elif i.isnumeric():
            d+=1
    return {'Number of alphabets':c,'Number of digits':d}


# In[35]:


count_num_alpha(t)


# In[36]:





# In[37]:





# In[38]:





# In[ ]:




