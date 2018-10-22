# 파이썬을 이용한 크롤링/스크레이핑

- 웹 사이트에서 데이터를 가져올 때 비동기 처리를 권장함
- 파이썬에는 Twistd, Troando 등 비동기 처리를 위한 프레임워크가 있음
  - asyncio 비동기 처리를 위한 표준 라이브러리 제공(python 3.4버전 이후)
- 파이썬으로 과학 기술 계산 분야 이용 NumPy, SciPy
  - pandas: NumPy를 기반으로 만들어진 데이터 전처리, 집계 라이브러리
  - matplotlib: 숫자 데이터를 그래프로 시각화 할 수 있는 라이브러리

## 가상환경

- 같은 라이브러리를 다른 버전으로 설치하여 프로그램을 동작 시킬 때 유용함

- 가상환경 사용법

  ```
  //생성
  python3 -m venv scraping
  
  //가상환경 들어감 => .(점) 명령어로 activate 스크립트 실행(bash, zsh에서는 source 명령어 사용)
  . scraping/bin/activate
  
  //파이썬 경로확인
  which python
  /Users/wonik/Desktop/TIL/TIL/Crawling/scraping/bin/python
  
  //종료
  eactivate
  ```



## 파이썬으로 웹 페이지 추출하기

- urllib 표준 라이브러리 이용
- 웹 페이지를 추출할 대는 HTTP헤도와 HTML의 meta태그를 기반으로 인코딩 방식을 판별해야함 => 정확히 판별해야 웹 페이지의 내용을 정확하게 추출할 수 있음

```python
#usingUrllib.py
#-*-coding:utf-8-*-
from urllib.request import urlopen
f = urlopen('http://hanbit.co.kr')
#urlopen()함수는 HTTPResponse 자료형의 객체를 반환함

print(type(f))

#read()메서드로 HTTP응답 본문을 추출
print(f.read())


print(f.status) #상태코드 추출
#200

print(f.getheader('Content-Type')) #HTTP 헤더 값 추출
#text/html; charset=UTF-8
```



### 문자 코드 다루기

- HTTPRespnse.read() 메서드로 추출할 수 있는 응답 본문의 값은 bytes 자료형이므로 문자열로 다루려면 문자 코드로 디코딩해야 함

- HTTP 헤더에서 인코딩 방식 추출하기

  HTTP 응답의 Content-Type 헤더를 참조하면 해당 페이지에 사용되고 있는 인코딩 방식을 알아 낼 수 있음

  text/html

  txt/html; charset=UTF-8

  text/html; charset=EUC-KR

```python
#urlopen_encoding.py
#-*-encoding:UTF-8-*-
import sys
from urllib.request import urlopen
f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')

#HTTP헤더를 기반으로 인코딩 방식을 추출(명시 되지 않으면 utf-8 사용)
encoding = f.info().get_content_charset(failobj="utf-8")

#인코딩 방식을 표준 오류에 출력
print('encoding:', encoding, file=sys.stderr)

#추출한 인코딩 방식으로 디코딩
text= f.read().decode(encoding)
#웹 페이지의 내용을 표준 출력에 출력
print(text)

#결과
encoding: utf-8
<!DOCTYPE html>
<html lang="ko">
<head>
<!--[if lte IE 8]>
<script>
  location.replace('/support/explorer_upgrade.html');
</script>
<![endif]-->
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-W9D5PM3');</script>
<!-- End Google Tag Manager -->
<meta charset="utf-8"/>
<title>한빛출판네트워크</title>
<link rel="shortcut icon" href="http://www.hanbit.co.kr/images/common/hanbit.ico">
<meta http-equiv="X-UA-Compatible" content="IE=Edge" />
<meta property="og:type" content="website"/>
<meta property="og:title" content="한빛출판네트워크"/> ... ...
```



#### 파일을 만들어 저장하는 방법

python3 urlopen_encoding.py > dp.html



## meta 태그에서 인코딩 방식 추출하기

- HTTP헤더에서 추출한 인코딩 정보가 항상 맞는것은 아님 => 웹 서버 설정이 잘못된 경우 형식이 다를 수 있음
- meta 태그에서 인코딩 방식 확인 가능
  - \<meta charset="utf-8">
  - \<meta http-equiv="Content-Type" content="text/html"; charset=EUC_KR">

```python
#meta 태그에서 인코딩 방식 추출
#-*-encoding:UTF-8-*-

import re
import sys
from urllib.request import urlopen

f= urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
#bytes 자료형의 응답 본문을 일단 변수에 저장
bytes_content = f.read()

#charset은 HTML 앞부분에 적혀있는 경우가 많음
#응답 본문의 앞부분 1024바이트를 ASCII 문자로 디코딩 해둠
#ASCII 범위 이외의 문자는 U+FFFD(REPLACEMENT CHARATER)로 변환되어 예외가 발생되지 않음
scanned_text = bytes_content[:1024].decode('ascii', errors='replace')

#디코딩한 문자열에서 정규 표현식으로 charset 값을 추출함
match =re.search(r'charset=["\']?([\w-]+)', scanned_text)
if match:
    encoding = match.group(1)
else:
    # charset이 명시돼 있지 않으면 UTF-8을 사용함
    encoding = 'utf-8'

#추출한 인코딩을 표준 오류에 출력함
print('encoding', encoding, file=sys.stderr)

#추출한 인코딩으로 다시 디코딩
text = bytes_content.decode(encoding)
#응답 본문을 표준 출력에 출력
print(text)

#결과
encoding utf-8
<!DOCTYPE html>
<html lang="ko">
<head>
<!--[if lte IE 8]>
<script>
  location.replace('/support/explorer_upgrade.html');
</script>
<![endif]-->
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-W9D5PM3');</script>
<!-- End Google Tag Manager -->
<meta charset="utf-8"/>
<title>한빛출판네트워크</title>
<link rel="shortcut icon" href="http://www.hanbit.co.kr/images/common/hanbit.ico">
<meta http-equiv="X-UA-Compatible" content="IE=Edge" />
<meta property="og:type" content="website"/>
<meta property="og:title" content="한빛출판네트워크"/>
<meta property="og:description" content="출판사, IT전문서, 대학교재, 경제경영, 어린이/유아, MAKE, 실용/여행, 전자책, 인터넷 강의"/>
<meta property="og:image" content="http://www.hanbit.co.kr/images/hanbitpubnet_logo.jpg" />
<meta property="og:url" content="http://www.hanbit.co.kr/store/books/full_book_list.html"/>
<link rel="canonical" href="http://www.hanbit.co.kr/store/books/full_book_list.html" />
<meta name="keywords" content="책,전자책,ebook,출판사,동영상,콘텐츠,강의,자격증,대학교재" />... ...
```



## 웹 페이지에서 데이터 추출하기(스크레이핑)

- 표준 라이브러리로 저장한 파일에서 서적의 제목과 URL 데이터 추출
- 추출 방법: 대상 웹사이트에 따라 구분하여 사용
  - 정규 표현식: HTML을 단순한 문자열로 취급하고 필요한 부분을 추출함
  - XML 파서:  XML 파싱 후  필요한 정보 추출. 블로그, 뉴스사이트 처럼 많은 정보가 XML로 제공됨. 정규표현식보다 정확함

#### 정규표현식으로 스크레이핑

- 정규 표현식에는 백슬러시가 많이 나오는데 일반 문자열로 처리하기 위해서는 두번해줘야함
- raw문자열이라고 부르는 r'...'형식의 문자열 리터럴을 사용하면 백슬러시가 이스케이프 문자열로 인식되지 않음

```python
#regular_expression_scraping.py
#-*-encoding:UTF-8-*-
import re

print(re.search(r'a.*c', 'abc123DEF'))
#<re.Match object; span=(0, 3), match='abc'>

print(re.search(r'a.*d', 'abc123DEF'))
#None(빈 화면)

#세번째 매개변수로 옵션 지정. re.IGNORECASE(or re.I) => 대소문자 무시
print(re.search(r'a.*d', 'abc123DEF', re.IGNORECASE))
#<re.Match object; span=(0, 7), match='abc123D'>

#Match 객체의 group()메서드로 일치한 값을 추출
#매개변수에 0을 지정하면 매치된 모든 값을 반환
m = re.search(r'a(.*)c', 'abc123DEF')
print(m.group(0))
#abc
print(m.group(1))
#b

#re.findall()함수로 정규표현식에 맞는 모든 부분 추출
#\w는 유니코드로 글자를 비교. 공백 문자는 \s로 추출 가능
#2글자 이상 단어 추출
print(re.findall(r'\w{2,}', 'This is a pen'))
#['This', 'is', 'pen']


#re.sub()함수를 사용하면 정규 표현식에 맞는 부분을 바꿀 수 있음
#3번째 매개변수에 넣은 문자열에서 첫 번째 정규 표현식에 맞는 부분을 2번째 매개변수로 변경
print(re.sub(r'\w{2,}', 'That', 'This is a pen'))
#That That a That
```



### 책 제목과 URL 추출

```python
#scrape_re.py
#-*-encoding:UTF-8-*-
import re
from html import unescape

with open('dp.html') as f:
    html = f.read()

#re.findall()을 사용해 도서 하나에 해당하는 HTML cncnf
for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
    #도서의 URL추출
    url = re.search(r'<a href="(.*?)">', partial_html).group(1)
    url = 'http://www.hanbit.co.kr' + url
    #태그를 제거해서 도서의 제목을 추출
    title = re.sub(r'</*?>', '', partial_html)
    title =unescape(title)
    print('url:', url)
    print('title:', title)
    print('---')


#결과
url: http://www.hanbit.co.kr/store/books/look.php?p_code=B9796997266
title: <td class="left"><a href="/store/books/look.php?p_code=B9796997266">(무료동영상) 2019 전기산업기사 필기</a></td>
---
url: http://www.hanbit.co.kr/store/books/look.php?p_code=B1401258166
title: <td class="left"><a href="/store/books/look.php?p_code=B1401258166">(무료동영상) 2019 전기기사 필기</a></td>
---
url: http://www.hanbit.co.kr/store/books/look.php?p_code=B4559886540
title: <td class="left"><a href="/store/books/look.php?p_code=B4559886540">리얼 블라디보스톡  PLUS 우수리스크 [2019~2020년 최신판]</a></td>
---
url: http://www.hanbit.co.kr/store/books/look.php?p_code=B1052483362
title: <td class="left"><a href="/store/books/look.php?p_code=B1052483362">프라이드</a></td>
---
```



### XML(RSS) 스크레이핑

- RSS: 블로그 또는 뉴스 사이트 등의 웹사이트는 변경 정보등을 RSS라는 이름의 XML 형식으로 제공 => HTML 간단하게 파싱 가능

- 날씨 정보 데이터 받아서 rss.xml로 변경 wget http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109

```python
#scrape_rss.py
#-*-encoding:UTF-8-*-
from xml.etree import ElementTree

#parrse() 함수로 파일을 읽어 들이고 ElementTree 객체를 만듦
tree = ElementTree.parse('rss.xml')

#getroot() 메서드로 xml의 루트 요소를 추가
root = tree.getroot()

#findall()메서드로 요소 목록 추출
for item in root.findall('channel/item/description/body/location/data'):
    #find()메서드로 요소를 찾고 text 속성으로 값을 추출
    tm_ef = item.find('tmEf').text
    tmn = item.find('tmn').text
    tmx = item.find('tmx').text
    wf = item.find('wf').text
    print(tm_ef, tmn, tmx, wf)
    
#결과
2018-10-25 00:00 10 20 구름조금
2018-10-25 12:00 10 20 구름조금
2018-10-26 00:00 10 16 구름많음
2018-10-26 12:00 10 16 흐리고 비
2018-10-27 00:00 8 14 구름조금
2018-10-27 12:00 8 14 구름조금
2018-10-28 00:00 6 14 구름많음
2018-10-28 12:00 6 14 구름많고 비
2018-10-29 00:00 5 12 구름많음
2018-10-29 12:00 5 12 구름많음
2018-10-30 00:00 5 11 구름조금
2018-10-31 00:00 6 13 구름많음
2018-11-01 00:00 7 14 구름조금
2018-10-25 00:00 10 19 구름조금
2018-10-25 12:00 10 19 구름조금
2018-10-26 00:00 12 16 구름많음
2018-10-26 12:00 12 16 흐리고 비
2018-10-27 00:00 9 13 구름조금
2018-10-27 12:00 9 13 구름조금
2018-10-28 00:00 7 14 구름많음
2018-10-28 12:00 7 14 구름많고 비
2018-10-29 00:00 6 11 구름많음 ... ...
```



## 데이터 저장하기

### CSV(Comma-Seperated Values)형식으로 저장

- 쉼표로 구분하는 텍스트 형식
- 행과 열로 구성되는 2차원 데이터를 저장할 때 사용

```python
#save_csv_join.py
#-*-encoding:UTF-8-*-
print('rank,city,population')

#join()메서드의 매개변수로 저달한 list는 str이어야 함
print(','.join(['1', '상하이', '24150000']))
print(','.join(['2', '카라치', '23500000']))
print(','.join(['3', '베이징', '21515500']))
print(','.join(['4', '텐진', '124596990']))
print(','.join(['5', '이스탄불', '11102223']))

#결과
rank,city,population
1,상하이,24150000
2,카라치,23500000
3,베이징,21515500
4,텐진,124596990
5,이스탄불,11102223

#파일로 저장하기(리다이렉트)
pyhon3 save_csv_join.py > top_cities.csv
```

```python
#save_csv.py
#csv모듈 사용 => csv파일이 생성됨
#-*-encoding:UTF-8-*-
import csv

with open('top_cities.csv', 'w', newline='') as f:
    #csv.writer는 파일 객체를 매개 변수로 지정
    writer = csv.writer(f)
    #첫번째 줄에는 헤더 작성
    writer.writerow(['rank', 'city', 'population'])

    writer.writerows([
        ['1', '상하이', '24150000'],
        ['2', '카라치', '23500000'],
        ['3', '베이징', '21515500'],
        ['4', '텐진', '124596990'],
        ['5', '이스탄불', '11102223']
    ])


```



### JSON(JavaScript Object Notation)형식으로 저장

```python
#save_json.py
#json.dumps()함수 이용
#-*-encoding:UTF-8-*-
import json

cities = [
    {'rank': 1, 'city': '상하이', 'population': 100},
    {'rank': 2, 'city': '카라치', 'population': 99},
    {'rank': 3, 'city': '베이징', 'population': 98},
    {'rank': 4, 'city': '텐진', 'population': 97},
    {'rank': 5, 'city': '이스탄불', 'population': 96},
]

#ASCII이외의 문자열을 \uxxxx라는 형태로 이스케이프 하지 않고 출력
#indent=2로 2개의 고백으로 들여쓰기 해줌
print(json.dumps(cities, ensure_ascii=False, indent=2))

#파일로 저장할때는 
#with open('top_cities.json', 'w') as f:
#    json.dump(cities, f)

#결과
[
  {
    "rank": 1,
    "city": "상하이",
    "population": 100
  },
  {
    "rank": 2,
    "city": "카라치",
    "population": 99
  },
  {
    "rank": 3,
    "city": "베이징",
    "population": 98
  },
  {
    "rank": 4,
    "city": "텐진",
    "population": 97
  },
  {
    "rank": 5,
    "city": "이스탄불",
    "population": 96
  }
]
```



### sqlite로 저장하기

- 가볍게 사용할수 있지만 파일 저장시 시간이 오래걸림 => 대용량일때는 병목현상이 발생
- MySQL 또는 MongoDB로 병목현상 해결

```python
#save_sqlite3.py
#-*-encoding:UTF-8-*-
import sqlite3

conn = sqlite3.connect('top_cities.db')

#커서 추출
c = conn.cursor()

#execute()메서드로 SQL구문 실행
c.execute('DROP TABLE IF EXISTS cities')

#cities 테이블 새성
c.execute('''
    CREATE TABLE cities(
        rank integer,
        city text,
        population integer
    )
''')

#execute()메서드의 두번째 매개변수에는 파라미터를 지정할 수 있음
c.execute('INSERT INTO cities VALUES (?, ?, ?)', (1, '상하이', 100))

#딕셔너리 저장
c.execute('INSERT INTO cities VALUES(:rank, :city, :population)',{'rank': 2, 'city': '카라치', 'population': 99})

#리스트로 저장
c.executemany('INSERT INTO cities VALUES(:rank, :city, :population)', [
    {'rank': 3, 'city': '베이징', 'population': 98},
    {'rank': 4, 'city': '텐진', 'population': 97},
    {'rank': 5, 'city': '이스탄불', 'population': 96},
])

#변경 사항 저장
conn.commit()

#저장 데이터 추출
c.execute('SELECT * FROM cities')
#쿼리의 결과는 fetcall()메서드로 추출
for row in c.fetchall():
    #추출한 데이터 출력
    print(row)

#연결 닫기
conn.close()

#결과
(1, '상하이', 100)
(2, '카라치', 99)
(3, '베이징', 98)
(4, '텐진', 97)
(5, '이스탄불', 96)
```



## 정리

```python
#python_scraper.py => books.db 파일 생성
#-*-encoding:UTF-8-*-
import re
import sqlite3
from urllib.request import urlopen
from html import unescape

def main():
    """
    메인 처리
    """
    html = fetch('http://www.hanbit.co.kr/store/books/full_book_list.html')
    books = scrape(html)
    save('books.db', books)

def fetch(url):
    """url 기반으로 웹페이지 추출"""
    f = urlopen(url)
    encoding = f.info().get_content_charset(failobj="utf-8")
    html = f.read().decode(encoding)
    return html

def scrape(html):
    """정규표현식으로 도서 정보 추출"""
    books = []

    for partial_html in re.findall(r'<td class="left">Ma.*?</td>', html, re.DOTALL):
        #도서의 URL 추출
        url = re.search(r'<a href="(.*?)">', partial_html).group(1)
        url = 'http://www.hanbit.co.kr' + url
        #태그를 제거해 도서의 제목 추출
        title = re.sub(r'<.*?>', '', partial_html)
        title = unescape(title)
        books.append({'url': url, 'title': title})

    return books

def save(db_path, books):
    """sqlite로 저장"""
    
    conn = sqlite3.connect(db_path)

    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS books')
    c.execute('''CREATE TABLE books( title text, url text) ''')

    c.executemany('INSERT INTO books VALUES (:title, :url)', books)
    conn.commit()
    conn.close()

#python명령어로 실행한 경우 main() 함수 호출
if __name__ == '__main__':
    main()
 
```

