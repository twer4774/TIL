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
# for sopt in collection.find():
#     print(sopt)

#find()메서드의 매개변수로 쿼리를 지정하면 해당 쿼리에 맞는 문서가 추출됨
for spot in collection.find({'prefecture': '서울'}):
    print(spot)
