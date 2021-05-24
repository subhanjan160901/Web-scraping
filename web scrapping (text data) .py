#!/usr/bin/env python
# coding: utf-8

# In[1]:


#If you want to scrap the website :
# 1. Use the API
# 2. HTML Web scraping using tools like bs4

#Step 0 :Install all the requirements

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"


# In[2]:


#Step 1 : Get the HTML file

r = requests.get(url)
htmlcontent = r.content
print(htmlcontent)


# In[3]:


#Step 2 : Parse the HTML

soup = BeautifulSoup(htmlcontent,'html.parser')
print(soup.prettify)


# ## HTML tree traversal

# In[9]:


#Get the title of the HTML page

title = soup.title


# In[10]:


print(title)


# In[11]:


print(type(title))


# In[12]:


print(type(title.string))


# In[13]:


print(type(soup))


# ### Commonly used types of objects:
# 

# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. Comment

# In[14]:


#Get the paragraphs of the page

para = soup.find_all('p')
print(para)


# In[15]:


#Get all the anchor tags
anchors = soup.find_all('a')
print(anchors)


# In[16]:


#Get the first para

print(soup.find('p'))


# In[19]:


#Get the classes of any element in html page

print(soup.find('p')['class'])


# In[17]:


#Get the first anchor tag

print(soup.find('a'))


# In[20]:


#Find all the elements with class 'lead' :

print(soup.find_all('p', class_='lead'))


# In[24]:


#Get the text from the tags

print(soup.find('p').get_text())


# In[27]:


#Get the text from the soup

print(soup.get_text())


# In[30]:


#Get all the links in a page

anchors = soup.find_all('a')
all_links = set()
for link in anchors :
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        print(linkText)


# In[ ]:




