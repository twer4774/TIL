#-*-coding:UTF-8-*-

import re
import requests
import lxml.html
import time
from pymongo import MongoClient

def main():

    #크롤러 호스트의 MongoDB 접속
    client = MongoClient('localhost', 27017)
    #scraping 데이터베이스의 ebooks 콜렉션
    collection = client.scraping.ebooks
    #데이터를 식별 할 수 있는 유일키를 저장할 key필드에 인덱스 생성
    collection.create_index('key', unique=True)

    #목록 페이지 추출
    response = requests.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)

    for url in urls:
        #URL로 키 추출
        key = extract_key(url)
        #MongoDB에서 key에 해당하는 데이터 검색
        ebook = collection.find_one({'key': key})
        #MongoDB에 존재하지 않는 경우만 상세 페이지 크롤링
        if not ebook:
            time.sleep(1)
            response = requests.get(url)
            ebook = scrape_detail_page(response) #상세페이지에서 상세 정보 추출
            #책 정보를 MongoDB에 저장
            collection.insert_one(ebook)
        print(ebook)
        # break #한 권만 추출 됨

def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        yield url

def scrape_detail_page(response):
    #상세페이지의 Respone에서 책 정보를 dict으로 추출
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url': response.url,
        'key': extract_key(response.url),
        'title': root.cssselect('.store_product_info_box h3')[0].text_content(),
        'price': root.cssselect('.pbr strong')[0].text_content(),
        'content':[normalize_spaces(p.text_content()) for p in root.cssselect('#tabs_3 .hanbit_edit_view p')
        if normalize_spaces(p.text_content()) != ''
        ]
    }
    return ebook

def extract_key(url):
    #URL에서 키(URL 끝의 p_code)를 추출함
    m = re.search(r"p_code=(.+)",url)
    return m.group(1)

def normalize_spaces(s):
    #연결돼 있는 공백을 하나의 공백으로 변경
    return re.sub(r'\s+', ' ', s).strip()

if __name__ == '__main__':
    main()