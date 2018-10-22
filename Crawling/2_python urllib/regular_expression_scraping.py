#-*-encoding:UTF-8-*-
import re

print(re.search(r'a.*c', 'abc123DEF'))

#세번째 매개변수로 옵션 지정. re.IGNORECASE(or re.I) => 대소문자 무시
print(re.search(r'a.*d', 'abc123DEF', re.IGNORECASE))

#Match 객체의 group()메서드로 일치한 값을 추출
#매개변수에 0을 지정하면 매치된 모든 값을 반환
m = re.search(r'a(.*)c', 'abc123DEF')
print(m.group(0))

#re.findall()함수로 정규표현식에 맞는 모든 부분 추출
#\w는 유니코드로 글자를 비교. 공백 문자는 \s로 추출 가능
print(re.findall(r'\w{2,}', 'This is a pne'))


print(re.sub(r'\w{2,}', 'That', 'This is a pen'))