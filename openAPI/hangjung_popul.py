import requests
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

service_key = '4643674e576c756e3537664442706f'
url = f'http://openapi.seoul.go.kr:8088/{service_key}/xml/SPOP_LOCAL_RESD_DONG/'

url_list = []

