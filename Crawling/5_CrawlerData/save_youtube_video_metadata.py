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