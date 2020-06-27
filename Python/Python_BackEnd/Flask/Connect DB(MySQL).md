# Connect DB(MySQL)

### SQLAlchemy

- ORM(Object Relational Mapper) : 파이썬과 DB를 연결해준다.

### MySQL-Connector

- 파이썬과 MySQL을 연결하기 위한 DB API(파이썬 공식 홈페이지에서 권장)

  

## 설치

```
pip install sqlalchemy
pip install mysql-connector-python
```

## 사용

- sqlalchemy

```python
from sqlalchemy import create_engine, text # creat_engine으로 연결을 생성, text로 sql문을 실행하게 만듦

db = {
  'user' : 'root',
  'password' : '1234',
  'host' : 'localhost',
  'port' : 3306, #대부분 RDBM은 3306포트 이용
  'database' : 'dbname'
}

db_url = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}?charset=utf8"
db = create_engine(db_url, encoding = 'utf-8', max_overflow = 0)

params = {'name' : 'walter'}
rows = db.execute(text("SELECT * FROM users WHERE name = :name"), params).fetchall() #fetchall로 리스트형태로 리턴

for row in rows:
  print(f"name : {row['name']}")
  print(f"email : {row['email']}")
```

