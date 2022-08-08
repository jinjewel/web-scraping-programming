# pip install beautifulsoup4 
# pip install lxml

import csv
import requests
from bs4 import BeautifulSoup

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf8", newline="") # newline="" : 각 정보들 사이에 줄 나눔공백이 들어가는걸 방지하기 위해, 만약 엑셀 파일에서 한글이 깨지면 utf-8-sig 를 사용한다.
writer = csv.writer(f)

title= "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t") # .split("\t") : \t를 기준으로 잘라서 리스트로 저장한다.
writer.writerow(title) # csv에 입력하는 방법, 리스트 형식으로 집어 넣어야 한다.


for page in range(1,5):

    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(page)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        columns = row.find_all("td")

        if len(columns) <= 1: # 의미없는 데이터 삭제
            continue

        data = [column.get_text().strip() for column in columns] # 불 필요한 값들(\n\t등)을 제거하기 위해 .strip() 를 사용함
        # print(data)
        writer.writerow(data)
