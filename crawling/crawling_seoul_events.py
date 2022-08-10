import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import datetime
import timestring
import os.path

service = Service('../../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)


url = 'https://stadium.seoul.go.kr/board/show-event'
driver.get(url)
# sleep(1)

# iframe으로 접근
driver.switch_to.frame(0)

# 월별안내 접근
month_select = driver.find_element(By.XPATH, '/html/body/div/nav/ul/li[2]/a')
month_select.click()
sleep(2)

# 분야 선택
event_select1 = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/div[2]/dl[1]/dd/ul/li[2]/input')
event_select1.click()
sleep(1)

event_select2 = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/div[2]/dl[1]/dd/ul/li[3]/input')
event_select2.click()
sleep(1)

event_select3 = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/div[2]/dl[1]/dd/ul/li[4]/input')
event_select3.click()
sleep(1)

soup = BeautifulSoup(driver.page_source, 'html.parser')

# 이전 연도
for k in range(6):

    if k == 0:
        pass
    else:
        past_year_select = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/div[1]/div[1]/a[1]')
        past_year_select.click()
        sleep(2)

    # 지금 연도
    event_year = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/div[1]/div[1]/div/span').text

    # month 선택
    for i in range(1, 4):

        for j in range(1, 5):

            month_select = driver.find_element(By.XPATH, f'/html/body/div/div[1]/form/div[1]/div[2]/table/tbody/tr[{i}]/td[{j}]/a')
            month_select.click()
            sleep(3)

            # 가져올 행의 수
            row_count_text = driver.find_element(By.XPATH, '/html/body/div/p/span').text
            row_count = int(str(row_count_text))
            sleep(3)

            if row_count == 0:
                pass
            else:
                for total_count in range(1, (row_count+1)):
                    event_total = driver.find_elements(By.XPATH, '/html/body/div/ul/li[' + str(total_count) + ']')
                    
                    # M.dd(요일) ~ M.dd(요일)
                    event_date_str = driver.find_element(By.XPATH, '/html/body/div/ul/li[' + str(total_count) + ']/a/time[1]').text

                    week = ['월', '화', '수', '목', '금', '토', '일']
                    event_date = event_date_str.replace('(', '').replace(')', '').replace('.', '-')

                    for weekcheck in range(len(week)):
                        event_date = event_date.replace(f'{week[weekcheck]}', '')

                    # format = '%m-%d'
                    # print(str(event_date.split('~')[0]))
                    # print(datetime.datetime.strptime(str(event.split('~')[0]), format))
                    # event_date = datetime.datetime.strptime(event_date.split('~'), format)
                    # timestring.Date(str(event_date.split('~')[0]))
                    event_time = driver.find_element(By.XPATH, '/html/body/div/ul/li[' + str(total_count) + ']/a/time[2]').text
                    event_location = driver.find_element(By.XPATH, '/html/body/div/ul/li[' + str(total_count) + ']/a/strong').text
                    event_category = driver.find_element(By.XPATH, '/html/body/div/ul/li[' + str(total_count) + ']/a/span[1]').text
                    event_name = driver.find_element(By.XPATH, '/html/body/div/ul/li[' + str(total_count) + ']/a/span[2]').text

                    event_data = [[event_year, event_date, event_time, event_location, event_category, event_name]]
                    seoul_events_df = pd.DataFrame(event_data, columns=['event_year', 'event_date', 'event_time', 'event_location', 'event_category', 'event_name'])

                    if not os.path.exists(f'crawling_seoul_events_{event_year}.csv'):
                        seoul_events_df.to_csv(f'crawling_seoul_events_{event_year}.csv', encoding='utf-8-sig', index=False, mode='w')
                    else:
                        seoul_events_df.to_csv(f'crawling_seoul_events_{event_year}.csv', encoding='utf-8-sig', index=False, mode='a', header=False)
