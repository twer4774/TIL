#-*-encoding:UTF-8-*-
from bs4 import BeautifulSoup

'''
첫 번재 매개변수에 파일 객체를 지정해 BeautifulSoup 객체 생성
BeautifulSoup()에는 파일 이름 또는 URL을 지정할 수 없음
두 번째 매개변수에는 파서의 종류 지정
'''

with open('full_book_list.html') as f:
    soup = BeautifulSoup(f, 'html.parser')


#BeautifulSoup todtjdwkdpsms HTML 문자열을 전달 할 수 있음
soup = BeautifulSoup('''
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
''', 'html.parser')

#h1요소 추출
print(soup.h1)

print(type(soup.h1))

#name 속성으로 태그 이름 추출
print(soup.h1.name)

print(soup.h1.string)

print(soup.ul.text)

print(soup.h1['id'])
print(soup.h1.get('id'))
print(soup.h1.attrs)

#여러개의 요소인 경우 맨 처음 요소만 추출
print(soup.li)

#키워드 매개변수로 calss 등의 속성을 이용해 지정 가능
print(soup.find_all('li', class_='featured'))

print(soup.find_all(id='main'))

#select()메서드로 CSS 선택자와 일치하는 요소 추출
print(soup.select('li'))

