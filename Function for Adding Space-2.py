#!/usr/bin/env python
# coding: utf-8

# # Function for Adding Space between Potential Words

# Input list =  ['ItReturnsListOfStringsWhichHaveAddedSpaceBeforeCapitalWords']
# 
# Output =  ['It', 'Returns', 'List', 'Of', 'Strings', 'Which', 'Have', 'Added', 'Space', 'Before', 'Capital', 'Words']

# In[1]:


def addspace(lis):
    """
    Given list of Strings, This function adds a space before sequence which begin with capital letters.
    Input argument: It takes list of strings as input
    Output: It returns list of strings which have added space before each capital letter in string, which
    potentially can be next word.
    """
        
    lis2 = []

    for i in lis:
        for j in i:
            if j.isupper():
                i = i.replace(j," "+j)
        lis2.extend(i.split())
    return lis2


# In[3]:


t = [ 'NewYear', 'CelebrationBegins', 'thisMonday']
addspace(t)


# In[4]:


n = ['ItReturnsListOfStringsWhichHaveAddedSpaceBeforeCapitalWords', 'ItIsUsefulFunction']
print(addspace(n))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




