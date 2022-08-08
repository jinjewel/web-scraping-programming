# pip install beautifulsoup4 
# pip install lxml

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a elmaent 출력
# print(soup.a.attrs) # a elment 의 속성 정보를 출력
# print(soup.a["href"]) # a elment 의 href 속성 '값' 정보를 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 a elment를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 elment를 찾아줘

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling # 중간에 어떤 문제(띄어쓰기, 쓰레기 값 등)때문에 두번을 써서 값을 찾았음
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling # 부모로 올라가서 저장한다.
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li") # rank1 다음 elment 중에서 첫번때 li를 찾아 저장한다.
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li") # rank2 다음 elment 중에서 첫번때 li를 찾아 저장한다.
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li") # rank3 이전 elment 중에서 첫번때 li를 찾아 저장한다.
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li")) # rank1 다음 elment 중에서 li를 모두 찾는다.

webtoon = soup.find("a", text="프리드로우-제450화 졸업 여행 (1)") # 전체에서 "a"를 기준으로 text가 "프리드로우-제450화 졸업 여행 (1)"인 것을 찾는다. ex) <...> text </...>
print(webtoon)
















