"""
동아일보 뉴스 기사 크롤링
"블록체인" 검색어에 대한 기사
"""

import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

TARGET_URL_BEFORE_PAGE_NUM = "http://news.donga.com/search?p="
TARGET_URL_BEFORE_KEWORD = '&query='
TARGET_URL_REST = '&check_news=1&more=1&sorting=3&search_date=1&v1=&v2=&range=3'


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
    for item in content_of_article:
        string_item = str(item.find_all(text=True))
        output_file.write(string_item)


# 메인함수
def main(argv):
    keyword = "비트코인"
    page_num = int(100)
    output_file_name = "ret1.txt"
    target_URL = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEWORD \
                 + quote(keyword) + TARGET_URL_REST
    output_file = open(output_file_name, 'w')
    get_link_from_news_title(page_num, target_URL, output_file)
    output_file.close()


if __name__ == '__main__':
    main(sys.argv)
