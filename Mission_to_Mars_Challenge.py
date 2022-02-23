#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


#visit Mars NASA news site
url = 'https://redplanetscience.com'
browser.visit(url)

#optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1) #search for elements with specific combo of tag and attribute


# In[4]:


#html parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# uses the parent element to find the first 'a' tag, then saves as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


#user the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ###Featured Images

# In[8]:


# visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


#find and click the full image button 
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


#parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


#find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


#use base URL to create the absolute URL
img_url= f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[13]:


import pandas as pd


# In[14]:


#set up DF
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[15]:


#convert DF to HTML code
df.to_html()


# In[16]:


#end automated browsing session
browser.quit()


# In[17]:


#------------------------------------------
# DELIVERABLE 1: scraping images and titles
#------------------------------------------


# In[18]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[19]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[20]:


html = browser.html
img_soup = soup(html, 'html.parser')


# In[21]:


# Create empty list to hold images/titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Get a list of all of the hemispheres first. 
links = browser.find_by_css('a.product-item img')

# Create a for loop to go through each link and return the href 
for i in range(len(links)):
    hemisphere = {}
    
    # Find the elements on each loop to avoid a stale element exception
    browser.find_by_css('a.product-item img')[i].click()
    
    # Next, we find the Sample image anchor tag and extract the href
    sample_elem = browser.links.find_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    
    # Get Hemisphere title
    hemisphere['title'] = browser.find_by_css('h2.title').text
    
    # Append hemisphere object to list
    hemisphere_image_urls.append(hemisphere)
    
    # navigate backwords
    browser.back()


# In[22]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[23]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:




