from selenium import webdriver
from bs4 import BeautifulSoup
from progress.bar import IncrementalBar
import configparser
from typing import Union
import time, os
import requests
from datetime import datetime
import urllib.parse

class DataCrawler:
    def __init__(self, query: str) -> None:
        self.query = query
        self.url = f"https://www.pinterest.com/search/pins/?q={query}"
        self.scroll, self.sleep = self.read_config()
        

    def read_config(self) -> Union[str, str]:
        try:
            config = configparser.ConfigParser()
            config.read("config.ini")
            default_config = config["DEFAULT"]

            return int(default_config["scroll_num"]), int(default_config["sleep_timer"])
        except Exception as e:
            raise e
        
    def crawl_data(self):
        try:
            print(self.url)
            imgs = []
            driver = self.__set_driver()
            imgs = self.__get_imgs(driver)
            self.__download_imgs(imgs)
            
            print("Imgs:", len(imgs))
        except Exception as e:
            raise e
        
    def __set_driver(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            driver = webdriver.Chrome(options=options)
            driver.get(self.url)

            return driver
        except Exception as e:
            raise e
        
    def __get_imgs(self, driver):
        try:
            imgs = []
            bar = IncrementalBar('Scanning', max=self.scroll)
            for _ in range(self.scroll):
                driver.execute_script("window.scrollTo(1, 100000)")
                soup = BeautifulSoup(driver.page_source, "html.parser")

                for link in soup.find_all('img'):
                    imgs.append(link.get('src'))
                time.sleep(self.sleep)
                bar.next()
            bar.finish()

            return imgs
        except Exception as e:
            raise e
        
    def __download_imgs(self, imgs: list):
        try:
            imgs = list(set(imgs))
            bar = IncrementalBar('Downloading', max=len(imgs))
            for i, img in enumerate(imgs):
                img_url = img.replace("/60x60/", "/originals/").replace("/165x165/", "/originals/").replace("/222x150/", "/originals/").replace("/236x/", "/originals/").replace("/564x/", "/originals/")
                # print(i, img_url)

                response = ''
                while response == '':
                    try:
                        response = requests.get(img_url)
                        break
                    except:
                        # print("Connection Refused. Retrying...")
                        time.sleep(5)
                        continue
                    
                img_data = response.content
                folder = urllib.parse.unquote(self.query).replace(" ", "_")
                img_path = f"data/downloads/{folder}/{img_url.split("/")[-1]}"

                dir = os.path.dirname(img_path)
                if not os.path.exists(dir):
                    os.makedirs(dir)
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_data)

                bar.next()
            bar.finish()

        except Exception as e:
            raise e