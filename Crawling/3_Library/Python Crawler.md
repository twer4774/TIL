# 크롤러와 URL

- 크롤러는 웹페이제 존재하는 하이퍼링크를 따라 돌아야 함 => URL 관련 지식 필요

- 크롤러를 만들기 위한 준비 

  - URL 관련지식

    - URL 구조

      - Uniform Resource Locator의 약자로 인터넷에 존재하는 리소스의 위치를 나타내는 식별자
      - http://example.com/main/index?q=python#lead
      - http: 스키마. http 또는 https 같은 프로토콜
      - example: 어서리티. //뒤에 나오는 일반적인 호스트 이름. 사용자 이름, 비밀번호, 포트번호등 포함
      - main/index: 경로. /로 시작하는 해당 호스트 내부에서의 리소스 경로
      - q=python: 쿼리.
      - lead: 플래그먼트. #뒤에 나오는 리소스 내부의 특정부분

    - a 태그의 href 속성에서 다른 페이지의 URL을 추출해야 함

      - 절대 URL
        - https:// 등의 스키마로 시작하는 URL
      - 상대 URL
        - 절대 URL을 기준으로 상대적으로 잡는 경로
          1. //로 시작하는 URL => //cdn.example.com/logo.png
          2. /로 시작하는 상대 URL => /articles/
          3. 상대 경로 형식을 사용하는 상대 URL => ./

    - 상대 URL을 절대 URL로 변환하기

      - urllib.parse 모듈의 urljoin()함수 이용
      - 첫번째 매개변수에 기준이 되는 url을 지정, 두번째 매개변수에 상대 url 지정

      ```python
      >>> from urllib.parse import urljoin
      >>> base_url = 'http://example.com/books/top.html'
      >>> urljoin(base_url, '//cdn.example.com/logo.png')
      'http://cdn.example.com/logo.png'
      >>> urljoin(base_url, '/articles/')
      'http://example.com/articles/'
      ```

  - 퍼머링크와 링크 구조 패턴

    - 퍼머링크
      - 최근의 웹사이트는 하나의 uests로 웨페이콘텐츠가 하나의 URL에 대응
      - 퍼머링크: 대응하는 컨텐츠가 변하지 않는 URL
      - 퍼머링크를 가진 웹사이트는 검색엔진의 크롤러가 콘텐츠를 인식하기 쉬움
    - 목록/상세 패턴
      - 퍼머링크를 사요하는 웹사이트는 퍼머링크를 가진 페이지로 연결되는 목록페이지가 존재함
      - 목록페이지: http://www.hnabilt.co.kr/store/store_submain.html
      - 상세페이지: http://www.hanbit.co.kr/stroe/books/look.php?p_code=B123456



## 파이썬으로 크롤러 만들기

- Requests로 웹페이지 추출
- lxml로 웹페이지 스크레이핑
- PyMongo로 MongoDB에 데이터 저장
- 한빛 미디어의 새로나온 책에서 제목, 가격, 목차 정보 추출

### 목록 페이지에서 퍼머 링크 목록 추출하기

- http://www.hanbit.co.kr/store/books/new_book_list.html : 새로 나온 책 목록 출력
  - view_box 클래스 속성안에 div 태그 내부에 a 태그 확인

```python
#python_crawler_1.py
#-*-coding:UTF-8-*-

import requests
import lxml.html

response = requests.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
root = lxml.html.fromstring(response.content)
for a in root.cssselect('.view_box a'):
    url = a.get('href')
    print(url)
    
#결과
/store/books/look.php?p_code=B8608817158
javascript:;
/store/books/look.php?p_code=B8608817158
/store/books/look.php?p_code=B1401258166
javascript:;
/store/books/look.php?p_code=B1401258166
/store/books/look.php?p_code=B9796997266
javascript:;
```

- javascript:; 라는 제외 할 대상이 있음  => 더 들어가서 book_tit에 a 태그로 더 정확히 찾을 수 있음
- 추출한 대상을 보면 URL이 상대 URL주소로 추출되어있음 => 절대 URL 주소로 변환 필요(make_links_absolute()이용)

```python
#python_crawler_2.py
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
    
#결과
http://www.hanbit.co.kr/store/books/look.php?p_code=B8608817158
http://www.hanbit.co.kr/store/books/look.php?p_code=B1401258166
http://www.hanbit.co.kr/store/books/look.php?p_code=B9796997266
http://www.hanbit.co.kr/store/books/look.php?p_code=B4559886540
http://www.hanbit.co.kr/store/books/look.php?p_code=B7076585695
http://www.hanbit.co.kr/store/books/look.php?p_code=B3202466252
http://www.hanbit.co.kr/store/books/look.php?p_code=B1052483362
http://www.hanbit.co.kr/store/books/look.php?p_code=B7473583156
http://www.hanbit.co.kr/store/books/look.php?p_code=B7883656935
http://www.hanbit.co.kr/store/books/look.php?p_code=B4743554662
http://www.hanbit.co.kr/store/books/look.php?p_code=B6952054209
http://www.hanbit.co.kr/store/books/look.php?p_code=B2845507407
http://www.hanbit.co.kr/store/books/look.php?p_code=B6910482773
http://www.hanbit.co.kr/store/books/look.php?p_code=B4458049183
```

- 확장성을 고려해 함수단위로 리펙터링

```python
#python_crawler_3.py
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
```



### 상세페이지 스크레이핑 하기

- 개발자 도구로 상세페이지의 타이틀, 가격, 목차 확인

| 요소   | CSS 선택자                               |
| ------ | ---------------------------------------- |
| 타이틀 | .store_product_info_box h3               |
| 가격   | .pbr strong                              |
| 목차   | \#tabs_3 .hanbit_edit_view 내부의 p 태그 |

```python
#python_crawler_4.py
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
    
#결과
{'url': 'http://www.hanbit.co.kr/store/books/look.php?p_code=B8608817158', 'title': 'IT 트렌드 스페셜 리포트 2019', 'price': '16,020', 'content': ['', '프롤로그\xa0', '\r\n\t\t\t\t\t1장. 인공지능 : 비즈니스의 경쟁력을 만들어내는 기반 기술\r\n', '01. 비즈니스에 미치는 영향\xa0', '02. 유용한 활용처\xa0', '03. 주목해야 하는 회사\xa0', '04. 실패 사례로 보는 한계점\xa0', '05. 전망\xa0', '06. 핵심 키워드 요약\xa0', '[테크 리포트] 솔리드웨어 : 세계가 인정하는 머신러닝 자동화 솔루션\xa0', '\xa0', '\r\n\t\t\t\t\t2장. 5G : 무지연 비즈니스 플랫폼의 탄생\r\n', '01. 4G가 만드는 비즈니스 변화', '02. 5G 탄생', '03. 5G를 활용한 모바일 서비스 변화\xa0', '04. 모바일 서비스 시나리오\xa0', '05. 국내 주요 사업자 동향\xa0', '06. 해외 동향\xa0', '07. 제약 사항\xa0', '08. 전망\xa0', '09. 핵심 키워드 요약\xa0', '[테크 리포트] SK텔레콤 : 5G 시대 선도 전략\xa0', '\xa0', '\r\n\t\t\t\t\t3장. 로봇 : 산업 현장을 넘어 일상으로\r\n', '01. 비즈니스 가치와 원인\xa0', '02. 활용 사례\xa0', '03. 주목해야 하는 회사\xa0', '04. 국가별 현황\xa0', '05. 주요 쟁점\xa0', '06. 전망\xa0', '07. 핵심 키워드 요약\xa0', ... ...
```

- 공백과 의미 없는 문자열 제거를 위해 정규표현식 이용

```python
#-*-coding:UTF-8-*-

import re
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
        'content':[normalize_spaces(p.text_content()) for p in root.cssselect('#tabs_3 .hanbit_edit_view p')
        if normalize_spaces(p.text_content()) != ''
        ]
    }
    return ebook

def normalize_spaces(s):
    #연결돼 있는 공백을 하나의 공백으로 변경
    return re.sub(r'\s+', ' ', s).strip()

if __name__ == '__main__':
    main()
    
#결과
{'url': 'http://www.hanbit.co.kr/store/books/look.php?p_code=B8608817158', 'title': 'IT 트렌드 스페셜 리포트 2019', 'price': '16,020', 'content': ['프롤로그', '1장. 인공지능 : 비즈니스의 경쟁력을 만들어내는 기반 기술', '01. 비즈니스에 미치는 영향', '02. 유용한 활용처', '03. 주목해야 하는 회사', '04. 실패 사례로 보는 한계점', '05. 전망', '06. 핵심 키워드 요약', '[테크 리포트] 솔리드웨어 : 세계가 인정하는 머신러닝 자동화 솔루션', '2장. 5G : 무지연 비즈니스 플랫폼의 탄생', '01. 4G가 만드는 비즈니스 변화', '02. 5G 탄생', '03. 5G를 활용한 모바일 서비스 변화', '04. 모바일 서비스 시나리오', '05. 국내 주요 사업자 동향', '06. 해외 동향', '07. 제약 사항', '08. 전망', '09. 핵심 키워드 요약', '[테크 리포트] SK텔레콤 : 5G 시대 선도 전략', '3장. 로봇 : 산업 현장을 넘어 일상으로', '01. 비즈니스 가치와 원인', '02. 활용 사례', '03. 주목해야 하는 회사', '04. 국가별 현황', '05. 주요 쟁점', '06. 전망', '07. 핵심 키워드 요약', '[테크 리포트] 뉴로메카 : RaaS로서의 협동로봇', '4장. 드론 : 지능형 드론 시대의 개막', '01. 비즈니스 가치와 원인', '02. 농업에서 우주 개발까지', '03. 주목할 만한 회사', '04. 유인 드론, 꿈이 현실로', '05. 인공지능, 드론을 진화시키다', '06. 전망', '07. 핵심 키워드 요약', '[테크 리포트] (주)엑스드론 : 다목적 임무용 무인기 상용화', '5장. 대화형 플랫폼 : 새로운 사용자 경험의 탄생', '01. 비즈니스 가치와 원인', '02. 대화형 플랫폼의 응용 사례', '03. 주목해야 하는 회사', '04. 한계점, 제약 사항', '05. 전망', '06. 핵심 키워드 요약', '[테크 리포트] 마인즈랩 : 고객접점 서비스의 미래, AI 컨택 센터', '6장. 실감형 미디어 : 포스트 중심기기로서 가능성', '01. 비즈니스 가치와 원인', '02. 활용 사례', '03. 주목해야 하는 회사', '04. 주요 쟁점 / 한계점과 제약 사항', '05. 전망', '06. 핵심 키워드 요약', '[테크 리포트] (주)살린 : VR 소셜 TV 플랫폼, 에픽라이브', '7장. 블록체인 : 생태 지도와 차세대 기술', '01. 실물 경제 시스템의 패러다임 변화', '02. 국내 블록체인 생태 지도', '03. 혁신 경제 시스템으로서의 쟁점', '04. 블록체인 채용 적합성 판단', '05. 블록체인 기술의 4가지 과제', '06. 합의 알고리즘 문제', '07. 오라클 문제', '08. 전망', '09. 핵심 키워드 요약', '[테크 리포트] ICON : 국내 최초의 본격적인 DApp 플랫폼']}
```



### 상세페이지 크롤링

- 위의 코드에서 main()함수의 break제거. time.sleep(1)을 넣어 크롤링함 => 1초마다 다음 책 상세정보 표출

#### 스크레이핑 한 데이터 저장

- MongoDB 이용
- 한번 크롤링한 URL은 다시 크롤링하지 않게 하기
- 위의 코드와 다른점: 위의 코드에서는 Session을 이용해 여러 페이지를 크롤링했지만, 여기서는 MongoDB에 저장해서 그런지 Session을 사용하지 않음

```python
#python_crawler_final.py
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
```

