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

## 91~ 150

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

# 1~ 90 이동
element_skip = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element_skip.click()
sleep(4)

element_skip.click()
sleep(4)

element_skip.click()
sleep(4)

element_skip.click()
sleep(4)

element_skip.click()
sleep(4)

element_skip.click()
sleep(4)

element_skip.click()
sleep(4)

element_skip.click()
sleep(4)

element_skip.click()
sleep(4)
# 91p

page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')
temp_list = []

for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 92p
element92 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element92.click()
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

# 93p
element93 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element93.click()
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

# 94p
element94 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element94.click()
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

# 95p
element95 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element95.click()
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

# 96p 크롤링
element96 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element96.click()
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

# 97p
element97 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element97.click()
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

# 98p
element98 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element98.click()
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

# 99p
element99 = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element99.click()
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

# 100p
element100 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element100.click()
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

# 101p
element101 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element101.click()
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

# 102p
element102 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element102.click()
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

# 103p
element103 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element103.click()
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

# 104p
element104 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element104.click()
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

# 105p
element105 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element105.click()
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

# 106p 크롤링
element106 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element106.click()
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

# 107p
element107 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element107.click()
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

# 108p
element108 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element108.click()
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

# 109p
element109 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element109.click()
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

# 110p
element110 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element110.click()
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

# 111p
element111 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element111.click()
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

# 112p
element112 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element112.click()
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

# 113p
element113 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element113.click()
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

# 114p
element114 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element114.click()
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

# 115p
element115 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element115.click()
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

# 116p 크롤링
element116 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element116.click()
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

# 117p
element117 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element117.click()
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

# 118p
element118 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element118.click()
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

# 119p
element119 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element119.click()
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

# 120p
element120 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element120.click()
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

# 121p
element121 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element121.click()
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

# 122p
element122 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element122.click()
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

# 123p
element123 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element123.click()
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

# 124p
element124 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element124.click()
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

# 125p
element125 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element125.click()
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

# 126p 크롤링
element126 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element126.click()
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

# 127p
element127 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element127.click()
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

# 128p
element128 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element128.click()
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

# 129p
element129 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element129.click()
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

# 130p
element130 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element130.click()
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

# 131p
element131 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element131.click()
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

# 132p
element132 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element132.click()
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

# 133p
element133 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element133.click()
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

# 134p
element134 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element134.click()
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

# 135p
element135 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element135.click()
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

# 136p 크롤링
element136 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element136.click()
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

# 137p
element137 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element137.click()
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

# 138p
element138 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element138.click()
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

# 139p
element139 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element139.click()
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

# 140p
element140 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element140.click()
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

# 141p
element141 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element141.click()
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

# 142p
element142 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element142.click()
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

# 143p
element143 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element143.click()
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

# 144p
element144 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element144.click()
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

# 145p
element145 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element145.click()
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

# 146p
element146 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element146.click()
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

# 147p
element147 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element147.click()
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

# 148p
element148 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element148.click()
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

# 149p
element149 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element149.click()
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

# 150p
element150 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element150.click()
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

event_pro_91_150_df = pd.DataFrame(temp_list)
event_pro_91_150_df.columns = ['event_name', 'event_date', 'event_time', 'event_loc']
event_pro_91_150_df.to_csv('event_pro91-150.csv', encoding = "utf-8-sig", index=False, mode='w')