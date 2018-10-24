# 라이브러리 활용(Requests, lxml, beautiful soup, pyquery)

## pip

```
pip install <라이브러리 이름>

//설치된 라이브러리 버전 확인
pip freeze
```



## Requests 로 웹 페이지 추출하기

- urllib는 GET, POST 요청 처리에는 간단함. HTTP 헤더 추가 또는 Basic 인증 처리 등은 복잡해짐
- Requests 모듈로 인터페이스 제공 => 문자 코드 변환, 압축 등을 자동으로 처리

```
pip install requests
```

```python
#Requests.py
#-*-encoding:UTF-8-*-
import requests
r = requests.get('http://hanbit.co.kr')
print(type(r))
#<class 'requests.models.Response'>

print(r.status_code)
#200

#headers 속성으로 HTTP 헤더를 딕셔너리로 추출
print(r.headers['content-type'])
#text/html; charset=UTF-8

print(r.encoding)
#UTF-8

#str 자료형으로 디코딩된 응답 본문 추출
print(r.text)

#content 속성으로 bytes wkfyguddml dmdekq qhsans cncnf
print(r.content)
```

- 헤더에서 인코딩 방식을 추출 => str 자료형으로 디코딩
- 응답 본문에 gzip 등의 압축이 있어도 자동으로 해제됨



## HTML 스크레이핑

- ### XPath와 CSS 선택자

  - XPath(XML Path Language): XML의 특정 요소를 지정할때 사용하는 언어

    - //body/h1 => body의 요소 중 h1태그를 선택
    - 세부적인 조건 지정 가능. 하지만 대부분 CSS 선택자로 처리 가능함

  - CSS 선택자 : CSS로 요소를 디자인 할 때 사용하는 표기방법

    - body > h1 => body의 요소 중 h1태그 선택
    - 사용 권장
    - 최근 스크레이핑할때 class 속성 지정을 많이 사용하는데 CSS 선택자는 이를 간편하게 해줌

  - XPath와 CSS 선택자 비교

    |                         대상 요소                          |                            XPath                             |     CSS 선택자      |
    | :--------------------------------------------------------: | :----------------------------------------------------------: | :-----------------: |
    |                         title 요소                         |                           //title                            |        title        |
    |                body 요소의 후손 중 h1 요소                 |                          //body//h1                          |       body h1       |
    |                body 요소의 자식 중 h1 요소                 |                          //body/h1                           |      body > h1      |
    |              body 요소 내부의 모든 자식 요소               |                           //body/*                           |      body > *       |
    |                  id 속성이 "main"인 요소                   |               id("main") 또는 //*[@id="main"]                |       \#main        |
    |      class 속성으로 "active"를 포함하고 있는 li 요소       | //li[@class and contains(concat(' ', normalize-space(@class), ' '), ' active')] |      li.active      |
    |              type 속성이 "text"인 input 요소               |                    //input[@type="text"]                     | input[type="text"]  |
    |          href 속성이 "http://"로 시작하는 a 요소           |              //a[starts-with(@href, "http://")]              | a[href^="http://"]  |
    |             src 속성이 ".jpg"로 끝나는 img요소             | //img[ends-with(@src, ".jpg")]<br />*XPath 2.0부터 사용가능  |  img[src$=".jpg"]   |
    | 요소의 내부에 "개요"라는 텍스트 노드가 포함돼 있는 h2 요소 |                   //h2[contains(.,"개요")]                   | h2:contains("개요") |
    |    요소의 바로 아래에 "개요"라는 텍스트가 있는 h2 요소     |                     //h2[text()="개요"]                      |          -          |

    - 대체적으로 CSS 선택자가 가독성이 좋고 사용하기 간단해 보인다.
    - 다만 세부적인 조건을 XPath가 설정할 수 있는 것이 많고, CSS 선택자로 불가능한 처리작업도 가능하다.

  - 개발자 도구 활용

    - 웹 브라우저에서 개발자 도구 - 요소 선택
      - copy - copy XPath: XPath 클립보드에 복사
        - //*[@id="gnb"]/ul/li[1]/a
      - copy - copy Selector: CSS 선택자가 클립보드에 복사
        - \#gnb > ul > li:nth-child(1) > a



- ### 라이브러리

  - lxml

    - 파이썬에서 사용하기 쉽게 API를 구현해 놓음

    - C언어로 작성된 XML처리와 관련된 라이브러리인 libxml2와 libxslt를 파이썬으로 바인딩해주는 라이브러리

    - C언어 확장 라이브러리이므로 가장 빠름

    - 초보자에게 추천

    - lxml로 스크레이핑

      - HTML을 파싱할때는 lxml.html 사용

      - ```
        #macOS C확장 모듈 개발전용 패키지설치
        brew install libxml2 libxslt
        
        pip install lxml
        
        #CSS선택자 이용을 위한 cssselect 설치
        pip install cssselect
        ```

      - 

      ```python
      #lxmlScraping.py
      #-*-encoding:UTF-8-*-
      import lxml.html
      tree = lxml.html.parse('full_book_list.html')
      tree = lxml.html.parse('http://example.com/')
      
      #파일 객체를 지정해서 파싱 가능
      from urllib.request import urlopen
      tree = lxml.html.parse(urlopen('http://example.com/'))
      print(type(tree)) #파싱하면 ElementTree 객체 추출
      #<class 'lxml.etree._ElementTree'>
      
      #getroot() 메서드로 html 루트 요소의 HtmlElement 객체 추출 가능
      html = tree.getroot()
      print(type(html))
      #<class 'lxml.html.HtmlElement'>
      
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
      #<class 'lxml.html.HtmlElement'>
      
      #xpath()메서드로 XPath와 일치하는 요소 목록 추출 가능
      print(html.xpath('//li'))
      #[<Element li at 0x10351a638>, <Element li at 0x10351a688>, <Element li at 0x10351a728>]
      
      #cssselect()메서드로 선택자와 일치하는 요소 목록 추출 가능
      print(html.cssselect('li'))
      #[<Element li at 0x110004688>, <Element li at 0x1100046d8>, <Element li at 0x1101895e8>]
      
      h1 = html.xpath('//h1')[0]
      print(h1.tag)
      #h1
      print(h1.text)
      #오늘의 과일
      print(h1.get('id'))
      #main
      print(h1.attrib)
      #{'id': 'main'}
      print(h1.getparent())
      #<Element body at 0x1100046d8>
      ```

    - 실제 사이트 스크레이핑하기

      ```python
      #lxmlScrapingSite.py
      #-*-encoding:UTF-8-*-
      import lxml.html
      
      #HTML 파일을 읽어 들이고, getroot()메서드로 HtmlElement 객체 생성
      tree = lxml.html.parse('full_book_list.html')
      html = tree.getroot()
      
      #cssselect()메서드로 a 요소의 리스트를 추출하고 반복문 실행
      for a in html.cssselect('a'):
          #href 속성과 글자 추출
          print(a.get('href'),a.text)
          
      #결과
      #gnb None
      #top_search None
      #container None
      http://www.hanbit.co.kr/index.html None
      http://www.hanbit.co.kr/media/ 한빛미디어
      http://www.hanbit.co.kr/academy/ 한빛아카데미
      http://www.hanbit.co.kr/biz/ 한빛비즈
      http://www.hanbit.co.kr/life/ 한빛라이프
      http://www.hanbit.co.kr/edu/ 한빛에듀
      http://www.hanbit.co.kr/realtime/ 리얼타임
      http://www.hanbit.co.kr/textbook/ 한빛정보교과서
      http://www.hanbit.co.kr/rent/ 한빛대관서비스
      http://www.hanbit.co.kr/member/login.html 로그인 ... ...
      ```

  - Beautiful Soup

    - 간단하고 직관적인 API를 활용해 데이터 추출 가능

    - 내부적으로 파서를 목적에 맞게 변경 가능

    - ```
      #설치
      pip install beautifulsoup4
      ```

      ```python
      #BeautifulSoup.py
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
      #<h1 id="main">오늘의 과일</h1>
      
      print(type(soup.h1))
      #<class 'bs4.element.Tag'>
      
      #name 속성으로 태그 이름 추출
      print(soup.h1.name)
      #h1
      
      print(soup.h1.string)
      #오늘의 과일
      
      print(soup.ul.text)
      #사과
      #귤
      #포도
      
      print(soup.h1['id'])
      #main
      print(soup.h1.get('id'))
      #main
      print(soup.h1.attrs)
      #{'id': 'main'}
      
      #여러개의 요소인 경우 맨 처음 요소만 추출
      print(soup.li)
      #<li>사과</li>
      
      #키워드 매개변수로 calss 등의 속성을 이용해 지정 가능
      print(soup.find_all('li', class_='featured'))
      #[<li class="featured">귤</li>]
      
      print(soup.find_all(id='main'))
      #[<h1 id="main">오늘의 과일</h1>]
      
      #select()메서드로 CSS 선택자와 일치하는 요소 추출
      print(soup.select('li'))
      #[<li>사과</li>, <li class="featured">귤</li>, <li>포도</li>]
      ```

    - 실제 사이트 스크레이핑

    ```python
    #BeautifulSoupSite.py
    #-*-encoding:UTF-8-*-
    from bs4 import BeautifulSoup
    
    #HTML 파일을 읽어 들이고 BeautifulSop 객체 생성
    with open('full_book_list.html') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    #find_all()메서드로 a요소 우출후 반복문 실행
    for a in soup.find_all('a'):
        #href 속성과 글자 추출
        print(a.get('href'), a.text)
        
    #결과
    #gnb 메뉴 바로가기
    #top_search 검색 및 카테고리 바로가기
    #container 본문 바로가기
    http://www.hanbit.co.kr/index.html HOME
    http://www.hanbit.co.kr/media/ 한빛미디어
    http://www.hanbit.co.kr/academy/ 한빛아카데미
    http://www.hanbit.co.kr/biz/ 한빛비즈
    http://www.hanbit.co.kr/life/ 한빛라이프
    http://www.hanbit.co.kr/edu/ 한빛에듀
    http://www.hanbit.co.kr/realtime/ 리얼타임
    http://www.hanbit.co.kr/textbook/ 한빛정보교과서 ... ...
    ```

  - pyquery

    - 자바스크립트 라이브러리인 jQuery와 같은 인터페이스로 스크레이핑을 할 수 있게 해주는 라이브러리

    - 내부적으로는 lxml을 사용함

    - ```
      pip install pyquery
      ```

    - 

    ```python
    #pyqueryScraping.py
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
    #<h1 id="main">오늘의 과일</h1>
    
    print(d('h1').text())
    #오늘의 과일
    
    print(d('h1').attr.id)
    #main
    
    print(d('li'))
    #<li>사과</li>
    #        <li class="featured">귤</li>
    #        <li>포도</li>
    
    print(d('body').find('li'))
    #<li>사과</li>
    #        <li class="featured">귤</li>
    #        <li>포도</li>
    
    #filter()메서드로 리스트 필터링
    print(d('li').filter('.featured'))
    #<li class="featured">귤</li>
    
    ```

