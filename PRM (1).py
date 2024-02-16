#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib. pyplot as plt
x =['2009', '2010', '2011', '2012', '2013', '2014', '2015']
y1=[20.05, 20.46, 21.46, 22.48, 23.59, 24.41, 25.62]
y2=[41.72, 41.07, 42.88, 46.77, 51.13, 56.75, 61.1]
y3=[16.62, 16.46, 17.73, 18.65, 20.25, 21.19, 23.31]
plt.plot(y1, label=('PRM'))
plt.plot(y2, label=('NHblack PRM'))
plt.plot(y3, label=('NHwhite PRM'))
plt.xlabel=("years")
plt.ylabel("range")
plt.title('PREGNANCY-RELATED DEATHS PER 100,000 LIVE BIRTHS')
plt.legend()


# In[ ]:




