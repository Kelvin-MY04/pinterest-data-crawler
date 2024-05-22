from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
import time
import urllib.parse
from progress.bar import Bar

scroll_num = 100
sleep_timer = 1

var = urllib.parse.quote("interior design")
url = f"https://www.pinterest.com/search/pins/?q={var}"

print(url)
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get(url)

bar = Bar('Processing', max=scroll_num - 1)
for _ in range(1, scroll_num):
    driver.execute_script("window.scrollTo(1, 100000)")
    time.sleep(sleep_timer)
    bar.next()
bar.finish()

soup = BeautifulSoup(driver.page_source, "html.parser")

for link in soup.find_all('img'):
    print(link.get('src'))