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