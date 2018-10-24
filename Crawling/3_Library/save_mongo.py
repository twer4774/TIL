#_*_coding:UTF-8_*_

import lxml.html
from pymongo import MongoClient

#HTML 파일을 읽어들이고 getroot()메서드를 사용해 HtmlElement객체를 추출
tree = lxml.html.parse('full_book_list.html')
html = tree.getroot()

client = MongoClient('localhost', 27017)
db = client.scraping #scraping 데이터베이스 추출
collection = db.links #links 콜렉션 추출

#스크립트를 여러번 사용해도 같은 겨로가를 출력하도록 콜렉션의 문서를 제거함
collection.delete_many({})

#cssselect()메서드로 a요소의 목록 추출
for a in html.cssselect('a'):
    #href 속성과 링크의 글자를 추출해서 저장
    collection.insert_one({
        'url': a.get('href'),
        'title': a.text,
    })

#콜렉션의 모든 문서를 _id 순서로 정렬해서 추출
for link in collection.find().sort('_id'):
    print(link['_id'], link['url'], link['title'])