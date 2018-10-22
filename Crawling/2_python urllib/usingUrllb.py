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