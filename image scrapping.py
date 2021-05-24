#!/usr/bin/env python
# coding: utf-8

# In[50]:


#list = ['a', 'b', 'c', 'd', 'e']

#for i in list:
    #print(i)


# In[51]:


#for i in enumerate(list):
    #print(i)


# In[2]:


from bs4 import *
import requests as rq
import os


# 1. 'bs4' is a library which get the entire web page in a text format and parse that as html.
# 2. 'requests' helps you to send that request to the web page
# 3. 'os' is operating system module which helps in creating a directory. I want to store my images in aprticular folder and also write some files in a desk. That's why this module is used.

# In[3]:


import time


r2 = rq.get("http://books.toscrape.com/")
soup2 = BeautifulSoup(r2.text, "html.parser")


# In[4]:


#print(soup2.prettify)


# In[5]:


images = soup2.find_all('img')
example = images[0]
example


# In[6]:


print(type(images))


# The part that is most important for us in pulling the actual image is **src=…** because this is the URL. Well, it’s not quite fully a URL, but a URL extension. 

# To breakdown the output a little bit more, we can use the **.attrs** method to pull out the URL found in **src=…**

# In[7]:


example.attrs


# In[8]:


example['src']


# In[13]:


links = []

for img in images:
    links.append('http://books.toscrape.com/'+img['src'])

for l in links:
    print(l)


# In[15]:


os.mkdir('latest_bookstoscrape_photos')


# In[16]:


i = 1

for index, img_link in enumerate(links):
    if i<=10:
        img_data = rq.get(img_link).content
        with open('latest_bookstoscrape_photos\\' + str(index+1) + '.jpg', 'wb+') as f:
            f.write(img_data)
        i+=1
    else:
        f.close()
        break   


# In[ ]:




