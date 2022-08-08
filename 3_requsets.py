import requests

res = requests.get("http://google.com")
# res = requests.get("http://ohcoding.com")
res.raise_for_status() # 웹에 문제가 없으면 다음 문장으로 넘어가지만, 오류가 있으면 바로 오류를 내면서 코딩을 종료한다.

# print("응답코드 :",res.status_code) # 200 이면 정상 아니면 이 페이지에 접근할 권한이 없다라는 뜻

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")    

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)