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


import warnings
warnings.filterwarnings('ignore')


#df = pd.read_csv('urlcrotest0414_01.csv')
temp_df = "https://m.place.naver.com/restaurant/11857980/review/visitor"
# 기사 한개로 크롤링 Test
dict = {} # 크롤링 내용을 담을 딕셔너리 생성

path = "chromedriver.exe"
driver = webdriver.Chrome()
driver.get(temp_df + "?type=photoView&photoUsed=true")         # 첫번째 수집한 기사로, []인덱싱 부분의 숫자를 바꾸면 다른 기사를 띄운다.

print(temp_df)


#sub_driver = webdriver.Chrome()
#sub_driver.get(temp_df + "?type=photoView&photoUsed=true")

print(temp_df + "?type=photoView&photoUsed=true")

#2. 기사 제목, 날짜, 추천수 수집

#title = driver.find_element_by_partial_link_text('data-cid') #개발자 도구 class에서 확인 가능함
#print(title)
#title = title.text
#print(title) # text로 변환하는 과정이 있어야 사용 가능함

# driver.find_element_by_css_selector('셀렉터') 셀레늄을 활용해서 갖고올 때는 왼쪽의 형태로 대부분의 값들을 가져온다. 위에서 이야기한 대로, 이후에 .get_attribute | .text 형태로 원하는 값을 가져올 수 있다.
# selector('    ') 괄호 안의 셀렉터 값은 F12 개발자 노트의 element에서 잘 찾아야한다. ㅠㅠ


#date = driver.find_element_by_css_selector('.t11')
#date = date.text
#print(date)

# = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[5]/div[3]/div[1]/div/div/div[1]/em').get_attribute('em')
review_count = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[5]/div[3]/div[1]/div/div/div[1]/em')
blog_count = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[3]/a/em')

pic_count = driver.find_element(By.CLASS_NAME, 'place_section_count')
#map_type = driver.find_element(By.CLASS_NAME, '3ocDE')
map_type = driver.find_element(By.XPATH, '//*[@id="_title"]/span[2]')
fct_first = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[5]/div[3]/div[1]/div/div/div[2]/ul/li[1]/div[2]/span[2]')



review_count = review_count.text
blog_count = blog_count.text
pic_count = pic_count.text
map_type = map_type.text
fct_first = fct_first.text
#pic_count = pic_count.text

driver.find_element_by_css_selector('a._22igH').click()
driver.find_element_by_css_selector('a._22igH').click()
#more_review = driver.find_element_by_css_selector('a.22igH')


print(review_count)
print(blog_count + "first")
#review_count=review_count.text
print(pic_count + "second")
print(map_type + "second")
print(fct_first + "second")
#df.iloc[i,-1] = driver.find_element_by_css_selector("#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview").get_attribute('data-cid')

#일단 음식점 코드 추출에 성공한 코드임
