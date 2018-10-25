#-*-coding:UTF-8-*-

import requests
import lxml.html

def main():
    #여러 페이지에서 크롤링 할 것 이므로 Session 사용
    session = requests.Session()
    #scrape_list_page() 함수로 제너레이터 추출
    response = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')

    urls = scrape_list_page(response)
    #제너레이터는 list처럼 사용 가능
    for url in urls:
        print(url)

def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        #yield 구문으로 제너레이터의 요소 반환
        yield url

if __name__ == '__main__':
    main()