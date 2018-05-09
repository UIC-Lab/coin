"""
TOKENPOST 속보 크롤링 하기
URL = "https://tokenpost.kr/breaking"
time 함수 출처 : http://yujuwon.tistory.com/entry/%ED%98%84%EC%9E%AC-%EB%82%A0%EC%A7%9C-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0
코드 출처 : http://yoonpunk.tistory.com/6
"""

import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
from datetime import datetime


URL = "https://tokenpost.kr/breaking"
now_time = int(datetime.today().hour)
now_day = int(datetime.today().day)
# 속보 불러오기
def get_link_from_news_title(URL, output_file):
        source_code_from_URL = urllib.request.urlopen(URL)
        soup = BeautifulSoup(source_code_from_URL, 'lxml',
                             from_encoding='utf-8')
        for title in soup.find_all('div', 'breakListRight'):
            title_link = title.select('a')
            article_URL = title_link[0]['href']
            get_text(article_URL, output_file)


# 기사 본문 내용 긁어오기 (하이퍼 링크 타기 )
def get_text(URL, output_file):
    source_code_from_url = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
    content_of_article = soup.select('div.viewContentArticle')
    for item in content_of_article:
        string_item = str(item.find_all(text=True))
        temp = str(item.find('p','viewInfoTime'))
        time = temp[37:39]
        if time[0] == '0':
            time = time[1]
        day = temp[32:35]
        if day[0] == '0':
            day = day[1]
        time = int(time)
        day = int(day)
        if day == now_day and time + 6 >= now_time:
            output_file.write(string_item)


# 메인함수
def main(argv):
    output_file_name = "ret3.txt"
    target_URL = URL
    output_file = open(output_file_name, 'w',encoding="utf-8")
    get_link_from_news_title(target_URL, output_file)
    output_file.close()


if __name__ == '__main__':
    main(sys.argv)
