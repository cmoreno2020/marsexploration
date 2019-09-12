import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import time
import datetime as dt
import pprint
from flask import Flask, render_template


# * Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` 
#   with a function called `scrape` that will execute all of your scraping code from above and 
#   return one Python dictionary containing all of the scraped data.

def scrape():
    
    mars_data = {}

    #FOR WINDOWS USERS:
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #FOR MAC USERS:
    #executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    #browser = Browser('chrome', **executable_path, headless=False)
    
    ### NASA Mars News
    # * Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) 
    #   and collect the latest News Title and Paragraph Text. Assign the 
    #   text to variables that you can reference later.

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    time.sleep(5)
    soup = bs(html, "html.parser")
    nasa_news1 = soup.find("li", class_="slide")
    news_title1 = nasa_news1.find("div", class_='content_title').get_text()
    nasa_body1 = nasa_news1.find("div", class_="article_teaser_body").get_text()

    mars_news = {"title": news_title1, "body": nasa_body1}

    mars_data["mars_news"] = mars_news

    #pprint.pprint (mars_data["mars_news"])
    #x = input ("Mars News")
 
    # JPL Mars Space Images - Featured Image
    # #* Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
    # #* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
    # #* Make sure to find the image url to the full size `.jpg` image.
    # #* Make sure to save a complete url string for this image.
    
    html_JPL = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(html_JPL)
    #CLICK for full image
    browser.find_by_id('full_image').click()
    time.sleep(3)
    image1 = browser.html
    soupImage = bs(image1, "html.parser")
    #x = input ("Stop")

    imagelink = soupImage.find("img", class_="fancybox-image")['src']
    completelink = "https://www.jpl.nasa.gov" + imagelink

    mars_data["JPL_Image"] = completelink
    
    #print (mars_news["JPL_Image"])
    #x = input ("JPL Image")

    ### Mars Weather
    # * Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) 
    #  and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather \
    #  report as a variable called `mars_weather`.
    # 
    html_MW = "https://twitter.com/marswxreport?lang=en"
    browser.visit(html_MW)
    htmlMW = browser.html
    MWsoup = bs(htmlMW, "html.parser")
    tweet1 = MWsoup.find("div", class_="js-tweet-text-container")
    mars_weather = tweet1.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()

    mars_data["mars_weather"] = mars_weather
    #pprint.pprint(mars_data["mars_weather"])
    #x = input ("Mars Weather")


    ### Mars Facts
    # * Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and 
    #   use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # * Use Pandas to convert the data to a HTML table string.
    # 
    
    html_MF = "https://space-facts.com/mars/"
    tables = pd.read_html(html_MF)
    mars_tab = tables[1]
    mars_tab.rename(columns={0: 'Metric', 1: 'Mars'}, inplace=True)
    mars_tab1 = mars_tab.set_index('Metric')
    mars_html_table = mars_tab1.to_html()

    mars_data["mars_table"] = mars_html_table
    #pprint.pprint(mars_data["mars_table"])
    #x = input ("Mars Table")

    ### Mars Hemispheres
    # * Visit the USGS Astrogeology site 
    #  [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) 
    #  to obtain high resolution images for each of Mar's hemispheres.
    # * You will need to click each of the links to the hemispheres in order to find the image url to the 
    #   full resolution image.
    # * Save both the image url string for the full resolution hemisphere image, 
    #   and the Hemisphere title containing the hemisphere name. Use a Python dictionary to 
    #   store the data using the keys `img_url` and `title`.
    # * Append the dictionary with the image url string and the hemisphere title to a list. 
    #   This list will contain one dictionary for each hemisphere.

    html_AS = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(html_AS)
    hemispheres_list = ["Cerberus", "Schiaparelli", "Syrtis", "Valles"]
    hemisphere_image_urls = []

    for item in hemispheres_list:
        h = {}
        browser.click_link_by_partial_text(item)
        itemhtml = browser.html
        soup1 = bs(itemhtml, "html.parser")
        urlimg = soup1.find("img", class_="wide-image")["src"]
        fullurl = "https://astrogeology.usgs.gov/" + urlimg
        title = cerberus_title = soup1.find("h2", class_="title").get_text()
        h = {"img_url":fullurl, "title":title}
        hemisphere_image_urls.append(h)

    
    mars_data["images_list"] = hemisphere_image_urls
    return (mars_data)

#data = scrape()

#print("TOTAL DATA")
#pprint.pprint(data)

