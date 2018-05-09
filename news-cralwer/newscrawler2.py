"""
한겨례 신문
"블록체인" 검색어에 대한 기사 크롤링
코드 출처 : http://yoonpunk.tistory.com/6
"""

import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

TARGET_URL_BEFORE_KEWORD = 'http://search.hani.co.kr/Search?command=query&' \
                          'keyword='
TARGET_URL_BEFORE_UNTIL_DATE = '&media=news&sort=s&period=all&datefrom=' \
                               '2000.01.01&dateto='
TARGET_URL_REST = '&pageseq='


def get_link_from_news_title(page_num, URL, output_file):
    for i in range(page_num):
        URL_with_page_num = URL + str(i)
        source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
        soup = BeautifulSoup(source_code_from_URL, 'lxml',
                             from_encoding='utf-8')
        for item in soup.select('dt > a'):
            article_URL = item['href']
            get_text(article_URL, output_file)


def get_text(URL, output_file):
    source_code_from_url = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
    content_of_article = soup.select('div.text')
    for item in content_of_article:
        string_item = str(item.find_all(text=True))
        output_file.write(string_item)


def main(argv):
    keyword = "블록체인"
    page_num = int(100)
    until_date = "2018.05.02"
    output_file_name = "ret2.txt"
    target_URL = TARGET_URL_BEFORE_KEWORD + quote(keyword) \
                 + TARGET_URL_BEFORE_UNTIL_DATE + until_date + TARGET_URL_REST
    output_file = open(output_file_name, 'w')
    get_link_from_news_title(page_num, target_URL, output_file)
    output_file.close()


if __name__ == '__main__':
    main(sys.argv)
