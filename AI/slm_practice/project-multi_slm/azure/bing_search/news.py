import re
import requests
import aiohttp

from .. import get_auth

class News:
    def __init__(self) -> None:
        auth = get_auth()
        self.url_search = "https://api.bing.microsoft.com/v7.0/search?"
        self.url_top = 'https://api.bing.microsoft.com/v7.0/news'
        self.headers = {'Ocp-Apim-Subscription-Key': auth['Bing_Search']['key']}
        self.params = {
            'mkt' : 'ko-KR',
            'freshness': 'Week'
        }

    def search (
            self,
            query: str,
            count: int=3,
    ) -> list:
        
        for keyword in ['오늘', '주요', '뉴스']:
            query = query.replace(keyword, "").strip()

        if query == '':
            endpoint = self.url_top
        else:
            endpoint = self.url_search
            self.params['q'] = f"{query}"
        self.params['count'] = count
        search_result = requests.get(
            endpoint,
            headers=self.headers,
            params=self.params
        ).json()['webPages']['value']

        documents = []
        for res in search_result:
            title = res.get('name', 'no title')
            url = res.get('url', '')
            snippet = re.sub(
                r"\[.*?\]", "",
                res.get("snippet", "no content")
            )
            documents.append({
                'title': title,
                'snippet': snippet,
                'url': url
            })

        return documents

        
