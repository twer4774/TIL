#-*-coding:UTF-8-*-

import requests
import lxml.html

def main():
    #여러페이지를 크롤링하기위해 Session사용
    session = requests.Session()
    response = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)

    for url in urls:
        response = session.get(url) #Session으로 상세페이지 추출
        ebook = scrape_detail_page(response) #상세페이지에서 상세 정보 추출
        print(ebook)
        break #한 권만 추출 됨

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
        'title': root.cssselect('.store_product_info_box h3')[0].text_content(),
        'price': root.cssselect('.pbr strong')[0].text_content(),
        'content':[p.text_content() for p in root.cssselect('#tabs_3 .hanbit_edit_view p')]
    }
    return ebook

if __name__ == '__main__':
    main()