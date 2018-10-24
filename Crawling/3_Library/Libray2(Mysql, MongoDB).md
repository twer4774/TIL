# 라이브러리  활용2

## RSS스크레이핑

- feedparser를 이용하면 ElementTree보다 간단하게 데이터 추출 가능
- 설치

```
pip install feedparser
```

```python
#feedparserScrapingSite.py
#-*-coding:UTF-8-*-
import feedparser

d = feedparser.parse('http://www.aladin.co.kr/rss/new_all/351')

for entry in d.entries:
    print('이름:', entry.title)
    print('링크', entry.link)
    print()
    
#결과
이름: Do it! 오라클로 배우는 데이터베이스 입문/이지훈 지음/이지스퍼블리싱
링크 http://www.aladin.co.kr/rsscenter/go.aspx?rssType=2&type=item&itemId=171630125

이름: 씽크톡톡 윈도우10 & 인터넷 활용/웰북교재연구회 지음/웰북(WellBook)
링크 http://www.aladin.co.kr/rsscenter/go.aspx?rssType=2&type=item&itemId=171602614

이름: 씽크톡톡 윈도우10 & 인터넷 기초/웰북교재연구회 지음/웰북(WellBook)
링크 http://www.aladin.co.kr/rsscenter/go.aspx?rssType=2&type=item&itemId=171601667 ... ...
```



## 데이터베이스에 저장

- 데이터베이스 저장하면 여러개의 프로세스에서 동시에 읽고 쓰기 가능
- 데이터의 중복 방지
- 데이터 분석에서 조건에 맞는 데이터만 추출
- 관계형 데이터베이스
  - 관계 모델과 트랜젝션으로 데이터의 정합성 보장
  - 표준화된 SQL구문 이용 => 유연한 데이터 관리
  - MySQL
- NoSQL: 데이터의 정합성이 약한 대신 확장성과 읽고 쓰기 성능이 좋은 데이터베이스
  - MongoDB

### MySQL

- 관계형 데이터베이스
- 클라이언트/서버형 아키텍쳐 채용
- 설치

```
brew install mysql

#서버 실행
mysql.server start
Starting MySQL
 SUCCESS!
mysql.server status
```

- 데이터베이스와 사용자 만들기

  ```
  mysql -u root -p
  Enter password:
  #mac일 경우 그냥 enter, 우분투일때는 우분투 접속 비밀번호
  
  #기본문자코드를 utf8mb4(4바이트 지원 UTF-8)로 설정
  mysql> CREATE DATABASE scraping DEFAULT CHARACTER SET utf8mb4;
  Query OK, 1 row affected (0.00 sec)
  
  #localhost에서 접속 가능한 사용자 scraper를 생성하고 비밀번호를 password로 설정
  mysql> CREATE USER scraper@localhost IDENTIFIED BY '1234';
  Query OK, 0 rows affected (0.00 sec)
  
  #오류!
  ERROR 1396 (HY000): Operation CREATE USER failed for 'scraper'@'localhost' 나올때
   drop user scraper@localhost;
   flush privileges;
  해준 뒤에 다시 USER 시도 
  
  #사용자 scraper에게 데이터 scraping을 읽고 쓸 수 있는 권한 부여
  mysql> GRANT ALL On scraping.* To scraper@localhost IDENTIFIED BY '1234';
  Query OK, 0 rows affected, 1 warning (0.05 sec)
  ```


## 파이썬에서 MySQL 접속

- mysqlclient사용
- 설치
- pip3를 하는 이유: mysql에서 데이터를 불러올때 문자가 깨진다
  - 인터넷에서 찾아본 결과 python2는 문자열과 유니코드가 서로다르고, python3에서는 문자열과 유니코드가 같게 처리된다.
  - (1L, u'\uc0c1\ud558\uc774', 100L) => 이런식

```
pip3 install mysqlclient
```

```
msysql scraping -u root -p -e 'SELECT * FROM cities'
+------+--------------+------------+
| rank | city         | population |
+------+--------------+------------+
|    1 | 상하이       	 |        100 |
|    2 | 카라치         |         99 |
|    3 | 베이징         |         98 |
|    4 | 텐진          |         97 |
|    5 | 이스탄불       |         96 |
+------+--------------+------------+
```

```python
#_*_coding:utf-8_*_

import MySQLdb

conn = MySQLdb.connect(db='scraping', user='scraper', passwd='1234', charset='utf8mb4')

#커서 추출
c = conn.cursor()

#execute()메서드로 SQL 구문 실행
c.execute('DROP TABLE IF EXISTS cities')

c.execute('''
    CREATE TABLE cities(
        rank integer,
        city text,
        population integer
    )
''')

#execute()메서드의 두번째 매개변수에는 파라미터를 지정할 수 있음
#SQL 내부에서 파라미터로 변경할 부분(플레이스홀더)은 %s로 지정
c.execute('INSERT INTO cities VALUES (%s, %s, %s)', (1, '상하이', 100))

#파라미터가 딕셔너리일 대는 플레이스 홀더를 %(<이름>)s 형태로 지정
c.execute('INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)', {'rank':2, 'city':'카라치', 'population':99})

#excutemany()메서드로 파라미터를 리스트로 지정가능
c.executemany('INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)',
[
    {'rank':3, 'city':'베이징', 'population':98},
    {'rank':4, 'city':'텐진', 'population':97},
    {'rank':5, 'city':'이스탄불', 'population':96},
])


#commit 저장
conn.commit()

#저장한 데이터 추출
c.execute('SELECT * FROM cities')

#쿼리 결과는 fetchall() 메서드로 추출
for row in c.fetchall():
    print(row)

#연결 종료
conn.close()

#결과
(1, '상하이', 100)
(2, '카라치', 99)
(3, '베이징', 98)
(4, '텐진', 97)
(5, '이스탄불', 96)
```



## MongoDB에 데이터 저장하기

- NoSQL의 일종
- 문서형이라고 부르는 데이터베이스
- 유연한 데이터 구조, 높은 쓰기 성능, 쉬운 사용법
- 하나의 데이터베이스는 여러 콜렉션을 가지고 있음
- 콜렉션 안에는 여러개의 문서(BSON이라고 부름 => JSON의 바이너리 형식)가 존재함
- 문서는 내부에서 필요한 데이터항목을 다룰 수 있어 문서마다 데이터 항목이 다를 수 있음
- 대량의 크롤링/스크레이핑 병목현상발생을 줄일 수 있음
- 설치

```
brew install mongodb

#기본 데이터베이스 디렉터리인 /data/db생성
#-p는 부모 디렉터리가 없을 경우 강제로 생성
mkdir -p /data/db

#MongoDB를 포그라운드에서 실행
mongod
```

#### 파이썬에서 MongoDB에 접속하기

```
pip install pymongo
```

```python
#pymongoDB.py
#_*_coding:utf-8_*_
from pymongo import MongoClient

#호스트 이름과 포트 번호를 지정해서 접속
client = MongoClient('localhost', 27017)

#test 데이터베이스 추출.
db = client.test
db = client['test']

#데이터베이스의 sports 콜렉션을 추출. 콜렉션이 존재하지 않으면 자동으로 생성
collection = db.sports
collection = db['spots'] 

#insert_one() 메서드로 딕셔너리를 콜렉션에 삽입
collection.insert_one({'name': 'N서울타워', 'prefecture': '서울'})

#insert_many()메서드로 여러 개의 딕셔너리를 콜렉션에 삽입
collection.insert_many([{'name': '첨성대', 'prefecture': '경주'}, {'name': '롯데월드타워', 'prefecture': '서울'}])

#find() 메서드를 사용해 문서를 추출하는 Cursor 객체 추출
#모든 문서에는 _id 필드가 자동으로 붙으며, 해당 값은 ObjectId라고 하는 12바이트 식별자
collection.find()

#Cursor 객체는 for 구문으로 반복할 수 있음
for sopt in collection.find():
    print(sopt)
#결과
{'_id': ObjectId('5bd086f8f374fb83bab55900'), 'prefecture': '서울', 'name': 'N서울타워'}
{'_id': ObjectId('5bd086f8f374fb83bab55901'), 'prefecture': '경주', 'name': '첨성대'}
{'_id': ObjectId('5bd086f8f374fb83bab55902'), 'prefecture': '서울', 'name': '롯데월드타워'}
    
#find()메서드의 매개변수로 쿼리를 지정하면 해당 쿼리에 맞는 문서가 추출됨
for spot in collection.find({'prefecture': '서울'}):
    print(spot)
    
#결과
{'_id': ObjectId('5bd086f8f374fb83bab55900'), 'prefecture': '서울', 'name': 'N서울타워'}
{'_id': ObjectId('5bd086f8f374fb83bab55902'), 'prefecture': '서울', 'name': '롯데월드타워'}
d'), 'name': 'N서울타워', 'prefecture': '서울'}
```

```python
#save_mongo.py
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
    
#결과
5bd089b2f374fb863eddf176 http://www.hanbit.co.kr/media/ 한빛미디어
5bd089b2f374fb863eddf177 http://www.hanbit.co.kr/academy/ 한빛아카데미
5bd089b2f374fb863eddf178 http://www.hanbit.co.kr/biz/ 한빛비즈
5bd089b2f374fb863eddf179 http://www.hanbit.co.kr/life/ 한빛라이프
5bd089b2f374fb863eddf17a http://www.hanbit.co.kr/edu/ 한빛에듀
5bd089b2f374fb863eddf17b http://www.hanbit.co.kr/realtime/ 리얼타임
5bd089b2f374fb863eddf17c http://www.hanbit.co.kr/textbook/ 한빛정보교과서
5bd089b2f374fb863eddf17d http://www.hanbit.co.kr/rent/ 한빛대관서비스
```

### MongoDB 데이터 확인 프로그램

- 3T MongoChef(http://3t.io/mongochef/)
- MongoBooster(http://mongobooster.com/)
- Mongoclient(http://www.mongoclient.com/)
- Robomongo(https://robomongo.org/)