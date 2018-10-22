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