from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import Keys
import openpyxl
import re
from datetime import datetime
import requests
import pandas as pd

## 1~90

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

url = 'http://data.prosports.or.kr/schedule/m0201/search'
driver.get(url)
sleep(3)

# 지정 되어 있는 날짜를 지웁니다.
date_delete = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[4]/ul/li[2]/a')
date_delete.click()
sleep(1)

# 단체 카테고리에 '전체'를 선택합니다.
g = driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div/div[1]/label')
g.click()
sleep(1)

# 리그 카테고리에 '전체'를 선택합니다.
l = driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div[1]/label')
l.click()
sleep(1)

# 구단 카테고리에 '전체'를 선택합니다.
l_g = driver.find_element(By.XPATH,
                          '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[3]/div[1]/div[1]/label')
l_g.click()
sleep(1)

# 주말/주중 카테고리에 '전체'를 선택합니다.
d = driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[5]/div/div[1]/label')
d.click()
sleep(1)

# 필요한 경기장 목록을 선택합니다.
c1 = driver.find_element(By.XPATH,
                         '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[6]/div/div[4]/label')
c1.click()
sleep(1)

c2 = driver.find_element(By.XPATH,
                         '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[6]/div/div[16]/label')
c2.click()
sleep(1)

c3 = driver.find_element(By.XPATH,
                         '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[6]/div/div[22]/label')
c3.click()
sleep(1)

c4 = driver.find_element(By.XPATH,
                         '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[6]/div/div[34]/label')
c4.click()
sleep(1)

c5 = driver.find_element(By.XPATH,
                         '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[6]/div/div[37]/label')
c5.click()
sleep(1)

c6 = driver.find_element(By.XPATH,
                         '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[6]/div/div[46]/label')
c6.click()
sleep(1)

c7 = driver.find_element(By.XPATH,
                         '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[6]/div/div[47]/label')
c7.click()
sleep(1)

c8 = driver.find_element(By.XPATH,
                         '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[6]/div/div[64]/label')
c8.click()
sleep(1)

date = driver.find_element(By.XPATH,
                           '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[4]/div/div/div/label')
date.click()
sleep(1)

# 2017년 1월까지 뒤로 갑니다.
prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

prev_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip.click()
sleep(1)

prev_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')
prev_skip1.click()
sleep(1)

# 2017년 1월 1일을 클릭합니다.
str_date = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[1]')
str_date.click()
sleep(5)

# 2022년 7월로 넘어갑니다.
# 1~10
next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

# 11~20
next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

# 21~30
next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

# 31~40
next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

# 41~50
next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

# 51~60
next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

# 61~65
next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

next_skip1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip1.click()
sleep(1)

next_skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')
next_skip.click()
sleep(1)

# 종료 날짜 클릭합니다.
end_date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/tbody/tr[6]/td[1]')
end_date.click()
sleep(1)

confirm = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/button[2]')
confirm.click()
sleep(2)

search = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[5]/button/i')
search.click()
sleep(1)

page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')
temp_list = []
# 1p 크롤링
for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 2p
element2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element2.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 3p
element3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element3.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 4p
element4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element4.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 5p
element5 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element5.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 6p 크롤링
element6 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element6.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 7p
element7 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element7.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 8p
element8 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element8.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 9p
element9 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element9.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 10p
element10 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element10.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 11p
element11 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element11.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 12p
element12 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element12.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 13p
element13 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element13.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 14p
element14 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element14.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 15p
element15 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element15.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 16p 크롤링
element16 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element16.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 17p
element17 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element17.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 18p
element18 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element18.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 19p
element19 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element19.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 20p
element20 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element20.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 21p
element21 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element21.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")
for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 22p
element22 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element22.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 32p
element23 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element23.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 24p
element24 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element24.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 25p
element25 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element25.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 26p 크롤링
element26 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element26.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 27p
element27 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element27.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 28p
element28 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element28.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 29p
element29 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element29.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 30p
element30 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element30.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 31p
element31 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element31.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 32p
element32 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element32.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 33p
element33 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element33.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 34p
element34 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element34.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 35p
element35 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element35.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 36p 크롤링
element36 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element36.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 37p
element37 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element37.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 38p
element38 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element38.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 39p
element39 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element39.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 40p
element40 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element40.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 41p
element41 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element41.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 42p
element42 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element42.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 43p
element43 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element43.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 44p
element44 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element44.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 45p
element45 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element45.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 46p 크롤링
element46 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element46.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 47p
element47 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element47.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 48p
element48 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element48.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 49p
element49 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element49.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 50p
element50 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element50.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 51p
element51 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element51.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 52p
element52 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element52.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 53p
element53 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element53.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 54p
element54 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element54.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 55p
element55 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element55.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 56p 크롤링
element56 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element56.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 57p
element57 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element57.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 58p
element58 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element58.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 59p
element59 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element59.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 60p
element60 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element60.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 61p
element61 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element61.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 62p
element62 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element62.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 63p
element63 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element63.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 64p
element64 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element64.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 65p
element65 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element65.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 66p 크롤링
element66 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element66.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 67p
element67 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element67.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 68p
element68 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element68.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 69p
element69 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element69.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 70p
element70 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element70.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 71p
element71 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element71.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 72p
element72 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element72.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 73p
element73 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element73.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 74p
element74 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element74.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 75p
element75 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element75.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 76p 크롤링
element76 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element76.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 77p
element77 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element77.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 78p
element78 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element78.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 79p
element79 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element79.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 80p
element80 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element80.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 81p
element81 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element81.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 82p
element82 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element82.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 83p
element83 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element83.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 84p
element84 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element84.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 85p
element85 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element85.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 86p 크롤링
element86 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element86.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 87p
element87 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element87.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 88p
element88 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element88.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 89p
element89 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element89.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 90p
element90 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element90.click()
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

event_pro_1_90_df = pd.DataFrame(temp_list)
event_pro_1_90_df.columns = ['event_name', 'event_date', 'event_time', 'event_loc']
event_pro_1_90_df.to_csv('event_pro1-90.csv', encoding = "utf-8-sig", index=False, mode='w')
