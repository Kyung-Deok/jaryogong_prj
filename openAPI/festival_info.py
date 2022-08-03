import requests
from bs4 import BeautifulSoup

service_key = '6477774d4f6a68793830796c69706b'
url = 'http://openapi.seoul.go.kr:8088/sample/xml/culturalEventInfo/1/5/'

result = requests.get(url)

parsing = BeautifulSoup(result, 'lxml-xml')


print(parsing)