import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0+%EB%A7%A4%EB%AC%BC&oquery=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0&tqi=hY4pZwp0Jy0ssD1L3Y8ssssss5o-411877"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

data_row = soup.find("table", attrs={"class":"list"}).find("tbody").find_all("tr", attrs={"class":"_land_tr_row"})

for index, row in enumerate(data_row):
    columns = row.find_all("td")

    print("========== 매물 {} ==========".format(index + 1))
    print("거래 : ", columns[0].get_text().strip()) # strip() : 공백을 없애기 위해서 사용
    print("소재지 : ", columns[1].get_text().strip())
    print("단지명 : ", columns[2].get_text().strip())
    print("면적 : ", columns[3].get_text().strip(), "(제곱미터)")
    print("매물가 : ", columns[4].get_text().strip(), "(만원)")
    print("층 : ", columns[5].get_text().strip())
