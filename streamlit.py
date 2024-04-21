#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


a = st.number_input("Enter the first number")
b = st.number_input("Enter the second number")
c = st.number_input("Enter the third number")


# In[4]:


if a>=b and b>=c:
    st.write("Third number is the greatest")
elif b>a and b>c:
    st.write("Second number is the greatest")
else:
    st.write("First number is the greatest")


# In[3]:





# In[ ]:




