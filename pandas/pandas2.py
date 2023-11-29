#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


products = ['A','B','C','D']


# In[3]:


products


# In[5]:


type(products)


# In[6]:


product_cat = pd.Series(products)


# In[7]:


product_cat


# In[8]:


type(product_cat)


# In[9]:


profits = pd.Series({
    '7/4/2014':2000,
    '1/2/2015':1500,
    '10/28/2019':4000,
    '4/24/2014':2000,
    '3/29/2014':2100
})


# In[18]:


profits


# In[12]:


profits.sum()


# In[13]:


profits.min()


# In[14]:


profits.max()


# In[16]:


profits.idxmax()


# In[17]:


profits.idxmin()


# In[19]:


profits.head()


# In[20]:


profits.tail()


# In[21]:


profits.head(2)


# In[22]:


profits.tail(2)


# In[6]:


import pandas as pd
info = {'id': [101,102,103],
       'dept':['Bsc','MSc','M.Tech']
       }

dbs = pd.DataFrame(info)


# In[7]:


dbs


# In[8]:


type(dbs)


# In[9]:


x = ['Python','Java']
data1 = pd.DataFrame(x)


# In[12]:


import pandas as pd


# In[30]:


info={
    'one': pd.Series([1,2,3,4,5,6,7,8], index=['a','b','c','d','e','f','g','h']),
    'two': pd.Series([1,2,3,4,5,6,7,8], index=['a','b','c','d','e','f','g','h'])
}


# In[31]:


data2 = pd.DataFrame(info)


# In[32]:


data2


# In[33]:


data2['one']


# In[34]:


data2['two']


# In[35]:


data2['three'] = pd.Series([10,20,30,40,50,60,70,80],index=['a','b','c','d','e','f','g','h'])


# In[36]:


data2


# In[37]:


data2['four'] = data2['one']+data2['two']


# In[38]:


data2


# In[39]:


data2['three'] = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])


# In[40]:


data2


# In[41]:


data2['four'] = data2['two']+data2['three']


# In[42]:


data2


# In[43]:


del data2['four']


# In[44]:


data2


# In[45]:


data2.pop('three')


# In[46]:


data2


# In[47]:


list1 = pd.DataFrame({
    "x":[10,20,30],
    "y":[30,40,50]

})


# In[48]:


list1


# In[52]:


list2 = pd.DataFrame({
    "m":[100,200,300],
    "n":[300,400,500]

})


# In[53]:


list2


# In[54]:


list1.append(list2)


# In[59]:


data3 = pd.DataFrame([[2,3]]*4, columns=['A','B'])


# In[60]:


data3


# In[62]:


import numpy as np
data3.apply(np.sqrt)


# In[63]:


def mul(a):
    return 2*a


# In[64]:


method1 = mul


# In[65]:


data2.apply(method1)


# In[66]:


data3.apply(lambda x:2*x)


# In[67]:


emps = {
    "names":["praveen","kumar","sunil","praveen"],
    "age":[39,31,24,39]
}
data5 = pd.DataFrame(emps)


# In[68]:


data5


# In[78]:


data6 = data5.drop_duplicates(keep='first',inplace=False)


# In[79]:


data5


# In[80]:


data6


# In[88]:


pddata = pd.read_csv('e://data/sales-products.csv')


# In[89]:


type(pddata)


# In[90]:


pddata


# In[91]:


cleandata = pddata.drop_duplicates()


# In[96]:


cleandata


# In[97]:


writer = pd.ExcelWriter('e://data/cleandata.xlsx')
cleandata.to_excel(writer)
writer.save()
print("Clean data is saved")


# In[ ]:




