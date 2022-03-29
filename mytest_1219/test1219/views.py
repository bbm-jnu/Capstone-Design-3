from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlencode
from urllib.request import urlopen
import json
import csv
import math

from test1219.models import Wifi_2018103297
from django.views.decorators.csrf import csrf_exempt

#@csrf_exempt
def index(request):
    return render(request, 'test1219/index.html', None)

#@csrf_exempt
def maps(request):
    jejuelec = request.POST.get('jejuelec')
    if(jejuelec==""):
        return render(request, 'test1219/index.html', {
            'error_message': "입력하지 않으셨습니다. 다시 입력 부탁드립니다.",
                })

    else:
        print(jejuelec)
        url = 'https://gw.jejudatahub.net/api/proxy/c5ef63523b1611e9ab958f5bbd84cea8/'


        input_json = {'addressDong': jejuelec}# 'name': '노형동주민센터'}#원하는 데이터 조건 설정, 필수 ㅔ데이터는 꼭 넣어야 한다, 받는 걸 선택할 땐, json
        # ,'addressDong': jejuelec
        # 'latitude': '33.483098',
        # 'longitude': '126.477231'}
        queryParams = '?' + urlencode(input_json)  # 키랑 url을 연결시키는 부분

        input_url = url + 'b9f1e4a56cd611eaa1d5aff3bc30f288' + queryParams  # api에 넣을 url 완성
        print(input_url)

        response_body = urlopen(input_url).read().decode('utf-8')  # 받은 응답 변수에 넣기
        print(response_body)

        json_data = json.loads(response_body)  # 응답 json으로 만들기

        if(json_data['totCnt']==0):
            return render(request, 'test1219/index.html', {
                'error_message': "없는 장소입니다. 다시 입력해주십시오",
            })
        items = json_data['data']  # 데이터에서 Data 안에 들어 있는 것 보기

        for data in items:  # data에 있는걸 itmes 만큼 출력해라
            onerow = []
            onerow.append(data['name'])
            onerow.append(data['longitude'])
            onerow.append(data['latitude'])

        name = onerow[0]
        longitude = onerow[1]
        latitude = onerow[2]

        return render(request, 'test1219/maps.html', {'name': name, 'longitude': longitude, 'latitude': latitude})