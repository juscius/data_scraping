import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd
import requests
import csv

links = []
url = 'https://www.15min.lt/tema/svietimas'
page = requests.get(url)

PATH = r"C:/Users/Pc/PycharmProjects/scraping/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.15min.lt/tema/svietimas')

time.sleep(3)
for k in range(2):
    time.sleep(3)

    try:
        elem = driver.find_element(By.TAG_NAME, 'body')
        no_of_pagedowns = 20

        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            no_of_pagedowns-=1

        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        for link in soup.find_all('a', {'class': 'vl-img-container'}):
            href = link.get('href')
            if href.startswith('https://www.15min.lt/naujiena/') and href not in links:
                links.append(href)
        time.sleep(3)
    except:
        pass

    time.sleep(2)

    show_more_button = driver.find_element(By.LINK_TEXT, 'Rodyti senesnius straipsnius')
    driver.execute_script("arguments[0].click();", show_more_button)

df = pd.DataFrame({"url": links})
df.to_csv('straipsniu_nuorodos.csv', index=False)