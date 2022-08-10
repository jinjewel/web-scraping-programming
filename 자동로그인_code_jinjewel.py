# pip install selenium
# chrome://version 검색 후 ...-도움말-크롬정보-버전확인
# chromedriver 검색후 버전에 맞게 다운받고 실행 파일로 가져와서 압축풀기

# 2022년도라 selenium 버전 4.0를 사용한다.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome() # 실행파일에 저장을 했으면 안적어도 되지만, 다른 경로에 저장을 했으면 따로 적어줘야한다. ex) "c:/downloads/chromedriver.exe"

# 1. 네이버 이동
browser.get("http://naver.com")
time.sleep(3)

# 2. 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME, "link_login")
elem.click()

# 3. id, pw 입력
browser.find_element(By.ID, "id").send_keys("실제 아이디")
browser.find_element(By.ID, "pw").send_keys("실제 비밀번호")

# 4. 로그인 버튼 틀릭
elem = browser.find_element(By.ID, "log.login").click()

# # 5. id 새로 입력
# time.sleep(3) # 로그인 딜레이 고려
# browser.find_element(By.ID, "id").clear() # 전에 적혀있던 문자 지우기
# browser.find_element(By.ID, "id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우져 종료