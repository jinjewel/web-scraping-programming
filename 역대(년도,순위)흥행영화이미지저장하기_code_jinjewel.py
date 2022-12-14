# pip install beautifulsoup4 
# pip install lxml

import requests
from bs4 import BeautifulSoup
page_number = 0

for year in range(2018,2022):

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):

        image_url = image["src"]

        if image_url.startswith("//"): # image_url 이 //로 시작한다면
            image_url = "http:" + image_url

        print(image_url)

        image_res = requests.get(image_url) # 다시 elment를 저장시킨다
        image_res.raise_for_status()

        with open("movie{}-{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)

        if idx >= 4: # 상위 5개의 이미지만 추출
            break
