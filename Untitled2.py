#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=set([1,2,3,4,5,6,7])
b=set([10,20])
mn=a|b
mn


# a=set([1,2,3,4,5,6,7])
# b=set([10,20])
# mn=a&b 
# 

# In[6]:


a=set([1,2,3,4,5,6,7])
b=set([10,20])
mn=a-b
mn


# In[7]:


a=set([1,2,3,4,5,6,7])
b=set([10,20])
mn.add("Здравствуйте ")
mn


# In[9]:


a=set([1,2,3,4,5,6,7])
b=set([10,20])
mn.add("Здравствуйте ")
mn.update([55,57,56])
mn


# In[11]:


a=set([1,2,3,4,5,6,7])
b=set([10,20])
mn.add("Здравствуйте ")
mn.update([55,57,56])
mn.remove(4)
mn


# In[ ]:





# In[12]:


z,z1=("Book",10)
z


# In[15]:


z1


# In[16]:


z,z1=("Book",10)
z,z1=z1,z
z


# In[17]:


z1


# In[ ]:




