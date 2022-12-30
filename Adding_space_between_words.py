#!/usr/bin/env python
# coding: utf-8

# # Function for Adding Space between Potential Words

# In[43]:


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
        lis2.append(i)
    return lis2
        


# In[44]:


lis1 = ['gtgBest', 'forNewbi','andComputerScienceStudents','sdfG','ssdf']


# In[45]:


addspace(lis1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#another approach


# In[ ]:


li = ['gfgBest', 'forGeeks','andComputerScienceStudents','sdfDFG']
li2 = []
for i in li:
    new = ""
    for j in i:
        if j.isupper():
            new += " " + j
        else:
            new += j
    li2.append(new)
print(li2)

