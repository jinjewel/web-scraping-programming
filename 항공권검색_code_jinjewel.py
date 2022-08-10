import time
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

# browser.maximize_window() # 창 거대화

url = "https://flight.naver.com/"
browser.get(url) # url로 이동

# 가는날 선택 클릭
browser.find_element(By.XPATH , '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

# ---------------------날짜 선택이 안되는 상황------------  오류 선  --# 

# 이번달 27,28일 선택
# browser.find_elements(By.LINK_TEXT, "27")[0].click() # [0] -> 이번달
# browser.find_elements(By.LINK_TEXT, "28")[0].click() # [0] -> 이번달

# 다음달 27,28일 선택
# browser.find_elements(By.LINK_TEXT, "27")[1].click() # [1] -> 다음달
# browser.find_elements(By.LINK_TEXT, "28")[1].click() # [1] -> 다음달

browser.find_elements(By.LINK_TEXT, "27")[0].click() # [0] -> 이번달
browser.find_elements(By.LINK_TEXT, "28")[1].click() # [1] -> 다음달

time.sleep(3)

# 제주도 선택
browser.find_element(By.XPATH , '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
browser.find_element(By.LINK_TEXT, "국내").click()
browser.find_element(By.LINK_TEXT, "제주, 대한민국").click()

# 항공권 검색 클릭
browser.find_element(By.LINK_TEXT, "항공권 검색").click()

try:
    # 브라우저를 10초까지 대기하는데, 해당 XPATH에 element가 나올때까지
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/button')))
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()
