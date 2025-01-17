# Azure 리소스 만들기 > marketplace > bing search v7
import re
import requests
import aiohttp

from .. import get_auth

class Web:
    def __init__(self) -> None:
        auth = get_auth()
        self.endpoint = "https://api.bing.microsoft.com/v7.0/search?"
        self.headers = {'Ocp-Apim-Subscription-Key': auth['Bing_Search']['key']}
        self.params = {
            'mkt' : 'ko-KR',
            'responseFilter': 'Webpages',
            'safeSearch': 'Strict'
        }

    def search (
            self,
            query: str,
            count: int=3,
    ) -> list:
        
        self.params['q'] = query
        self.params['count'] = count

        search_result = requests.get(
            self.endpoint,
            headers=self.headers,
            params=self.params
        ).json()


        
        documents = []
        for res in search_result:
            title = res.get('name', 'no')
            url = res.get('url', '')
            snippet = re.sub(
                r"\[.*?\]", "",
                res.get('snippet', 'no')
            )
            documents.append(
                {
                    'title' : title,
                    'snippet' : snippet,
                    'url' : url
                }
            )

        return documents
