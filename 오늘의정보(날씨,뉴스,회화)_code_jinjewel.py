import requests
import re
from bs4 import BeautifulSoup

# 웹 정보 가져오기
def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    return soup

# 뉴스 타이틀, 링크 출력
def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print("  (링크 : {}".format(link))

# 날씨 정보 가져오기
def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%8F%84%EB%B4%89%EA%B5%AC+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&tqi=hY5F%2Bsp0Jy0ss7Y9tBwssssssmZ-353556"
    soup = create_soup(url)
    # 어제보다 00 / 비,맑음
    cast = soup.find("p",attrs={"class":"summary"}).get_text()
    # 현재 00도 (최저, 최고)
    curr_temp = soup.find("div", attrs={"class","temperature_text"}).get_text() # 현재 온도
    min_temp = soup.find("span", attrs={"class","lowest"}).get_text() # 최저 온도
    max_temp = soup.find("span", attrs={"class","highest"}).get_text() # 최고 온도
    # 오전 오후 강수 확률
    rain_rate = soup.find("div", attrs={"class":"cell_weather"}).get_text()

    # 출력
    print(cast)
    print("{}({} / {})".format(curr_temp, min_temp, max_temp).strip()) # .strip() : 공백을 없애기 위해 사용
    print(rain_rate.strip())
    print()

    # 미세먼지 
    dust_data = soup.find_all("li", attrs={"class":"item_today level2"})
    for index, dust in enumerate(dust_data):
        print(dust.get_text().strip())
        if index >= 1:
            break
    print()    

# 헤더뉴스 정보 가져오기
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
    soup = create_soup(url)
    
    news_list = soup.find("ul", attrs={"class":"rankingnews_list"}).find_all("li", limit=3) # limit=3 : li 이라는 태그를 3개 까지만 찾으라는 뜻
    for index, news in enumerate(news_list):
        # title = news.fine.div.a.get_text().strip()
        title = news.find("a").get_text().strip()
        link = news.find("a")["href"]
        print_news(index, title, link)
    print()

# it 뉴스 정보 가져오기
def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)

    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3) # limit=3 : li 이라는 태그를 3개 까지만 찾으라는 뜻
    for index, news in enumerate(news_list):
        title = news.find_all("dt")[1].get_text().strip()
        link = news.find("a")["href"]
        print_news(index, title, link)
    print()

# 오늘의 영어회화 정보 가져오기
def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_lec/lec_study/lec_I_others_english&keywd=haceng_submain_lnb_lec_I_others_english&logger_kw=haceng_submain_lnb_lec_I_others_english"
    soup = create_soup(url)

    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")}) # re.compile("^conv_kor_t") : 정규표현식을 사용하여 conv_kor_t 로 시작하는 문장을 찾는다.
    print("영어지문")
    for sentence in sentences[len(sentences)//2:]: # 8문장이 있다고 가정할때, index 기준 4-7까지 영어지문
        print(sentence.get_text().strip())
    print()    
    print("한글지문")
    for sentence in sentences[:len(sentences)//2]: # 8문장이 있다고 가정할때, index 기준 0-3까지 한글지문
        print(sentence.get_text().strip())


if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news() # 오늘의 헤더뉴스 가져오기
    scrape_it_news() # it 뉴스 가져오기
    scrape_english() # 오늘의 영어회화 가져오기