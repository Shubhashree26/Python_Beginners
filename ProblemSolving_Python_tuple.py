#!/usr/bin/env python
# coding: utf-8

# # Finding Element in tuple

# In[22]:


def find(tuple1,x):
    """
    This Function finds element in a tuple; if element is found, it gives index of the element as output.
    
    Input: 2 arguments. Provide the tuple and the element to search from a tuple. 
    If element is not found, it gives "Not found" as output.
    
    Note: if element is inside a set, it gives index of that particular set element.
    if element is inside a dictionary (keys), it gives index of that particular dictionary element.
    
    """
    
    if x in tuple1:
        return tuple1.index(x)
    else:
        li = []
        for i in tuple1:
            if type(i) == dict:
                if x in i:
                    return tuple1.index(i)
            elif type(i) == set:
                if x in i:
                    return tuple1.index(i)
            elif type(i) not in [int,set,dict]:
                li.append(i)
        tuple2 = tuple(li)
        for i in tuple2:
            for j in i:
                if j == x:
                    return tuple2.index(i) , i.index(j)
        else:
            return "Not found"


# In[23]:


tuple1 = ("Orange", [10, 20, 30], (5, 15, 25),68)
find(tuple1,68)


# In[24]:


new = (('a', 23),('b', 37),('c', 11), ('d',"name", 29),('e',37), {25,65,85}, "hi", {"z":2, "y":8})


# In[25]:


find(new,25)


# In[29]:


find(new,85)


# In[ ]:




