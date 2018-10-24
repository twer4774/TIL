#-*-encoding:UTF-8-*-
import requests
r = requests.get('http://hanbit.co.kr')
print(type(r))

print(r.status_code)

#headers 속성으로 HTTP 헤더를 딕셔너리로 추출
print(r.headers['content-type'])

print(r.encoding)

# #str 자료형으로 디코딩된 응답 본문 추출
print(r.text)

# #content 속성으로 bytes wkfyguddml dmdekq qhsans cncnf
# print(r.content)
