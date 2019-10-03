#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd


# In[25]:


def parse_input(list):
    input = pd.DataFrame(list)
    return input.to_csv('thing.csv')


# In[ ]:




