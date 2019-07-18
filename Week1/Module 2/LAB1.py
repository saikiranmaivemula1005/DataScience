#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd 
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)
import seaborn as sns


# In[2]:


import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd 
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)
import seaborn as sns


# In[4]:


df=pd.read_csv("https://raw.githubusercontent.com/cs109/2015lab1/master/all.csv", header=None,
               names=["rating", 'review_count', 'isbn', 'booktype','author_url', 'year', 'genre_urls', 'dir','rating_count', 'name'],
)
df.head()


# In[5]:



df.dtypes


# In[11]:


df.shape


# In[7]:



df.shape[0], df.shape[1]


# In[8]:


df.columns


# In[12]:


type(df.rating), type(df)


# In[10]:


df.rating < 3


# In[13]:


np.sum(df.rating < 3)


# In[15]:


print (1*True), (1*False)


# In[16]:



np.sum(df.rating < 3)/df.shape[0]


# In[17]:


np.mean(df.rating < 3.0)


# In[18]:


(df.rating < 3).mean()


# In[19]:


df.query("rating > 4.5")


# In[20]:



df[df.year < 0]


# In[21]:


df[(df.year < 0) & (df.rating > 4)]


# In[22]:


df.dtypes


# In[23]:


df[df.year.isnull()]


# In[24]:


df = df[df.year.notnull()]
df.shape


# In[25]:



df['rating_count']=df.rating_count.astype(int)
df['review_count']=df.review_count.astype(int)
df['year']=df.year.astype(int)


# In[26]:


df.dtypes


# In[27]:


df.rating.hist();


# In[37]:


sns.set_context("notebook")
meanrat=df.rating.mean()
print (meanrat, np.mean(df.rating), df.rating.median())
with sns.axes_style("whitegrid"):
    df.rating.hist(bins=30, alpha=0.4);
    plt.axvline(meanrat, 0, 0.75, color='y', label='Mean')
    plt.xlabel("average rating of book")
    plt.ylabel("Counts")
    plt.title("Ratings Histogram")
    plt.legend()


# In[44]:


df.review_count.hist(bins=np.arange(0, 40000, 300))


# In[45]:


df.review_count.hist(bins=100)
plt.xscale("log");


# In[49]:


plt.scatter(df.year, df.rating, lw=0, alpha=.08)
plt.xlim([1900,2010])
plt.xlabel("Year")
plt.ylabel("Rating")


# In[ ]:




