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

# 151로 이동
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

# 페이지 파싱
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

# 리스트에 크롤링 할 정보 넣기
table = soup.find_all("table", {"class": "tableBasic"})
tr = table[0].select('tbody > tr')
temp_list = []

# 151p
for i in range(len(tr)):
    event_name = tr[i].select_one('td:nth-child(2)').text + '+ ' + tr[i].select_one('td:nth-child(6)').text + '+ ' + tr[
        i].select_one('td:nth-child(8)').text
    event_date = tr[i].select_one('td:nth-child(4)').text
    event_time = tr[i].select_one('td:nth-child(5)').text
    event_loc = tr[i].select_one('td:nth-child(9)').text

    temp_list.append([event_name, event_date, event_time, event_loc])
print(temp_list)

# 152p
element152 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element152.click()
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

# 153p
element153 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element153.click()
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

# 154p
element154 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element154.click()
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

# 155p
element155 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element155.click()
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

# 156p
element156 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element156.click()
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

# 157p
element157 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element157.click()
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

# 158p
element158 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element158.click()
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

# 159p
element159 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element159.click()
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

# 160p
element160 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[11]/a')
element160.click()
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

# 161p
element161 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[12]/a')
element161.click()
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

# 162p
element162 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[3]/a')
element162.click()
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

# 163p
element163 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[4]/a')
element163.click()
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

# 164p
element164 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[5]/a')
element164.click()
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

# 165p
element165 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[6]/a')
element165.click()
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

# 166p 크롤링
element166 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[7]/a')
element166.click()
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

# 167p
element167 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[8]/a')
element167.click()
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

# 168p
element168 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[9]/a')
element168.click()
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

# 169p
element169 = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div[3]/div/div[2]/div/div/div[3]/div[2]/ul/li[10]/a')
element169.click()
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

event_pro_151_169_df = pd.DataFrame(temp_list)
event_pro_151_169_df.columns = ['event_name', 'event_date', 'event_time', 'event_loc']
event_pro_151_169_df.to_csv('event_pro151-169.csv', encoding = "utf-8-sig", index=False, mode='w')