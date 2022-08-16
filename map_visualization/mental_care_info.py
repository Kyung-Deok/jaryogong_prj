import requests
import json
import pandas as pd
from pprint import pprint

service_key = 'QQsdoth%2B0GJt57VarZap%2FOxQ5BiXlZIX7HGCczFzLsWxOjAe0wcLuGhYwhsp3ht3kRTQUVPCS0TubUB12LO4gw%3D%3D'
pages = 'page=1&perPage=10000'
api_list = [
    '/3049990/v1/uddi:0fcb2f4e-b1ff-442e-a4d0-a328e1b22050',
    '/3049990/v1/uddi:253d954b-457b-469c-9897-c6cfb1f501ea',
    '/3049990/v1/uddi:16666701-9eba-467b-b0f8-b8c9a638f22c',
    '/3049990/v1/uddi:bc39a40f-ad39-493a-84f4-a71b9830109e',
    '/3049990/v1/uddi:0137d4c0-be61-4215-9275-a1c95e85820d_201909111023',
    '/3049990/v1/uddi:819cc15c-e726-493b-a52d-bdba85807ac2_201909111054',
    '/3049990/v1/uddi:8fa8bfa2-f92b-4a48-8197-be62b43aa182_201909111052',
    '/3049990/v1/uddi:62073a45-3890-4950-baa8-c1dcb3f546e8_201909111050',
    '/3049990/v1/uddi:98153f24-3596-4eb6-ae1b-c01b5dca5e27_201909111048',
    '/3049990/v1/uddi:eeff7c92-02e9-45f0-97bb-a2b5a95c8dcd',
    '/3049990/v1/uddi:ffd056e3-4e1e-4e42-b3bd-952c7625930f',
    '/3049990/v1/uddi:14a6ea21-af95-4440-bb05-81698f7a1987'
]
'''
for i in api_list:
    url = f'https://api.odcloud.kr/api{i}?{pages}&serviceKey={service_key}'
    response = requests.get(url).json()

    # pprint(response)

    with open('mental_care.json','w', encoding='UTF-8') as mental_care:
        json.dump(response, mental_care, ensure_ascii=False, indent=4, sort_keys=True)
'''
# 병원계열(상급, 종합, 의원 등) 전부 병원으로 묶어버리기
# 기관구분 우선 > 지역이후
# 경도위도로 좌표바꾸기 geojson

with open('./mental_care.json', 'r', encoding='UTF-8') as js:
    mc = json.load(js)

    # pprint(mc)

    df2 = pd.DataFrame(mc)
    df = pd.DataFrame(mc['data'])
    gigwan_search = df['기관구분']

    df.loc[gigwan_search == '국립', '기관구분'] = '병원'
    df.loc[gigwan_search == '공립', '기관구분'] = '병원'
    df.loc[gigwan_search == '종합병원', '기관구분'] = '병원'
    df.loc[gigwan_search == '의원', '기관구분'] = '병원'
    df.loc[gigwan_search == '상급종합병원', '기관구분'] = '병원'
    df.loc[gigwan_search == '병원', '기관구분'] = '병원'

    df = df.drop(index=df.loc[df['기관구분'] == '병원'].index)

    df.loc[gigwan_search == '정신요양시설', '기관구분'] = '시설'
    df.loc[gigwan_search == '정신재활시설', '기관구분'] = '시설'
    df.loc[gigwan_search == '중독관리통합지원센터', '기관구분'] = '센터'
    df.loc[gigwan_search == '기초정신건강복지센터', '기관구분'] = '센터'
    df.loc[gigwan_search == '자살예방센터', '기관구분'] = '센터'
    df.loc[gigwan_search == '광역정신건강복지센터', '기관구분'] = '센터'
    df['공공/민간'] = ''
    # if else 사용방법은 없을까?
    # df.loc[gigwan_search == '병원', '공공/민간'] = '민간'
    df.loc[gigwan_search == '보건소', '공공/민간'] = '공공'
    # df.loc[gigwan_search == '공립', '공공/민간'] = '공공'
    # df.loc[gigwan_search == '국립', '공공/민간'] = '공공'
    df.loc[gigwan_search == '중독관리통합지원센터', '공공/민간'] = '공공'
    df.loc[gigwan_search == '기초정신건강복지센터', '공공/민간'] = '공공'
    df.loc[gigwan_search == '자살예방센터', '공공/민간'] = '공공'
    df.loc[gigwan_search == '광역정신건강복지센터', '공공/민간'] = '공공'
    df.loc[gigwan_search == '정신요양시설', '공공/민간'] = '민간'
    df.loc[gigwan_search == '정신재활시설', '공공/민간'] = '민간'
    # print(df.loc[gigwan_search == '보건소', '공공/민간'])
    

    df['전화번호'] = 'null'
    # (gigwan_search)
    # print(gigwan_jungbok)
    # print(df)

    # 의료기관 카테고리 전부 삭제

    # print(df)

    # df.to_json('mental_care_nohospital.json', force_ascii=False, orient='records', indent=4)

    # print(gigwan_juso)
    # print(df.columns)
    def la_lo(addr):
        url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr

        headers = {'Authorization': 'KakaoAK d45bfa896dfff37a7ba89931acb69982'}

        try:
            api_call = json.loads(str(requests.get(url, headers=headers).text))
            lalo = api_call['documents'][0]['address']

            return [float(lalo['x']), float(lalo['y'])]
        except:
            return None

    # print(la_lo('경기도 안양시 동안구 부림로 113'))

    gigwan_juso = df['주소']
    # print('-------------',gigwan_juso)
    # print(gigwan_juso)
    # print(la_lo(gigwan_juso.values[0])[0])
    # print(la_lo('광주광역시 북구 태봉로 32, 유동 115-1'))
    # print(df)
    # 위도경도작업

    lati = []
    longi = []

    df['위도'] = ''
    df['경도'] = ''

    df = df[['공공/민간', '기관구분', '기관명', '주소', '위도', '경도', '전화번호', '홈페이지']]
    # print(la_lo('경기도 안산시 상록구 석호공원로 2길7, 401호(사동)'))

    for i in range(0, len(gigwan_juso)):
        # print(gigwan_juso.values[i])

        # pprint(la_lo(gigwan_juso.values[i])[0])

        lati = la_lo(gigwan_juso.values[i])[0]
        longi = la_lo(gigwan_juso.values[i])[1]

        df['위도'].iloc[i] = lati
        df['경도'].iloc[i] = longi

    # pprint(df['위도'])

df.to_json('mental_care_final.json')

'''
json 양식
1. 공공/민간
2. 기관구분 (상담소or병원)
3. 기관명
4. 주소 
5. 좌표 (위도경도)
6. 전화번호 (null)
7. 홈페이지 (null)
'''



'''
# 기존 10개 테스트 코드
headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'accept': 'application/json',
    'Authorization': 'QQsdoth%2B0GJt57VarZap%2FOxQ5BiXlZIX7HGCczFzLsWxOjAe0wcLuGhYwhsp3ht3kRTQUVPCS0TubUB12LO4gw%3D%3D',
}

params = {
    'serviceKey': 'QQsdoth+0GJt57VarZap/OxQ5BiXlZIX7HGCczFzLsWxOjAe0wcLuGhYwhsp3ht3kRTQUVPCS0TubUB12LO4gw==',
}

response = requests.get(url='https://api.odcloud.kr/api/3049990/v1/uddi:0fcb2f4e-b1ff-442e-a4d0-a328e1b22050?serviceKey=QQsdoth%2B0GJt57VarZap%2FOxQ5BiXlZIX7HGCczFzLsWxOjAe0wcLuGhYwhsp3ht3kRTQUVPCS0TubUB12LO4gw%3D%3D', params=params, headers=headers).json()

pprint(response)
'''