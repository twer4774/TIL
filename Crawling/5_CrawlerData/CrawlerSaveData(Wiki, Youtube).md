# 데이터 세트 추출

### 위티백과 데이터 세트 다운로드

- 데이터 세트 - 크롤링해서 서버에 부하를 주는 대신 데이터 세트를 제공해 서버 부하를 줄임
- https://dumps.wikimedia.org/kowiki/

```
wget https://dumps.wikimedia.org/kowiki/20180601/kowiki-20180601-pages-articles-multistream.xml.bz2

#WikiExtractor라는 파이썬 스크립트를 사용함
wget https://github.com/attardi/wikiextractor/raw/master/WikiExtractor.py
```

- WikiExtractor.py를 실행하면 위키백과 덤프 파일을 텍스트로 변환 -> 너무 많이 나옴..
- --no-templates: 페이지 앞의 템플릿을 생략
- -o: 출력 대상 디렉터리를 지정
- -b: 분할할 파일크기를 지정

```
python WikiExtractor.py --no-templates -o articles -b 100M kowiki-20180601-pages-articles-multistream.xml
```

### 자연어 처리를 사용한 빈출 단어 추출

- 파이썬 한국어 형태소 분석 라이브러리 KoNILPy
- KoNILPy는 내부적으로 자바로 이루어짐

```
#KoNILPy 설치
pip3 install konlpy
pip3 install jpype1
```

```python
#konlpy_sample.py
from konlpy.tag import Kkma

kkma = Kkma()
malist = kkma.pos("아버지 가방에 들어가신다.") #형태소 분석
print(malist)

#결과 <형태소>, <품사> 품사의 의미는 http://kkma.snu.ac.kr/documents/?doc=postag
[('아버지', 'NNG'), ('가방', 'NNG'), ('에', 'JKM'), ('들어가', 'VV'), ('시', 'EPH'), ('ㄴ다', 'EFN'), ('.', 'SF')]
```



## 유튜브에서 동영상 정보 수집하기

- API이용
- 댓글 이용에는 OAuth 인증이 필요하지만, 동영상 검색 또는 채널 내용확인은 API키 만으로 가능
- 동영상 자체는 추출 불가능하지만, 동영상과 관련된 메타데이터 추출 가능

#### API키 추출

- 구글 계정 필요
- console.developer.google.com 접속 후 프로젝트 생성(구글에선 리소스를 프로젝트로 관리함)
- API 중 "Youtube Data API" 선택 후 사용설정
- 사용자 인증정보 만들기로 Key 생성
- curl 명령어로 Youtube Data API 사용하기

```
curl "https://www.googleapis.com/youtube/v3/search?key=<API 키>&part=snippet&q=축구&type=video"

#결과
{
 "kind": "youtube#searchListResponse",
 "etag": "\"XI7nbFXulYBIpL0ayR_gDh3eu1k/ZHUWV1mzuc99d6gHX-Wm4OoW6Es\"",
 "nextPageToken": "CAUQAA",
 "regionCode": "KR",
 "pageInfo": {
  "totalResults": 695199,
  "resultsPerPage": 5
 },
 "items": [
  {
   "kind": "youtube#searchResult",
   "etag": "\"XI7nbFXulYBIpL0ayR_gDh3eu1k/JQ16jR1aogg3yIj2qKWjyJiHTbM\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "agIf-9rhuZM"
   },
   "snippet": {
    "publishedAt": "2018-10-27T03:00:00.000Z",
    "channelId": "UCudWn3bvgyuEw-rTD7zJZOg",
    "title": "가장 창의적인 축구 선수 TOP 5",
    "description": "구독과 좋아요는 큰힘이 됩니다~! 이메일:Philfritz@naver.com.",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/agIf-9rhuZM/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/agIf-9rhuZM/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/agIf-9rhuZM/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "No.1 스포츠채널 불양TV",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"XI7nbFXulYBIpL0ayR_gDh3eu1k/ZkBQ8BIp2f500zpzDkHXfRDe-i4\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "RwWx5pKS3eA"
   },
   "snippet": {
    "publishedAt": "2018-09-01T14:52:47.000Z",
    "channelId": "UCMEbRpvuwTbXxGiyDb1mT8w",
    "title": "★한일전 명장면 대방출★ 한국축구 금메달, 아시안게임 2연패 달성! / 비디오머그",
    "description": "아시안게임 남자 축구 결승에서 한국이 숙적 일본을 2:1로 꺾고 우승했습니다. 치열한 공방 속에 정규시간 90동안 승부를 못낸 양팀은 연장전에...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/RwWx5pKS3eA/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/RwWx5pKS3eA/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/RwWx5pKS3eA/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    }, ... ...
```

#### Goolge API Client for Python 사용하기

- Requests 라이브러리를 사용해도 되지만, 구글에서 제공하는 Google API Client for Python을 이용함

- API키를 .env에 넣어서 활용하는 방법

  - .env 파일을 생성한다(vim or nano)

  - 이것을 .gitignore에 추가하면 키 관리가 수월해짐

  - ```
    #.env
    YOUTUBE_API_KEY = <발급 받은 API 키>
    ```

- .env 같은 스크립트 파일을 읽기 위해 forego를 설치한다

- brew install forego

```python
#-*-coding:UTF-8-*-
import os

#pip3 install google-api-python-client
from apiclient.discovery import build
#환경변수에서 API키 추출
YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']

#Youtube API 클라이언트 생성
#build()함수의 첫번째 매개변수에는 API 이름, 두번째 매개변수에는 API 버전 지정
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

#키워드를 매개변수로 매지정하고 serach.list 메서드 호출
search_response = youtube.search().list(
    part='snippet',
    q='축구',
    type='video',
).execute()

for item in search_response['items']:
    #동영상 제목 출력
    print(item['snippet']['title'])

#결과
가장 창의적인 축구 선수 TOP 5
★한일전 명장면 대방출★ 한국축구 금메달, 아시안게임 2연패 달성! / 비디오머그
최고의 팬서비스 TOP 10 축구선수
[2018 아시안게임 축구] 금메달까지 전체 과정 하이라이트 ⚽ (HD)
이 공은 절대 터지지 않는 신기한 축구공입니다
```

#### 동영상의 메타 정보 추출

```
curl "https://www.googleapis.com/youtube/v3/videos?key=<API 키>&id=agIf-9rhuZM&part=snippet,statistics"
#결과
"statistics": {
    "viewCount": "299689",
    "likeCount": "2141",
    "dislikeCount": "87",
    "favoriteCount": "0",
    "commentCount": "597"
```

#### 동영상 정보를 MongoDB에 저장하고 검색

- 조회수가 많은 상위 3개 출력

```python
#save_youtube_video_metadata.py
import os
import sys

from apiclient.discovery import build
from pymongo import MongoClient, DESCENDING

#환경변수에서 API 키 추출
YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']

def main():
    mongo_client = MongoClient('localhost', 27017)
    collection = mongo_client.youtube.videos
    collection.delete_many({})

    #동영상을 검색, 페이지 단위로 아이템 목록에 저장
    for items_per_page in search_videos('야구'):
        save_to_mongodb(collection, items_per_page)

    #뷰 수가 높은 동영상 출력
    show_top_videos(collection)

def search_videos(query, max_pages=5):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    search_request = youtube.search().list(
        part='id',
        q=query,
        type='video',
        maxResults = 50,
    )

    i=0
    while search_request and i < max_pages:
        search_response = search_request.execute()
        video_ids=[item['id']['videoId'] for item in search_response['items']]

        videos_response = youtube.videos().list(
            part='snippet,statistics',
            id=','.join(video_ids)
        ).execute()

        yield videos_response['items']

        search_request = youtube.search().list_next(search_request, search_response)
        i+=1

def save_to_mongodb(collection, items):
    for item in items:
        item['_id'] = item['id']
        for key, value in item['statistics'].items():
            item['statistics'][key] = int(value)

    result = collection.insert_many(items)
    print('Inserted {0} documents'.format(len(result.inserted_ids)), file=sys.stderr)

def show_top_videos(collection):
    for item in collection.find().sort('statistics.viewCont', DESCENDING).limit(3):
        print(item['statistics']['viewCount'], item['snippet']['title'])

if __name__ == '__main__':
    main()
    
#결과 forego run python3 save_youtube_vidoe_metadata.py
10002 [2018 프로야구] 넥센 vs SK PO 2차전 경기 하이라이트 (10.28)
19595 [2018 프로야구] 넥센 vs SK PO 1차전 경기 하이라이트 (10.27)
13401 [2018 프로야구] 한화 vs 넥센 준PO 4차전 경기 하이라이트 (10.23)
```

