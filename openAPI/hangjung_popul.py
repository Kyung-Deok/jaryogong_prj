import os.path

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint
import json

service_key = '4643674e576c756e3537664442706f'
url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/SPOP_LOCAL_RESD_DONG/'

url_list = []

# url 기준일자 8월 한달 기준으로 매일 돌아가게
for i in range(1, 31):
    august = '202208'

    # 일자가 한자리라면 0을 추가해서 01일 형태로 만들기
    if i < 10:
        august_date = august + '0' + str(i)
    # 일자가 두자리면 그냥 일자 붙이기
    else:
        august_date = august + str(i)

    # openapi가 1천개까지밖에 못불러와서 천개단위로 반복하기
    for j in range(1, 12):
        multiple = j * 1000

        if j == 1:
            get_url = url + str(j) + '/' + str(multiple - 1) + '/' + august_date
            url_list.append(get_url)
        else:
            get_url = url + str(multiple - 1000) + '/' + str(multiple - 1) + '/' + august_date
            url_list.append(get_url)

# 모든 url 속 데이터 가져오기
for k in range(len(url_list)):
    
    # 데이터를 받아올 수 있다면 json형태로 만들고, 데이터를 받아올 수 없다면 멈추기
    try:
        response = requests.get(url_list[k])
        if response.status_code == 200:
            hjp_content = response.text

            hjp_json = json.loads(hjp_content)
        else:
            response.close()

        # 데이터프레임에 row밑 데이터 모두 가져오기
        hangjung_popul_df = pd.json_normalize(hjp_json['SPOP_LOCAL_RESD_DONG']['row'])
        
        hangjung_popul_df.columns = ['기준일ID', '시간대구분', '행정동코드', '총생활인구수', '남자0세부터9세생활인구수', '남자10세부터14세생활인구수',
                                     '남자15세부터19세생활인구수', '남자20세부터24세생활인구수', '남자25세부터29세생활인구수', '남자30세부터34세생활인구수',
                                     '남자35세부터39세생활인구수', '남자40세부터44세생활인구수', '남자45세부터49세생활인구수', '남자50세부터54세생활인구수',
                                     '남자55세부터59세생활인구수', '남자60세부터64세생활인구수', '남자65세부터69세생활인구수', '남자70세이상생활인구수',
                                     '여자0세부터9세생활인구수', '여자10세부터14세생활인구수', '여자15세부터19세생활인구수', '여자20세부터24세생활인구수',
                                     '여자25세부터29세생활인구수', '여자30세부터34세생활인구수', '여자35세부터39세생활인구수', '여자40세부터44세생활인구수',
                                     '여자45세부터49세생활인구수', '여자50세부터54세생활인구수', '여자55세부터59세생활인구수', '여자60세부터64세생활인구수',
                                     '여자65세부터69세생활인구수', '여자70세이상생활인구수']

        # 최초엔 csv파일 write모드로 생성, csv파일이 존재한다면 add 모드로 추가

        if not os.path.exists(
                '../../../Users/luniv/Desktop/멀티캠퍼스/DE전공프로젝트/개인작업물/git백업/filedata/LOCAL_PEOPLE_DONG_2208.csv'):

        if not os.path.exists('../filedata/LOCAL_PEOPLE_DONG_2208.csv'):

            hangjung_popul_df.to_csv('LOCAL_PEOPLE_DONG_2208.csv', encoding='utf-8-sig', index=False, mode='w')
        else:
            hangjung_popul_df.to_csv('LOCAL_PEOPLE_DONG_2208.csv', encoding='utf-8-sig', index=False, mode='a', header=False)

    except Exception as e:
        print(e)
