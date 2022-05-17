import pandas as pd
import numpy as np
from selenium import webdriver
#라이브러리(모듈) 가져오라
from selenium.webdriver import ActionChains as AC
#import chromedriver_autoinstaller
from tqdm import tqdm
from tqdm.notebook import tqdm
import re
from time import sleep
import time
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup


import warnings
warnings.filterwarnings('ignore')

def review_Scraping():
    df = pd.DataFrame(columns=['url', '방문자리뷰','블로그리뷰', '사진리뷰', '음식점종류'])
    df_url = []
    df_visit = []
    df_blog = []
    df_pic = []
    df_cat = []

    # df = pd.read_csv('urlcrotest0414_01.csv')
    temp_df = "https://m.place.naver.com/restaurant/11857980/review/visitor"
    # 기사 한개로 크롤링 Test
    dict = {}  # 크롤링 내용을 담을 딕셔너리 생성

    path = "chromedriver.exe"
    driver = webdriver.Chrome()
    # iframe = driver.find_element_by_id("mainFrame") # id가 mainFrame이라는 요소를 찾아내고 -> iframe임
    # river.switch_to.frame(iframe)

    driver.get(temp_df + "?type=photoView&photoUsed=true")  # 첫번째 수집한 기사로, []인덱싱 부분의 숫자를 바꾸면 다른 기사를 띄운다.

    print(temp_df)
    time.sleep(1)

    print(temp_df + "?type=photoView&photoUsed=true")

    # = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[5]/div[3]/div[1]/div/div/div[1]/em').get_attribute('em')
    review_count = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[2]/a/em')
    # review_count = driver.find_element_by_css_selector('#app-root > div > div > div > div:nth-child(5) > div:nth-child(3) > div.place_section._11ptV > div > div > div._3zxNp > em')
    # review_count = driver.find_elements_by_css_selector('#section_body > ul > li > dl > dt > a')
    # review_count = driver.find_element(By.CLASS_NAME, 'pCb5N')
    # review_count = driver.find_elements(By.CSS_SELECTOR, '#app-root > div > div > div > div > div > div > div > div > div > em')

    blog_count = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[3]/a/em')

    pic_count = driver.find_element(By.CLASS_NAME, 'place_section_count')
    # pic_count = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[6]/div[4]/div[3]/h2/span[1]')
    # pic_count = driver.find_element(By.CSS_SELECTOR,'#app-root > div > div > div > div:nth-child(6) > div:nth-child(4) > div.place_section.cXO6M > h2 > span.place_section_count')

    # map_type = driver.find_element(By.CLASS_NAME, '3ocDE')
    map_type = driver.find_element(By.XPATH, '//*[@id="_title"]/span[2]')

    # review_count = review_count
    review_count = review_count.text
    blog_count = blog_count.text
    pic_count = pic_count.text
    map_type = map_type.text

    # pic_count = pic_count.text

    # driver.find_element_by_css_selector('a._22igH').click()
    # driver.find_element_by_css_selector('a._22igH').click()
    # more_review = driver.find_element_by_css_selector('a.22igH')

    print("방문자 리뷰 수 : " + review_count)
    print("블로그 리뷰 수 : " + blog_count)
    # review_count=review_count.text
    print("리뷰 사진 수 : " + pic_count)
    print("음식점 종류 : " + map_type)

    # df.iloc[i,-1] = driver.find_element_by_css_selector("#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview").get_attribute('data-cid')

    # 일단 음식점 코드 추출에 성공한 코드임
    df_url.append(temp_df)
    df_visit.append(review_count)
    df_blog.append(blog_count)
    df_pic.append(pic_count)
    df_cat.append(map_type)

    df['url'] = df_url
    df['방문자리뷰'] = df_visit
    df['블로그리뷰'] = df_blog
    df['사진리뷰'] = df_pic
    df['음식점종류'] = df_cat

    print(df)
    df.to_csv('reviewcountcroltest0517_01.csv')


review_Scraping()