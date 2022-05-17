from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

path = "chromedriver.exe"
driver = webdriver.Chrome()

# driver.get("https://m.place.naver.com/restaurant/11857980/review/visitor?type=photoView&photoUsed=true")
time.sleep(1)

# articles = driver.find_elements_by_css_selector('#section_body > ul > li > dl > dt > a')
articles = driver.find_elements(By.CSS_SELECTOR,
                                '#app-root > div > div > div > div > div > div > div > div > div > ul > li > div > span')

article_list = []


def article_Scraping():
    driver = webdriver.Chrome()
    df = pd.DataFrame(columns=['url', 'keyword','count'])
    df_title = []
    df_pick = []
    df_num = []

#    data

#    df_title.append("https://m.place.naver.com/restaurant/11857980/review/visitor?type=photoView&photoUsed=true")

    for i in range(1, 2):
        driver.get("https://m.place.naver.com/restaurant/11857980/review/visitor?type=photoView&photoUsed=true")
        time.sleep(1)
        driver.find_element_by_css_selector('a._22igH').click()
        driver.find_element_by_css_selector('a._22igH').click()

        #        driver.find_elements(By.CSS_SELECTOR, 'div:nth-child(7) > div:nth-child(2) > div.place_section._11ptV > div > div > div._10UcK > a').click()
        #       driver.find_elements(By.CSS_SELECTOR, 'div:nth-child(7) > div:nth-child(2) > div.place_section._11ptV > div > div > div._10UcK > a').click()
        articles = driver.find_elements(By.CSS_SELECTOR,
                                        '#app-root > div > div > div > div > div > div > div > div > div > ul > li > div > span')
        for article in articles:
            if article.text == "동영상기사":
                pass
            elif len(article.text) != 0:
                article_list.append(article.text)
    driver.quit()


    for article in article_list:
#        print(article)
#        ps1 = pd.Series(article)
        if "이 키워드를 선택한 인원" in  article:
            article = article.replace('이 키워드를 선택한 인원\n', '')
            df_num.append(article)
            df_title.append(
                "https://m.place.naver.com/restaurant/11857980/review/visitor?type=photoView&photoUsed=true")
            print(df_num)

        else:
            df_pick.append(article)
#            print(df_pick)



#        print('ps1')
#        print(df_title)
#        print(df_pick)
#        data = pd.DataFrame(article)
#        data.head()

        #df_pick = pd.DataFrame(date = [article], columns=['기사내용'])
#        df_pick.append(article)

    df['url'] = df_title
    df['keyword'] = df_pick
    df['count'] = df_num
    print(df)
    df.to_csv('pickcroltest0517_01.csv')


article_Scraping()