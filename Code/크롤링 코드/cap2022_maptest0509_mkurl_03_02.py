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

df = pd.read_csv('shops.csv', sep=',', encoding = 'CP949')

df = df.loc[df['상권업종대분류명'] == '음식']

df = df[['상호명', '상권업종중분류명', '상권업종소분류명', '표준산업분류명', '행정동명', '위도', '경도']]

df = df.loc[(df['행정동명'] == '노형동') | (df['행정동명'] == '연동')]
df = df[['상호명', '행정동명', '위도', '경도']]

df.columns = ['name',  # 상호명
              'dong',  # 행정동명
              'lon',  # 위도
              'lat'  # 경도
              ]

df['naver_keyword'] = "제주" + df['dong'] +  df['name']  # "%20"는 띄어쓰기를 의미합니다.
df['naver_map_url'] = ''
#print(df)
#위 코드는 전처리 과정으로 사전에 DB를 조작해도 문제 없음


for i, keyword in enumerate(df['naver_keyword'].tolist()):
    #print("이번에 찾을 키워드 :", i, f"/ {df.shape[0] - 1} 행", keyword) #정상작동
    try:
        naver_map_search_url = f"https://m.map.naver.com/search2/search.naver?query={keyword}&sm=hty&style=v5"
        driver.get(naver_map_search_url)
        time.sleep(3.5)
        #df['number']= driver.find_element(By.XPATH, '//*[@id="ct"]/div[2]/ul/li[1]/div[1]/a[1]').get_attribute('data-cid')
        #print( df['number'])
        df.iloc[i, -1] = driver.find_element(By.XPATH, '//*[@id="ct"]/div[2]/ul/li[1]/div[1]/a[1]').get_attribute('data-cid')
        print(df.iloc[i, -1])
        # 네이버 지도 시스템은 data-cid에 url 파라미터를 저장해두고 있었습니다.
        # data-cid 번호를 뽑아두었다가 기본 url 템플릿에 넣어 최종적인 url을 완성하면 됩니다.

        # 만약 검색 결과가 없다면?
    except Exception as e1:
        if "li:nth-child(1)" in str(e1):  # -> "child(1)이 없던데요?"
            try:
                df.iloc[i, -1] = driver.find_element(By.XPATH,
                                                     '//*[@id="ct"]/div[2]/ul/li[1]/div[1]/a[1]').get_attribute(
                    'data-cid')
                time.sleep(1)
            except Exception as e2:
                #print(e2)
                df.iloc[i, -1] = np.nan
                time.sleep(1)
        else:
            pass

#driver.quit()

# 이때 수집한 것은 완전한 URL이 아니라 URL에 들어갈 ID (data-cid 라는 코드명으로 저장된) 이므로, 온전한 URL로 만들어줍니다

#print(df['naver_map_url'])

df['naver_map_url'] = "https://m.place.naver.com/restaurant/" + df['naver_map_url'] + "/review/visitor"

# URL이 수집되지 않은 데이터는 제거합니다.

target = ['https://m.place.naver.com/restaurant//review/visitor']
df = df.loc[~df['naver_map_url'].isnull()]

df = df.loc[~df['naver_map_url'].isin(target)]
df.head()

#print(df)


df = pd.DataFrame(df)

df.to_csv('urlcrotest0414_01.csv')
