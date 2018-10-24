#-*-coding:UTF-8-*-
import feedparser

d = feedparser.parse('http://www.aladin.co.kr/rss/new_all/351')

for entry in d.entries:
    print('이름:', entry.title)
    print('링크', entry.link)
    print()