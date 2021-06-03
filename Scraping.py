# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt
import Mission_to_Mars_Challenge

def scrape_all():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": mars_hemispheres(browser),
        "last_modified": dt.datetime.now()
             
    }
    browser.quit()
    return data


def mars_news(browser):
    # Visit the Mars news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    try:
        slide_elem = news_soup.select_one('div.list_text')

        slide_elem.find('div', class_='content_title')

        # Use the parent element to find the first a tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        news_title

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
        news_p
    except AttributeError:
        return none,none    

    return news_title, news_p

# ## JPL Space Images Featured Image
def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')


    try:
        # find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
        #img_url_rel
    except AttributeError:
        return None    

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    img_url

    return img_url

# ## Mars Facts

def mars_facts():
    try:
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
        df.head()
    except BaseException:
        return None


    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    df

    return df.to_html()

### Mars Images and titles
def mars_hemispheres(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    
    hemisphere_image_urls = []
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

    return hemisphere_image_urls     

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
