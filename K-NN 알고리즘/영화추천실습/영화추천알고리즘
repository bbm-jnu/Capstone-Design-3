from google.colab import drive 
drive.mount('/content/gdrive')

import pandas as pd 
import numpy as np
# 데이터 읽어오기 
movies=pd.read_csv('/content/gdrive/My Drive/movies.csv')
ratings=pd.read_csv('/content/gdrive/My Drive/ratings.csv')

# 아이템 기반 협업 필터링 
data=pd.merge(ratings,movies,on="movieId")
column=['userId','movieId','rating','title','genres']
data=data[column]
data
moviedata=data.pivot_table(index="movieId",  columns='userId')['rating']
moviedata

#NaN값을 -1로 변경 ( 평점을 계산할 때 양수값만 처리하면 됌)
moviedata.fillna(-1, inplace=True)
moviedata

#kdd 유사도 함수 
from math import sqrt
def sim_distance(data, n1, n2):
    sum=0
    #두 사용자가 모두 본 영화를 기준으로 해야해서 i로 변수 통일(j따로 안 써줌)
    for i in data.loc[n1,data.loc[n1,:]>=0].index:
         if data.loc[n2,i]>=0:
            sum+=pow(data.loc[n1,i]-data.loc[n2,i],2) #누적합 
    return sqrt(1/(sum+1)) #유사도 형식으로 출력 
    
# 나와 유사도가 높은 user 매칭 함수
def top_match(data, name, rank = 5, simf = sim_distance):
    simList = []
    for i in data.index[-10:]:
        if name != i:
            simList.append((simf(data, name, i), i))
    simList.sort()
    simList.reverse()    
    return simList[:rank]
    
# 추천 시스템 함수
def recommendation(data, person, simf = sim_distance):
    res = top_match(data, person, len(data))
    score_dic = {}
    sim_dic = {}
    myList = []
    for sim, name in res:
        if sim < 0:
            continue
        for movie in data.loc[person, data.loc[person, :] < 0].index:
            simSum = 0
            if data.loc[name, movie] >= 0:
                simSum += sim * data.loc[name, movie]
                
                score_dic.setdefault(movie, 0)
                score_dic[movie] += simSum
                
                sim_dic.setdefault(movie, 0)
                sim_dic[movie] += sim                
    for key in score_dic:
        myList.append((score_dic[key] / sim_dic[key], key))
    myList.sort()
    myList.reverse()
    return myList
    
# 25번 user가 안본 영화중에서 
#추천 점수가 가장 높은 순으로 예상평점과 영화제목을 추천 (10개까지)
movieList = []
for rate, m_id in recommendation(moviedata, 25):
    movieList.append((rate, movies.loc[movies['movieId'] == m_id, 'title']. values[0]))
movieList[:10]
