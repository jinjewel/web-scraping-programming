# pip install beautifulsoup4 
# pip install lxml

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=773797&weekday=fri"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


# cartoon_titles = soup.find_all("td", attrs={"class":"title"})
# title = cartoon_titles[0]
# link = cartoon_titles[0].a["href"]
# print(title.get_text())
# print("https://comic.naver.com"+link)

# 1페이지 제목과 링크들 가져오기

# for cartoon_title in cartoon_titles:
#     title = cartoon_title.a.get_text()
#     link = "https://comic.naver.com"+ cartoon_title.a["href"]
#     print(title, link)

# 평점 구하기

cartoon_grades = soup.find_all("div", attrs={"class":"rating_type"})
total_rates = 0
number = 0
for cartoon_grade in cartoon_grades:
    number += 1
    print(cartoon_grade.get_text())
    grade = cartoon_grade.find("strong").get_text()
    total_rates += float(grade)
    print(str(number) + " 화 까지" , "현재 평균 평점" ,  str(total_rates/number)+"점 입니다.")
    