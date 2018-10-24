#-*-encoding:UTF-8-*-
from bs4 import BeautifulSoup

#HTML 파일을 읽어 들이고 BeautifulSop 객체 생성
with open('full_book_list.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

#find_all()메서드로 a요소 우출후 반복문 실행
for a in soup.find_all('a'):
    #href 속성과 글자 추출
    print(a.get('href'), a.text)