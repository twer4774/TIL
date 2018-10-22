#-*-encoding:UTF-8-*-
import re
import sqlite3
from urllib.request import urlopen
from html import unescape

def main():
    """
    메인 처리
    """
    html = fetch('http://www.hanbit.co.kr/store/books/full_book_list.html')
    books = scrape(html)
    save('books.db', books)

def fetch(url):
    """url 기반으로 웹페이지 추출"""
    f = urlopen(url)
    encoding = f.info().get_content_charset(failobj="utf-8")
    html = f.read().decode(encoding)
    return html

def scrape(html):
    """정규표현식으로 도서 정보 추출"""
    books = []

    for partial_html in re.findall(r'<td class="left">Ma.*?</td>', html, re.DOTALL):
        #도서의 URL 추출
        url = re.search(r'<a href="(.*?)">', partial_html).group(1)
        url = 'http://www.hanbit.co.kr' + url
        #태그를 제거해 도서의 제목 추출
        title = re.sub(r'<.*?>', '', partial_html)
        title = unescape(title)
        books.append({'url': url, 'title': title})

    return books

def save(db_path, books):
    """sqlite로 저장"""
    
    conn = sqlite3.connect(db_path)

    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS books')
    c.execute('''CREATE TABLE books( title text, url text) ''')

    c.executemany('INSERT INTO books VALUES (:title, :url)', books)
    conn.commit()
    conn.close()

#python명령어로 실행한 경우 main() 함수 호출
if __name__ == '__main__':
    main()
