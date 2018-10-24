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