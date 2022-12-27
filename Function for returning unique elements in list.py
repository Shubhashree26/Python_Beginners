#!/usr/bin/env python
# coding: utf-8

# In[6]:


def count_unique(li):
    
    """This function returns the unique elements from list in the same sequence of elements and count of unique elements.
    Input argument: It takes list as input
    Output: It returns new list of unique elements from input list and count of unique elements
    """
    #taking input as list li
    unique = []
    for i in li:
        if li.count(i) == 1:
            unique.append(i)
        elif li.count(i)>1 and unique.count(i) == 0:
            unique.append(i)
    return unique , len(unique)


# In[7]:


li = [100,90,90,0,90,90,160,120]
count_unique(li)


# In[8]:


li2 = ['My', 'Name', 'is', 'Shubhashree', 'and', 'I', 'live', 'in', 'Nagar','and','it','is','near','pune','My']


# In[9]:


len(li2)


# In[11]:


print(count_unique(li2))


# In[ ]:




