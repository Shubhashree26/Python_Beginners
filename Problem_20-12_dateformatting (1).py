#!/usr/bin/env python
# coding: utf-8

# In[7]:


def dateformat(country_region):
    
    """This function gives the correctly formatted date for the country given in input
    input argument: country/continent , User can enter either country name or continent or major region
    Eg. Europe, Asia, United states, Australia, UK, China, Japan, North Korea, South America
    
    """
    #taking input in MM/DD/YY format
    date_in_DDMMYY_format = input("date_in_DDMMYY_format: ")
    if "/" in date_in_DDMMYY_format:
        li = date_in_DDMMYY_format.split("/")
    if "-" in date_in_DDMMYY_format:
        li = date_in_DDMMYY_format.split("-")
    if "." in date_in_DDMMYY_format:
        li = date_in_DDMMYY_format.split(".")
        
    #for MM/DD/YY format
    if country_region.lower() in ["usa" , "us", "united states", "canada","south africa"]:
        date = "/".join([li[1],li[0],li[2]])
        return date
    
    #for DD/MM/YY format
    if country_region.lower() in ["europe", "asia", "north america", "south ameria", "central america" , "australia", "new zealand" , "north africa", "india", "russia", "vietnam", "germany", "iran", "france", "united kingdom", "spain", "poland", "afghanistan", "nepal", "sri lanka"]:
        date = "/".join(li[::])
        return date
    
    #for YY/MM/DD format
    if country_region.lower() in ["china", "japan", "south korea", "north korea", "taiwan", "hungary"]:
        date = "/".join(li[::-1])
        return date
    
    


# In[8]:


dateformat("chiNa")


# In[ ]:




