import time
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

def scrape_url():
    # create a Browser instance
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

    #Mars News
    
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    mars_news_html=browser.html
    mars_news_soup = BeautifulSoup(mars_news_html,'html.parser')

    print(mars_news_soup.prettify())

    news_title_html = mars_news_soup.find('h3',class_=None)

    for x in news_title_html:
        news_title = x
    

    for paragraph in paragraphs:
        news_p = paragraph

    # Mars Image

    url_2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_2)

    jpl_html = browser.html
    jpl_soup = BeautifulSoup(jpl_html,'html.parser')


    featured_image_url = 'https://www.jpl.nasa.gov' + jpl_soup.find('img',class_='thumb')['src']

    # Mars Weather
    mars_weather_twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_weather_twitter_url)
    
    mars_weather_twitter_html = browser.html
    mars_weather_soup = BeautifulSoup(mars_weather_twitter_html,'html.parser')

    mars_weather = mars_weather_soup.find('p',class_='tweet-text').text

    #Mars Fact

    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_fact_url)

    mars_facts_html = browser.html
    mars_facts_soup = BeautifulSoup(mars_facts_html,'html.parser')

    first_column_data = mars_facts_soup.find_all('td',class_='column-1')
    second_column_data = mars_facts_soup.find_all('td',class_='column-2')

    labels = []
    values = []

    for x in first_column_data:
        labels.append(x.text)
    
    for y in second_column_data:
        values.append(y.text)

    
    mars_facts_df = pd.DataFrame({
        "Labels":labels,"Values":values
    
        })

    # Section 5: Mars Heimsperes


    mars_heimsperes_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_heimsperes_url)

    mars_heimsperes_html = browser.html
    mars_heimsperes_soup = BeautifulSoup(mars_heimsperes_html,'html.parser')

    title_html = mars_heimsperes_soup.find_all('h3')
    titles=[]

    for x in title_html:
        titles.append(x.text)

    
    img_url = []

    for title in titles:
        browser.click_link_by_partial_text(title)
        time.sleep(2)
        mars_img_html=browser.html
        mars_img_soup= BeautifulSoup(mars_img_html,'html.parser')
        mars_img = mars_img_soup.find('a',text='Original')
        img_url.append(mars_img.get('href'))
        browser.back()
        time.sleep(2)

    mars_hemisphere_image_urls = dict(zip(titles,img_url))
    
    mars_dictioanry = {
        "id":1,
        "news_title":news_title,
        "news_p":news_p,
        "featured_image_url":featured_image_url,
        "mars_weather":mars_weather,
        "mars_facts_df":mars_facts_df,
        "mars_hemisphere_image_urls":mars_hemisphere_image_urls}

    return mars_dictioanry