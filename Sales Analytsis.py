#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Upon initial inspection of the data, we can start thinking of some questions about it that we would want to answer.

## 1 What is the overall sales trend?

## 2 Which are the Top 10 products by sales?

## 3 Which are the Most Selling Products?

## 4 Which is the most preferred Ship Mode?

## 5 Which are the Most Profitable Category and Sub-Category?

import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_excel('F:/Python/Sale analysis/superstore_sales.xlsx')


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.shape


# In[7]:


df.info()


# In[8]:


df.isna().sum()


# In[9]:


df.describe()


# In[10]:


df.describe().round()


# In[11]:


####EXPLORATORY DATA ANALYSIS


# In[12]:


##What is the overall Sales Trend?


# In[14]:


# Getting month year from order_date
df['month_year'] = df['order_date'].apply(lambda x: x.strftime('%Y-%m'))


# In[15]:


df['month_year']


# In[16]:


# grouping month_year by sales
df1 = df.groupby('month_year')['sales'].sum()


# In[17]:


df1


# In[18]:


# grouping month_year by sales
df1 = df.groupby('month_year')['sales'].sum().reset_index()


# In[19]:


df1


# In[23]:


plt.figure(figsize=(16,5))
plt.plot(df1['month_year'], df1['sales'], color = 'blue')
plt.xticks(rotation='vertical', size=8)
plt.show()


# In[24]:


#which are the top 10 products by sales?


# In[26]:


#grouping products ny sales
prod_sales = pd.DataFrame(df.groupby('product_name')['sales'].sum())
#sorting the dataframe in decending order
prod_sales.sort_values(by=['sales'], inplace = True, ascending=False)
#top 10 products by sales
prod_sales[:10]


# In[27]:


#Which are the most selling products?


# In[28]:


#grouping products by quantity
best_selling_prods = pd.DataFrame(df.groupby('product_name')['quantity'].sum())
#sprting the datframe in decending order
best_selling_prods.sort_values(by=['quantity'], inplace=True, ascending=False)
#Most selling products
best_selling_prods[:10]


# In[29]:


#what is the most preferred ship mode?


# In[30]:


#setting the figure size
plt.figure(figsize=(10,8))
sns.countplot(x='ship_mode', data=df)
plt.show()


# In[31]:


#Which are the most profitable category and Sub-Category?


# In[32]:


#Grouping products by category and Sub-Category
cat_subcat = pd.DataFrame(df.groupby(['category', 'sub_category']).sum()['profit'])
cat_subcat.sort_values(['category', 'profit'], ascending=False)


# In[ ]:




