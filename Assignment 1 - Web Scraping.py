#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python script to scrape an article given the url of the article and store the extracted text in a file
# Url: https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7


# In[2]:


import os
import requests
import re
from bs4 import BeautifulSoup as bs


# In[3]:


# function to get the html source text of the medium article
def get_page():
    global url
    
    # Ask the user to input "Enter url of a medium article: " and collect it in url
    url = input("Enter url of a medium article: ")
    
    # handling possible error
    if not re.match(r'https?://medium.com/', url):
        print('Please enter a valid website, or make sure it is a medium article')
        sys.exit(1)
    
    # Call get method in requests object, pass url and collect it in res
    res = requests.get(url)
    
    res.raise_for_status()
    soup = bs(res.text, 'html.parser')
    print(type(soup))
    return soup


# In[4]:


def clean(text):
    rep = {"<br>": "\n", "<br/>": "\n", "<li>":  "\n"}
    rep = dict((re.escape(k), v) for k, v in rep.items()) 
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    text = re.sub('\<(.*?)\>', '', text)
    return text


# In[5]:


def collect_text(soup):
    text = f'url: {url}\n\n'
    para_text = soup.find_all('p')
    print(f"paragraphs text = \n {para_text}")
    for para in para_text:
        text += f"{para.text}\n\n"
    return text


# In[6]:


def save_file(text):
    if not os.path.exists('./scraped_articles'):
        os.mkdir('./scraped_articles')
    name = url.split("/")[-1]
    print(name)
    fname = f'scraped_articles/{name}.txt'
    
    # write a file using with (2 lines)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f'File saved in directory {fname}')


# In[7]:


# Url: https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7


# In[8]:


if __name__ == '__main__':
    text = collect_text(get_page())
    save_file(text)

