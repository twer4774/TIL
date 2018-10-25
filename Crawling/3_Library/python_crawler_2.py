#-*-coding:UTF-8-*-

import requests
import lxml.html

response = requests.get('http://hanbit.co.kr/store/books/new_book_list.html')

root = lxml.html.fromstring(response.content)

#모든 링크를 절대 URL로 변환
root.make_links_absolute(response.url)

#선택자를 추가
for a in root.cssselect('.view_box .book_tit a'):
    url = a.get('href')
    print(url)