from bs4 import BeautifulSoup
import requests

search_word = '신림선'
sd = '2022.03.02'
ed = '2022.03.02'
start_num = 1
url = "https://search.naver.com/search.naver?where=news&query={}&pd=3&ds={}&de={}&start={}".format(search_word,sd,ed,start_num)
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')


text_file = open("output.html", "w",encoding='utf-8')
text_file.write(html)
text_file.close()

# 뉴스제목 뽑아오기
import csv
from datetime import datetime

fd = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(fd, delimiter=',')
wr.writerow(['url', 'source', 'time', 'title', 'snippet'])
items = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')

for li in items:
    print(li)
    row = []
    url = li.div.a['href']

    source = li.find('a', {'class', 'info press'}).text
    time = li.find('span', {'class', 'info'}).text
    if "단" in time:
        time = datetime.today().strftime("%Y.%m.%d")

    title = li.find('a', {'class', 'news_tit'}).text
    snippet = li.find('a', {'class', 'api_txt_lines dsc_txt_wrap'}).text
    row.append(url)
    row.append(source)
    row.append(time)
    row.append(title)
    row.append(snippet)
    print("test1")

    print(row)

    wr.writerow(row)
fd.close()

from datetime import datetime
tt = datetime.today().strftime("%Y.%m.%d")
print(tt)
