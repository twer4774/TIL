#-*-encoding:UTF-8-*-
import json

cities = [
    {'rank': 1, 'city': '상하이', 'population': 100},
    {'rank': 2, 'city': '카라치', 'population': 99},
    {'rank': 3, 'city': '베이징', 'population': 98},
    {'rank': 4, 'city': '텐진', 'population': 97},
    {'rank': 5, 'city': '이스탄불', 'population': 96},
]

#ASCII이외의 문자열을 \uxxxx라는 형태로 이스케이프 하지 않고 출력
#indent=2로 2개의 고백으로 들여쓰기 해줌
print(json.dumps(cities, ensure_ascii=False, indent=2))