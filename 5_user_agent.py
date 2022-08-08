import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status() # 웹에 문제가 없으면 다음 문장으로 넘어가지만, 오류가 있으면 바로 오류를 내면서 코딩을 종료한다.    


with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)