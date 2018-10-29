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
