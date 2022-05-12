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

#-*- coding: utf-8 -*-


import warnings
warnings.filterwarnings('ignore')


#user_input = "성산일출봉" #
#keyword= user_input + " 맛집"

path = "chromedriver.exe" #크롬 드라이버 있는 위치 설정하면 됨
driver = webdriver.Chrome()
sub_driver = webdriver.Chrome()

df = pd.read_csv('urlcrotest0414_01.csv', sep=',', encoding = 'UTF-8')

naver_map_name_list = []
blog_review_list = []
blog_review_qty_list = []
naver_map_star_review_stars_list = []
naver_map_star_review_qty_list = []
naver_map_type_list = []
review_text_list = []

#chromedriver = '/Users/datakim101/workspace/chromedriver'


for i, url in enumerate(tqdm(df['naver_map_url'])):
    driver.get(url)
    #sub_driver.get(url)
    sub_driver.get(url + "?type=photoView&photoUsed=true")
    time.sleep(2)

    try:

        # 간단 정보 가져오기

        # 네이버 지도의 유형 분류
        naver_map_type = driver.find_element_by_css_selector("#_title > span._3ocDE").text

        # 이런점이 좋았어요
        blog_review_qty = driver.find_element_by_css_selector(
            "#app-root > div > div > div > div:nth-child(5) > div:nth-child(3) > div.place_section._11ptV > div > div > div._3zxNp > em").text
        print(blog_review_qty)
        # 블로그 리뷰수
        star_review_qty = driver.find_element_by_css_selector(
            "#app-root > div > div > div > div.place_section.GCwOh > div._3uUKd > div._37n49 > span:nth-child(3) > a > em").text

        # 네이버 지도 블로그 리뷰 탭은 동적 웹사이트의 순서가 주문하기, 메뉴보기 등의 존재 여부로 다르기 때문에 css selector가 아니라 element 찾기로 진행
        #review_text_crawl_list = sub_driver.find_elements_by_class_name("_2CbII")
        review_text_crawl_list = sub_driver.find_element_by_css_selector(
            "#app-root > div > div > div > div:nth-child(6) > div:nth-child(4) > div.place_section.cXO6M > h2 > span.place_section_count").text

        # find element's' 메소드를 통해 가져온 내용은 리스트로 저장되고, 리스트 타입을 풀어서(for문 사용) 임시 데이터에 모아 두어야 한다
#        for review_crawl_data in review_text_crawl_list:
 #           review_text_list.append(review_crawl_data.find_element_by_tag_name('div').text)

        # 그 리스트에 저장된 텍스트 (한 식당에 대한 여러 리뷰들)를 한 텍스트 덩어리로 모아(join)줍니다.
        review_text = ','.join(review_text_list)

        blog_review_list.append(review_text)

        naver_map_type_list.append(naver_map_type)
        blog_review_qty_list.append(blog_review_qty)
        naver_map_star_review_qty_list.append(star_review_qty)

    # 리뷰가 없는 업체는 크롤링에 오류가 뜨므로 표기해둡니다.
    except Exception as e1:
        print(f"{i}행 문제가 발생")

        # 리뷰가 없으므로 null을 임시로 넣어줍니다.
        blog_review_list.append('null')
        naver_map_type_list.append('null')
        blog_review_qty_list.append('null')
        naver_map_star_review_qty_list.append('null')

driver.quit()
sub_driver.quit()

df['naver_store_type'] = naver_map_type_list  # 네이버 상세페이지에서 크롤링한 업체 유형
df['naver_star_point'] = naver_map_star_review_stars_list  # 네이버 상세페이지에서 평가한 별점 평점
df['naver_star_point_qty'] = naver_map_star_review_qty_list  # 네이버 상세페이지에서 별점 평가를 한 횟수
df['naver_blog_review_qty'] = blog_review_qty_list  # 네이버 상세페이지에 나온 블로그 리뷰의 총 개수

# 크롤링 에러가 떠서 'null'을 넣어 둔 데이터는 활용 의미가 없으므로 행 삭제를 해줘도 됩니다
df = df.loc[~(df['naver_store_type'].str.contains('null'))]

# 별점 평균, 수 같은 데이터 역시 스트링 타입으로 크롤링이 되었으므로 numeric으로 바꿔줍니다.
df[['naver_star_point', 'naver_star_point_qty', 'naver_blog_review_qty']] = df[
    ['naver_star_point', 'naver_star_point_qty', 'naver_blog_review_qty']].apply(pd.to_numeric)

#print(df)


df = pd.DataFrame(df)

df.to_csv('urlcrotest0511_01.csv')
