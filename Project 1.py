#!/usr/bin/env python
# coding: utf-8

# # Proof of Central Limit Theorem of Statistics
#                 

# In[4]:


import numpy as np
from numpy.random import randn
n=1000 #sample size
counter=0
for i in randn(n): #to generate the norammly distributed random numbers
    if -1<i<1:     #range of our sample size 
        counter+=1 
print("count=",counter) #count of numbers occuring between -1 to 1 put of 1000
print("mean=",(counter/n)) #average of numbers occuring between -1 to 1
print("percentage=",(counter/n)*100)  #percentage of occuring between -1 to 1


# In[ ]:




