#!/usr/bin/env python
# coding: utf-8

# In[1]:




def type_validation(variable, _type): 
    #check type of variable passed and convert it to string 
    var_type = str(type(variable))
    #check if var_type contains _type
    if _type in var_type:
        return True
    else:
        return False


# In[ ]:




