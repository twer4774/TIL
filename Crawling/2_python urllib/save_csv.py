#-*-encoding:UTF-8-*-
import csv

with open('top_cities.csv', 'w', newline='') as f:
    #csv.writer는 파일 객체를 매개 변수로 지정
    writer = csv.writer(f)
    #첫번째 줄에는 헤더 작성
    writer.writerow(['rank', 'city', 'population'])

    writer.writerows([
        ['1', '상하이', '24150000'],
        ['2', '카라치', '23500000'],
        ['3', '베이징', '21515500'],
        ['4', '텐진', '124596990'],
        ['5', '이스탄불', '11102223']
    ])

