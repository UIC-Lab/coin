"""
동아일보 뉴스 기사 크롤링
"비트코인" 검색어에 대한 기사 실시간 크롤링
time 함수 출처 : http://yujuwon.tistory.com/entry/%ED%98%84%EC%9E%AC-%EB%82%A0%EC%A7%9C-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0
출처 : http://yoonpunk.tistory.com/6
"""

import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
from datetime import datetime

TARGET_URL_BEFORE_PAGE_NUM = "http://news.donga.com/search?p="
TARGET_URL_BEFORE_KEWORD = '&query='
TARGET_URL_REST = '&check_news=1&more=1&sorting=1&range=2&search_date='

now_time = int(datetime.today().hour)
now_day = int(datetime.today().day)

# 기사 검색 페이지에서 기사 제목에 링크된 기사 본문 주소 받아오기
def get_link_from_news_title(page_num, URL, output_file):
    for i in range(page_num):
        current_page_num = 1 + i*15
        position = URL.index('=')
        URL_with_page_num = URL[: position+1] + str(current_page_num) \
                            + URL[position+1 :]
        source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
        soup = BeautifulSoup(source_code_from_URL, 'lxml',
                             from_encoding='utf-8')
        for title in soup.find_all('p', 'tit'):
            title_link = title.select('a')
            article_URL = title_link[0]['href']
            get_text(article_URL, output_file)


# 기사 본문 내용 긁어오기 (위 함수 내부에서 기사 본문 주소 받아 사용되는 함수)
def get_text(URL, output_file):
    source_code_from_url = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
    content_of_article = soup.select('div.article_txt')
    time_of_article = soup.select('div.title_foot > span.date01')
    temp = str(time_of_article[0])
    day = temp[32:34]
    time = temp[35:37]
    if time[0] == '0':
        time = time[1]
    if day[0] == '0':
        day = day[1]
    time = int(time)
    day = int(day)
    if day == now_day and time + 6 >= now_time:
        output_file.write(string_item)
    #print(temp_time)
    for item in content_of_article:
        string_item = str(item.find_all(text=True))
        if day == now_day and time + 6 >= now_time:
            output_file.write(string_item)


# 메인함수
def main(argv):
    keyword = "비트코인"
    page_num = int(1)
    output_file_name = "ret5.txt"
    target_URL = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEWORD \
                 + quote(keyword) + TARGET_URL_REST
    output_file = open(output_file_name, 'w',encoding='utf-8')
    get_link_from_news_title(page_num, target_URL, output_file)
    output_file.close()


if __name__ == '__main__':
    main(sys.argv)
