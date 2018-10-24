#-*-encoding:UTF-8-*-

#PyQuery 클래스를 pq라는 이름으로 읽기
from pyquery import PyQuery as pq

d = pq(filename='full_book_list.html')
d = pq(url='http://example.com/')

#문자열 파싱
d = pq('''
    <html>
    <head><title>온라인 과일 가게</titl></head>
    <body>
    <h1 id="main">오늘의 과일</h1>
    <ul>
        <li>사과</li>
        <li class="featured">귤</li>
        <li>포도</li>
    </ul>
    </body>
    </html>
''')

print(d('h1'))
#

print(d('h1').text())
#

print(d('h1').attr.id)
#

print(d('li'))
#

print(d('body').find('li'))

#filter()메서드로 리스트 필터링
print(d('li').filter('.featured'))
