import os
import re
import yaml
import requests
import openai
from openai.embeddings_utils import get_embedding, get_embeddings
import hashlib
import json

from .. import get_auth

class AISearch:
    """MS AZURE DB 관리하는 클래스"""
    def __init__(self) -> None:

        auth = get_auth()
        self.base_url = f"https://{auth['AI_Search']['name']}.search.windows.net"
        self.index_name = auth['AI_Search']['index_name']
        self.api_version = '2023-11-01'
        self.header = {"Content-Type": "application/json", "api-key": auth['AI_Search']['key']}

    def upload(self, data: list[dict]) -> None:
        
        context_embs = get_embeddings([d['context'] for d in data], engine='embedding')
        for d, context_emb in zip(data, context_embs):
            id = hashlib.sha1(d['context'].encode()).hexdigest()
            d['id'] = id
            d['context_vector'] = context_emb
            d['@search.action'] = 'upload'

        url = f'{self.base_url}/indexes/{self.index_name}/docs/index?api-version={self.api_version}'
    
        res = requests.post(
            url=url, 
            headers=self.header, 
            data=json.dumps({"value": data})
        )

        if res.status_code == 200:
            print('Upload Success')
        else:
            print('Upload Fail')
    
        return res

    def search(
        self,
        query: str,
        file_name: str,
        topk: int = 3,
    ) -> list[dict]:

        query_vector = get_embedding(query, engine='embedding')
        body = {
            "select": "id, context",
            "search": query,
            "filter": f"file_name eq '{file_name}'",
            "vectorFilterMode": "preFilter",
            "vectorQueries": [
                {
                    "kind": "vector",
                    "vector": query_vector,
                    "exhaustive": True,
                    "fields": "context_vector",
                    "k": topk
                }
            ]
        }

        url = f'{self.base_url}/indexes/{self.index_name}/docs/search?api-version={self.api_version}'
        res = requests.post(
            url=url, 
            headers=self.header, 
            data=json.dumps(body)
        )
    
        if res.status_code == 200 :
            print("Search Success")
            return res.json()['value'][:topk]
        else:
            print("Search Fail")
            return []

    def delete(self, ids:list[str]) -> None:
        url = f'{self.base_url}/indexes/{self.index_name}/docs/index?api-version={self.api_version}'

        docs = {"value": [{"@search.action": "delete", "id": i} for i in ids]}

        res = requests.post(
            url=url, 
            headers=self.header, 
            data=json.dumps(docs)
        )

        if res.status_code == 200:
            print('Delete Success!')
        else:
            print('Delete Fail!')