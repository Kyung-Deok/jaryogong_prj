import requests
from bs4 import BeautifulSoup
import pandas as pd

service_key = '6477774d4f6a68793830796c69706b'
url = f'http://openapi.seoul.go.kr:8088/{service_key}/xml/culturalEventInfo/'

url_list = []
for p in range(1, 4) :
    multiple = p * 1000
    if p == 1 :
        get_url = url + str(p) + '/' + str(multiple - 1) + '/'
        url_list.append(get_url)
    else :
        get_url = url + str(multiple - 1000) + '/' + str(multiple - 1) + '/'
        url_list.append(get_url)

datas = []

for j in range(len(url_list)) :
    result = requests.get(url_list[j])
    soup = BeautifulSoup(result.text, 'lxml')

    rows = soup.find_all("row")

    for i in range(len(rows)):
        codename = rows[i].find('codename').get_text()
        guname = rows[i].find('guname').get_text()
        title = rows[i].find('title').get_text()
        date = rows[i].find('date').get_text()
        place = rows[i].find('place').get_text()
        org_name = rows[i].find('org_name').get_text()
        use_trgt = rows[i].find('use_trgt').get_text()
        use_fee = rows[i].find('use_fee').get_text()
        player = rows[i].find('player').get_text()
        program = rows[i].find('program').get_text()
        etc_desc = rows[i].find('etc_desc').get_text()
        org_link = rows[i].find('org_link').get_text()
        main_img = rows[i].find('main_img').get_text()
        rgstdate = rows[i].find('rgstdate').get_text()
        ticket = rows[i].find('ticket').get_text()
        strtdate = rows[i].find('strtdate').get_text()
        end_date = rows[i].find('end_date').get_text()
        themecode = rows[i].find('themecode').get_text()

        data = [codename, guname, title, date, place, org_name, use_trgt, use_fee, player, program, etc_desc, org_link,
                main_img, rgstdate, ticket, strtdate, end_date, themecode]
        datas.append(data)


festival_info_df = pd.DataFrame(datas, columns=['codename', 'guname', 'title', 'date', 'place', 'org_name', 'use_trgt', 'use_fee',
                                  'player', 'program', 'etc_desc', 'org_link', 'main_img', 'rgstdate', 'ticket',
                                  'strtdate', 'end_date', 'themecode'])

# data type을 확인하여, 날짜 데이터를 확인. 날짜 데이터를 datetime 형태로 변경할지는 일단 보류.(DATE, RGSTDATE, STRTDATE, END_DATE 는 날짜 형태로 되어있음.)
# print(festival_info_df.info())

# 최종적으로 csv 파일로 저장
festival_info_df.to_csv("festival_info.csv", encoding="utf-8-sig")