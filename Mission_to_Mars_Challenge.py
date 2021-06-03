#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[2]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)


# In[3]:


# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


html=browser.html
news_soup = soup(html,'html.parser')
slide_elem = news_soup.select_one('div.list_text')

news_title=slide_elem.find('div', class_='content_title').get_text()
news_title


# In[5]:


news_summary=slide_elem.find('div', class_='article_teaser_body').get_text()
news_summary


# ###Featured Images

# In[6]:


url="https://spaceimages-mars.com/"
browser.visit(url)


# In[7]:


full_image_elem=browser.find_by_tag('button')[1]
full_image_elem.click()


# In[8]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[9]:


img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[10]:


df = pd.read_html('https://galaxyfacts-mars.com/')[0]
df.columns= ['description','Mars','Earth']
df.set_index('description',inplace =True)
df


# In[11]:


df.to_html()


# In[12]:


browser.quit()


# In[13]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# # Visit the mars nasa news site

# In[14]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[15]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[16]:


slide_elem.find('div', class_='content_title')


# In[17]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[18]:


news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # JPL Space Images Featured Image

# In[19]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[20]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[21]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[22]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[23]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# # Mars Facts

# In[24]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[25]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[26]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ## Hemispheres

# In[27]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[28]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

url_title={}

for i in range(0,4):
    full_img_elem = browser.find_by_tag('h3')[i]
    full_img_elem.click()
    html = browser.html
    image_soup = soup(html,'html.parser')
    full_img_link = browser.links.find_by_text('Sample')
    url_title['img_url'] = full_img_link['href']
    full_img_title = image_soup.find('h2', class_='title').get_text()
    url_title['title'] = full_img_title
    hemisphere_image_urls.append(url_title.copy()) 
    browser.back()
    

    


# In[29]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[30]:


# 5. Quit the browser
browser.quit()

