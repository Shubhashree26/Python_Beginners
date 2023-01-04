#!/usr/bin/env python
# coding: utf-8

# # Write a Python function to check whether a string is Pangram or not.
# Note: A Pangram is a sentence containing every letter of the alphabet series.
# 
# Example:
# A quick brown fox jumps over the lazy dog.

# In[5]:


def pangram(string):
    """
    This Python function checks whether a string is Pangram or not.
    Input: any string
    Output: Pangram or Not Pangram
    
    """
    
    for i in range(97,123):
        if chr(i) in string.lower():
            pass
        else:
            return "Not Pangram"
    return "Pangram"


# In[6]:


pangram("A quick brown fox jumps over the lazy dog")


# In[7]:


pangram ("A Pangram is a sentence containing every letter of the alphabet series")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




