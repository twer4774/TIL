#pip3 install voluptuous
from voluptuous import Schema, Match

# 다음의 큐칙들을 가진 스키마 정의
schema = Schema({   #규칙1: 객체는 dict 자료형
    'name': str,    #규칙2: name은 str자료형
    'price': Match(r'^[0-9,]+$'), #규치3: price가 정규 표현식에 맞는지 확인
}, required=True)   #rbclr4: dict의 키는 필수

#Schema 객체는 함수처럼 호출해서 사용
#매개변수에 대상을 넣으면 유효성 검사를 수행
# schema({
#     'name': '포도',
#     'price': '3,000',
# }) #유효성 검사를 통과하므로 아무 문제 없음

schema({
    'name': None,
    'price': '3,000',
}) #유효성 검사를 통과하지 못하므로, MultipleInvalid 예외 발생