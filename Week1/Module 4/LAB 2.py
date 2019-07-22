#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[61]:


req = requests.get("https://en.wikipedia.org/wiki/Harvard_University")


# In[3]:


req = requests.get("https://en.wikipedia.org/wiki/Harvard_University")


# In[4]:


req


# In[5]:


type(req)


# In[6]:


dir(req)


# In[7]:


page = req.text
page


# In[9]:


from bs4 import BeautifulSoup


# In[10]:


soup = BeautifulSoup(page, 'html.parser')


# In[11]:


soup


# In[12]:


type(page)


# In[13]:


type(soup)


# In[15]:


print (soup.prettify())


# In[16]:


soup.title


# In[17]:


"title" in dir(soup)


# In[18]:


soup.p


# In[19]:


soup.find_all("p")


# In[20]:


len(soup.find_all("p"))


# In[21]:


soup.table["class"]


# In[22]:


[t["class"] for t in soup.find_all("table") if t.get("class")]


# In[66]:


my_list = []
for t in soup.find_all("table"):
    if t.get("class"):
        my_list.append(t["class"])
my_list


# In[67]:


table_html = str(soup.findAll("table", "wikitable")[2])


# In[68]:


from IPython.core.display import HTML

HTML(table_html)


# In[70]:


rows = [row for row in soup.findAll("table", "wikitable")[2].find_all("tr")]
rows


# In[86]:


rem_nl = lambda s: s.replace("\n", "")


# In[32]:


def power(x, y):
    return x**y

power(2, 3)


# In[37]:


def print_greeting():
    print ("Hellooooo")
    
print_greeting()


# In[36]:


def get_multiple(x, y=1):
    return x*y

print ("With x and y: ", get_multiple(10, 2))
print ("With x only: ", get_multiple(10))


# In[41]:


def print_special_greeting(name, leaving=False, condition="nice"):
    print ("Hi", name)
    print ("How are you doing in this", condition, "day?")
    if leaving:
        print ("Please come back!")
print_special_greeting("Sai Kiranmai")
print_special_greeting("John", True, "rainy")


# In[42]:


def print_siblings(name, *siblings):
    print (name, "has the following siblings:")
    for sibling in siblings:
        print (sibling)
    print
        
print_siblings("John", "Ashley", "Lauren", "Arthur")
print_siblings("Mike", "John")
print_siblings("Terry")


# In[43]:


def print_brothers_sisters(name, **siblings):
    print (name, "has the following siblings:")
    for sibling in siblings:
        print (sibling, ":", siblings[sibling])
    print
    
print_brothers_sisters("John", Ashley="sister", Lauren="sister", Arthur="brother")


# In[87]:


columns = [rem_nl(col.get_text()) for col in rows[0].find_all("th") if col.get_text()]
columns
    


# In[88]:


indexes = [rem_nl(row.find("th").get_text()) for row in rows[1:]]
indexes


# In[89]:


HTML(table_html)


# In[90]:


to_num = lambda s: s[-1] == "%" and int(s[:-1]) or None


# In[91]:


values = [to_num(rem_nl(value.get_text())) for row in rows[1:] for value in row.find_all("td")]
values


# In[97]:


stacked_values = zip(*[values[i::3] for i in range(len(columns))])
list(stacked_values)


# In[93]:


HTML(table_html)


# In[96]:


# passing parameters
def print_args(arg1, arg2, arg3):
    print (arg1, arg2, arg3)

print_args(1, 2, 3)

print_args([1, 10], [2, 20], [3, 30])


# In[82]:


#container
parameters = [100, 200, 300]

p1 = parameters[0]
p2 = parameters[1]
p3 = parameters[2]

print_args(p1, p2, p3)


# In[83]:


p4, p5, p6 = parameters

print_args(p4, p5, p6)


# In[84]:


#exploding is the best way...
print_args(*parameters)


# In[99]:


#PANDAS Dataframe

import pandas as pd

stacked_values = zip(*[values[i::3] for i in range(len(columns))])
#create a data frame
df = pd.DataFrame(stacked_values, columns=columns, index=indexes)
df


# In[100]:


#other ways of creating data frame:
#1. converting into key-value pair

stacked_values = zip(*[values[i::3] for i in range(len(columns))])
columns = [rem_nl(col.get_text()) for col in rows[0].find_all("th") if col.get_text()]
data_dicts = [{col: val for col, val in zip(columns, col_values)} for col_values in stacked_values]
data_dicts


# In[101]:


pd.DataFrame(data_dicts, index=indexes)


# In[102]:


# Group values column wise
stacked_by_col = [values[i::3] for i in range(len(columns))]
stacked_by_col


# In[104]:


#to revert the pattern, we create a list of dictionaries
data_lists = {col: val for col, val in zip(columns, stacked_by_col)}
data_lists

pd.DataFrame(data_lists, index=indexes)


# In[105]:


# Dataframe cleanup
df.dtypes


# In[106]:


# drop columns which have null values
df.dropna()


# In[107]:


df.dropna(axis=1)


# In[108]:


# Replace null with zero
df_clean = df.fillna(0).astype(int)
df_clean


# In[109]:


df_clean.dtypes


# In[110]:


#statistics of table
df_clean.describe()


# In[112]:


#NUMPY
#The values method of the DataFrame will return a two-dimensional array with the DataFrame values. 
import numpy as np
df_clean.values


# In[113]:


type(df_clean.values)


# In[116]:


#mean of a column
np.mean(df_clean.Undergrad)


# In[117]:


np.std(df_clean)


# In[119]:


# Data frame indexing

df_clean["Undergrad"]


# In[121]:


df_clean.Undergrad


# In[123]:


df_clean.loc["Asian/Pacific Islander"]


# In[124]:


df_clean.iloc[0]


# In[125]:


#not preferable
df_clean.ix["Asian/Pacific Islander"]


# In[126]:


df_clean.ix[0]


# In[128]:


df_clean.loc["White/non-Hispanic", "Graduate"]


# In[129]:


#Split Apply Combine pattern

df_flat = df_clean.stack().reset_index()
df_flat.columns = ["race", "source", "percentage"]
df_flat


# In[132]:


#group tasks
grouped = df_flat.groupby("race")
print(grouped.groups)
type(grouped)


# In[134]:


mean_percs = grouped.mean()
print(mean_percs)
type(mean_percs)


# In[136]:


#Iterate over groups
for name, group in df_flat.groupby("source", sort=True):
    print (name)
    print (group)


# In[138]:


#Simple plotting
get_ipython().run_line_magic('matplotlib', 'inline')
mean_percs.plot(kind="bar");

