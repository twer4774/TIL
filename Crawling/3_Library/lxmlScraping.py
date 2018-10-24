#-*-encoding:UTF-8-*-
import lxml.html
tree = lxml.html.parse('full_book_list.html')
tree = lxml.html.parse('http://example.com/')

#파일 객체를 지정해서 파싱 가능
from urllib.request import urlopen
tree = lxml.html.parse(urlopen('http://example.com/'))
print(type(tree)) #파싱하면 ElementTree 객체 추출

#getroot() 메서드로 html 루트 요소의 HtmlElement 객체 추출 가능
html = tree.getroot()
print(type(html))

#fromstring() 함수로 문자열(str 자료형 또는 bytes 자료형) 파싱 가능
#주의 사항: encoding이 지정된 XML 선언을 포함한 str을 파싱하면 ValueError가 발생함
html = lxml.html.fromstring('''
    <html>
    <head><title>온라인 과일 가게</title></head>
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
#fromstring()함수로 직접 HtmlElement 객체를 추출 할 수 있음
print(type(html))

#xpath()메서드로 XPath와 일치하는 요소 목록 추출 가능
print(html.xpath('//li'))

#cssselect()메서드로 선택자와 일치하는 요소 목록 추출 가능
print(html.cssselect('li'))

h1 = html.xpath('//h1')[0]
print(h1.tag)
print(h1.text)
print(h1.get('id'))
print(h1.attrib)
print(h1.getparent())